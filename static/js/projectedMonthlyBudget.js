document.addEventListener('DOMContentLoaded', function () {

    // ── Account type metadata ─────────────────────────────────────────────
    const ACCOUNT_INFO = {
        general: null,
        '401k': {
            name: '401(k)',
            annualLimit: 23000,
            taxNote: 'Pre-tax contributions reduce your taxable income now. Growth is tax-deferred until withdrawal.',
            incomeLimitNote: null,
            hasEmployerMatch: true,
        },
        roth_ira: {
            name: 'Roth IRA',
            annualLimit: 7000,
            taxNote: 'After-tax contributions. Growth and qualified withdrawals are completely tax-free.',
            incomeLimitNote: 'Income limits apply: phase-out begins at $146,000 (single) / $230,000 (married) for 2024. Check IRS guidelines for eligibility.',
            hasEmployerMatch: false,
        },
        traditional_ira: {
            name: 'Traditional IRA',
            annualLimit: 7000,
            taxNote: 'Contributions may be tax-deductible depending on your income and workplace plan. Growth is tax-deferred.',
            incomeLimitNote: 'Deductibility may be limited if you or your spouse have a workplace retirement plan. Check IRS guidelines.',
            hasEmployerMatch: false,
        },
    };

    let chart1 = null;
    let chart2 = null;

    // ── Shared helpers ────────────────────────────────────────────────────

    function updateAccountBanner(prefix) {
        const type = document.getElementById(prefix + '-account-type').value;
        const info = ACCOUNT_INFO[type];
        const banner = document.getElementById(prefix + '-account-banner');
        const matchRow = document.getElementById(prefix + '-match-row');

        if (info) {
            let html = '<strong>' + info.name + ':</strong> ' + info.taxNote;
            if (info.annualLimit) {
                html += ' Annual IRS contribution limit: <strong>$' + info.annualLimit.toLocaleString() + '</strong>.';
            }
            if (info.incomeLimitNote) {
                html += '<br><span class="account-banner-income">' + info.incomeLimitNote + '</span>';
            }
            banner.innerHTML = html;
            banner.style.display = 'block';
        } else {
            banner.style.display = 'none';
        }

        if (matchRow) {
            matchRow.style.display = (info && info.hasEmployerMatch) ? 'flex' : 'none';
        }
    }

    function buildChart(canvasId, chartRef, labels, data) {
        if (chartRef) chartRef.destroy();
        const ctx = document.getElementById(canvasId).getContext('2d');
        return new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Projected Savings ($)',
                    data: data,
                    borderColor: '#18a558',
                    backgroundColor: 'rgba(24,165,88,0.1)',
                    fill: true,
                    tension: 0.3,
                    pointRadius: 0,
                    pointHoverRadius: 5,
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        callbacks: {
                            label: function (ctx) {
                                return '$' + ctx.parsed.y.toLocaleString(undefined, { minimumFractionDigits: 2 });
                            }
                        }
                    }
                },
                scales: {
                    x: {
                        type: 'linear',
                        title: { display: true, text: 'Number of Months' },
                        ticks: { stepSize: 6 }
                    },
                    y: {
                        title: { display: true, text: 'Amount ($)' },
                        beginAtZero: true,
                        ticks: { callback: function (v) { return '$' + v.toLocaleString(); } }
                    }
                }
            }
        });
    }

    function showLimitWarning(warningEl, accountType, annualContrib) {
        const info = ACCOUNT_INFO[accountType];
        if (info && info.annualLimit && annualContrib > info.annualLimit) {
            const over = (annualContrib - info.annualLimit).toLocaleString(undefined, { minimumFractionDigits: 2 });
            warningEl.innerHTML =
                '&#9888;&#65039; Your projected annual contribution (<strong>$' + annualContrib.toLocaleString() + '/yr</strong>) ' +
                'exceeds the <strong>' + info.name + ' limit of $' + info.annualLimit.toLocaleString() + '/yr</strong> ' +
                'by $' + over + '. Consider adjusting your timeline or splitting the overage into a taxable brokerage account.';
            warningEl.style.display = 'block';
        } else {
            warningEl.style.display = 'none';
        }
    }

    // ── Savings Calculator ────────────────────────────────────────────────
    // Target amount + date → monthly contribution needed

    document.getElementById('calc1-account-type').addEventListener('change', function () {
        updateAccountBanner('calc1');
    });

    document.getElementById('submitSavingsGoal').addEventListener('click', function (e) {
        e.preventDefault();
        const savingsGoal  = document.getElementById('savingsGoal').value.trim();
        const goalDate     = document.getElementById('goalDate').value;
        const interestRate = document.getElementById('interestRate').value.trim();
        const accountType  = document.getElementById('calc1-account-type').value;

        if (!savingsGoal)  { alert('Please enter a target amount.'); return; }
        if (!goalDate)     { alert('Please enter a target date.'); return; }
        if (!interestRate) { alert('Please enter an interest rate.'); return; }

        const btn = this;
        btn.disabled = true;
        btn.textContent = 'Calculating...';

        fetch('/budgets/projected-budget/' + savingsGoal + '/' + interestRate + '/' + goalDate + '/')
            .then(function (r) { return r.json(); })
            .then(function (data) {
                btn.disabled = false;
                btn.textContent = 'Calculate';
                if (data.error) { alert(data.error); return; }

                const monthly = data['projected amount per month'];
                const info = ACCOUNT_INFO[accountType];

                // Employer match (401k)
                let matchMonthly = 0;
                if (info && info.hasEmployerMatch) {
                    const matchRate = parseFloat(document.getElementById('calc1-match-rate').value) || 0;
                    const matchCap  = parseFloat(document.getElementById('calc1-match-cap').value) || Infinity;
                    matchMonthly = Math.min(monthly * (matchRate / 100), matchCap);
                }

                // Build result
                let resultHTML = 'You need to save <strong>$' + monthly.toLocaleString() + '/month</strong>';
                if (matchMonthly > 0) {
                    const effective = (monthly + matchMonthly).toFixed(2);
                    resultHTML += ' — plus your employer contributes <strong>$' + matchMonthly.toFixed(2) +
                        '/month</strong>, making your effective monthly total <strong>$' + effective + '</strong>';
                }
                resultHTML += ' to reach your goal.';
                document.getElementById('calc1-result').innerHTML = resultHTML;

                // Limit warning
                showLimitWarning(
                    document.getElementById('calc1-limit-warning'),
                    accountType,
                    monthly * 12
                );

                // Show result section + chart
                document.getElementById('calc1-result-section').style.display = 'block';
                document.getElementById('calc1-chart-card').style.display = 'block';
                chart1 = buildChart('savingsGoalChart', chart1, data.labels, data.data);
            })
            .catch(function (err) {
                console.error('Calculator error:', err);
                btn.disabled = false;
                btn.textContent = 'Calculate';
            });
    });

    // ── Deposit Planner ───────────────────────────────────────────────────
    // Monthly deposit → time to reach target

    document.getElementById('calc2-account-type').addEventListener('change', function () {
        updateAccountBanner('calc2');
    });

    document.getElementById('submitDepositGoal').addEventListener('click', function (e) {
        e.preventDefault();
        const monthlyDeposit = document.getElementById('savingsAmount').value.trim();
        const goalAmount     = document.getElementById('goalAmount').value.trim();
        const interestRate   = document.getElementById('interestRate2').value.trim();
        const accountType    = document.getElementById('calc2-account-type').value;

        if (!monthlyDeposit || isNaN(monthlyDeposit)) { alert('Please enter a valid monthly deposit.'); return; }
        if (!goalAmount     || isNaN(goalAmount))      { alert('Please enter a valid goal amount.'); return; }
        if (!interestRate   || isNaN(interestRate))    { alert('Please enter a valid interest rate.'); return; }

        // Employer match for 401k — boosts effective deposit
        const info = ACCOUNT_INFO[accountType];
        let effectiveDeposit = parseFloat(monthlyDeposit);
        let matchMonthly = 0;
        if (info && info.hasEmployerMatch) {
            const matchRate = parseFloat(document.getElementById('calc2-match-rate').value) || 0;
            const matchCap  = parseFloat(document.getElementById('calc2-match-cap').value) || Infinity;
            matchMonthly = Math.min(effectiveDeposit * (matchRate / 100), matchCap);
            effectiveDeposit += matchMonthly;
        }

        const btn = this;
        btn.disabled = true;
        btn.textContent = 'Calculating...';

        fetch('/budgets/monthly-deposit-project/' + effectiveDeposit + '/' + goalAmount + '/' + interestRate + '/')
            .then(function (r) { return r.json(); })
            .then(function (data) {
                btn.disabled = false;
                btn.textContent = 'Calculate';
                if (data.error) { alert(data.error); return; }

                const years  = Math.floor(data.months / 12);
                const months = Math.ceil(data.months % 12);
                let timeStr;
                if (years === 0)       timeStr = data.months + ' months';
                else if (months === 0) timeStr = years + ' year' + (years > 1 ? 's' : '');
                else                   timeStr = years + ' year' + (years > 1 ? 's' : '') + ' and ' + months + ' month' + (months > 1 ? 's' : '');

                let resultHTML = '<strong>' + timeStr + '</strong> to reach your goal';
                if (matchMonthly > 0) {
                    resultHTML += ' — using an effective contribution of <strong>$' + effectiveDeposit.toFixed(2) +
                        '/month</strong> ($' + parseFloat(monthlyDeposit).toFixed(2) +
                        ' yours + $' + matchMonthly.toFixed(2) + ' employer match)';
                }
                resultHTML += '.';
                document.getElementById('calc2-result').innerHTML = resultHTML;

                // Limit warning (based on user's own deposit, not effective)
                showLimitWarning(
                    document.getElementById('calc2-limit-warning'),
                    accountType,
                    parseFloat(monthlyDeposit) * 12
                );

                document.getElementById('calc2-result-section').style.display = 'block';
                document.getElementById('calc2-chart-card').style.display = 'block';
                chart2 = buildChart('projectedChart', chart2, data.labels, data.data);
            })
            .catch(function (err) {
                console.error('Calculator error:', err);
                btn.disabled = false;
                btn.textContent = 'Calculate';
            });
    });

});
