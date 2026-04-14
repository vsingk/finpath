"""
Full article content for the Learn section.
Each article dict includes:  body (HTML string) and references (list of dicts).
"""

ARTICLES = [
    {
        'slug': 'first-paycheck',
        'category': 'Taxes',
        'category_color': 'blue',
        'title': 'Your First Paycheck: Why It Looks Smaller Than You Expected',
        'summary': 'You negotiated $60,000 — so why did only $3,800 hit your account? A quick breakdown of federal tax, FICA, state tax, and pre-tax deductions so nothing surprises you.',
        'read_time': '4 min',
        'tags': ['taxes', 'paycheck', 'beginner'],
        'body': """
<p>You accepted the offer, did the math on your annual salary, and were ready to celebrate. Then your first direct deposit landed and it was hundreds of dollars less than you expected. You're not getting cheated — this is just how payroll works. Here's exactly where your money goes.</p>

<h3>Gross Pay vs. Net Pay</h3>
<p>Your salary is your <strong>gross pay</strong> — the number before any deductions. What lands in your bank account is your <strong>net pay</strong>, sometimes called "take-home pay." The gap between the two is filled by taxes and benefit deductions, all of which show up on your pay stub.</p>

<h3>Federal Income Tax Withholding</h3>
<p>Your employer withholds federal income tax from every paycheck based on two things: your income and the W-4 form you filled out on your first day. The W-4 tells your employer how much to withhold. If you claimed fewer allowances (or filed as single with no adjustments), more is withheld — which usually means a refund at tax time. Claim more allowances and you take home more each paycheck but may owe in April.</p>
<p>Federal tax rates for 2025 are marginal, meaning only the income in each bracket is taxed at that rate. A single filer earning $60,000 pays 10% on the first $11,925, 12% on income from $11,926–$48,475, and 22% on income above that. Your <em>effective</em> rate ends up well below 22%.</p>

<h3>FICA: Social Security and Medicare</h3>
<p>FICA stands for the Federal Insurance Contributions Act. It funds Social Security and Medicare, and it's split equally between you and your employer:</p>
<ul>
  <li><strong>Social Security:</strong> 6.2% on wages up to $176,100 (2025)</li>
  <li><strong>Medicare:</strong> 1.45% on all wages (plus an extra 0.9% over $200,000)</li>
</ul>
<p>That's 7.65% off the top of every paycheck, no exceptions. Unlike income tax, FICA doesn't care about your W-4 elections.</p>

<h3>State Income Tax</h3>
<p>Nine states have no income tax (Alaska, Florida, Nevada, New Hampshire, South Dakota, Tennessee, Texas, Washington, Wyoming). Everyone else pays state income tax on top of federal. Rates vary widely — from a flat 3% in some states to over 13% at the top bracket in California. Check your pay stub line by line; it should itemize every deduction.</p>

<h3>Pre-Tax Deductions Lower Your Taxable Income</h3>
<p>Here's the good news: certain benefits reduce your taxable income before withholding is calculated.</p>
<ul>
  <li><strong>401(k) contributions</strong> — traditional contributions come out pre-tax, so a $500/month 401(k) contribution reduces your taxable income by $6,000/year.</li>
  <li><strong>Health insurance premiums</strong> — employer-sponsored plans are typically paid pre-tax.</li>
  <li><strong>HSA or FSA contributions</strong> — pre-tax dollars set aside for medical expenses.</li>
  <li><strong>Commuter benefits</strong> — up to $325/month (2025) for transit or parking.</li>
</ul>
<p>This means a bigger 401(k) contribution actually costs you less than it looks — the government effectively subsidizes part of it through reduced withholding.</p>

<h3>A Real Example</h3>
<p>Single filer in a state with 5% income tax, $60,000 salary, contributing 6% to a traditional 401(k), paying $150/month for health insurance:</p>
<ul>
  <li>Gross pay (biweekly): ~$2,308</li>
  <li>401(k) deduction: $138</li>
  <li>Health insurance: $150</li>
  <li>Federal income tax: ~$215</li>
  <li>FICA: ~$177</li>
  <li>State tax: ~$89</li>
  <li><strong>Net pay: ~$1,539 per paycheck (~$3,078/month)</strong></li>
</ul>
<p>Your W-2 at year-end will show all of this and reconcile your total withholding against what you actually owed. If too much was withheld, you get a refund. If too little, you pay the difference — which is why it's worth reviewing your W-4 annually.</p>
""",
        'references': [
            {
                'title': 'Tax Withholding Estimator',
                'url': 'https://www.irs.gov/individuals/tax-withholding-estimator',
                'source': 'IRS.gov',
            },
            {
                'title': 'Topic No. 751: Social Security and Medicare Withholding Rates',
                'url': 'https://www.irs.gov/taxtopics/tc751',
                'source': 'IRS.gov',
            },
            {
                'title': '2025 Federal Income Tax Brackets',
                'url': 'https://www.irs.gov/newsroom/irs-provides-tax-inflation-adjustments-for-tax-year-2025',
                'source': 'IRS.gov',
            },
            {
                'title': 'Understanding Your Paycheck',
                'url': 'https://www.consumerfinance.gov/consumer-tools/money-as-you-grow/what-is-a-paycheck/',
                'source': 'Consumer Financial Protection Bureau',
            },
        ],
    },
    {
        'slug': 'emergency-fund',
        'category': 'Saving',
        'category_color': 'green',
        'title': 'Build Your Emergency Fund Before Anything Else',
        'summary': "Before investing, before extra loan payments, before lifestyle upgrades — you need 3–6 months of expenses in cash. Here's why, and the fastest way to get there on an entry-level salary.",
        'read_time': '5 min',
        'tags': ['saving', 'emergency fund', 'beginner'],
        'body': """
<p>Financial advice is full of competing priorities: pay off debt, invest early, save for a house. But there's one thing that should come first for almost everyone starting out: a cash buffer that can absorb an unexpected hit without sending you into debt. That's your emergency fund.</p>

<h3>Why an Emergency Fund Comes First</h3>
<p>Without one, a single bad event — a medical bill, a car repair, a sudden job loss — forces you to put expenses on a credit card at 20%+ APR or dip into retirement accounts and pay penalties. An emergency fund breaks that cycle. It's not an investment; it's insurance.</p>
<p>It also gives you leverage. When you have 3 months of expenses saved, you can leave a toxic job without panicking. You can negotiate a salary instead of taking the first offer out of desperation. Liquidity is freedom.</p>

<h3>How Much Do You Actually Need?</h3>
<p>The standard advice is <strong>3–6 months of essential expenses</strong>. Essential means: rent, utilities, groceries, minimum debt payments, and transportation to work. Not your full lifestyle — just the basics to keep the lights on if income disappeared tomorrow.</p>
<p>On an entry-level salary, calculate your monthly essentials honestly. If your baseline is $2,500/month, you're aiming for $7,500–$15,000. That can feel overwhelming, which is why the first milestone is a $1,000 starter fund — enough to cover most minor emergencies without touching debt.</p>

<h3>Where to Keep It</h3>
<p>Your emergency fund should be in a <strong>high-yield savings account (HYSA)</strong> — not a checking account, not the stock market, not crypto. You need it accessible within 1–2 business days and earning meaningful interest while it sits there.</p>
<p>As of early 2025, many online banks are offering 4–5% APY on HYSAs compared to the national average of 0.46% at traditional banks. On a $10,000 emergency fund, that's roughly $450/year in interest vs. $46. The difference is meaningful.</p>
<p>Good options include SoFi, Marcus by Goldman Sachs, Ally, and Discover. These are FDIC-insured up to $250,000 and take 5 minutes to open. Do not keep your emergency fund in the same checking account you spend from — psychological separation matters.</p>

<h3>The Fastest Way to Build It</h3>
<p>Automation is the only system that reliably works for most people. Set up an automatic transfer on payday — even $100 or $150 every two weeks. You won't miss what never hits your checking account. After 6 months at $150 biweekly, you'll have $1,950. That's a real emergency fund taking shape.</p>
<p>To accelerate it, look for one-time windfalls to redirect: tax refunds, work bonuses, birthday money, selling things you no longer use. Any cash infusion goes straight to the fund until you hit your target.</p>

<h3>What Counts as an Emergency</h3>
<p>An emergency fund is for actual emergencies, not irregular but predictable expenses. Car registration, holiday gifts, and annual subscriptions are not emergencies — they're just things you should budget for separately. An emergency is unexpected, necessary, and urgent: medical bills, job loss, a broken appliance that's required for daily life, emergency travel.</p>
<p>Resist the temptation to use it for anything else. If you have to tap it, immediately start rebuilding. The peace of mind of a full emergency fund is worth more than the marginal return from investing those dollars.</p>

<h3>After You Hit Your Target</h3>
<p>Once you have 3–6 months covered, redirect the automatic transfer to your next priority — typically maxing an employer 401(k) match (free money) or paying down high-interest debt. Your emergency fund isn't growing your wealth; it's protecting it. Once it's funded, leave it alone and move on.</p>
""",
        'references': [
            {
                'title': 'An Essential Guide to Building an Emergency Fund',
                'url': 'https://www.consumerfinance.gov/about-us/blog/an-essential-guide-to-building-an-emergency-fund/',
                'source': 'Consumer Financial Protection Bureau',
            },
            {
                'title': 'Best High-Yield Savings Accounts',
                'url': 'https://www.bankrate.com/banking/savings/best-high-yield-interests-savings-accounts/',
                'source': 'Bankrate',
            },
            {
                'title': 'National Savings Rate Data',
                'url': 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/',
                'source': 'FDIC',
            },
            {
                'title': 'Building Savings for Emergencies',
                'url': 'https://www.consumerfinance.gov/consumer-tools/saving-for-emergencies/',
                'source': 'Consumer Financial Protection Bureau',
            },
        ],
    },
    {
        'slug': '401k-basics',
        'category': 'Investing',
        'category_color': 'purple',
        'title': "Your 401(k): Don't Leave Free Money on the Table",
        'summary': "If your employer matches contributions and you're not contributing, you're turning down free money. Learn how to set up your 401(k), what \"vesting\" means, and how much to contribute.",
        'read_time': '6 min',
        'tags': ['401k', 'investing', 'retirement'],
        'body': """
<p>A 401(k) is a retirement savings account sponsored by your employer. It lets you invest a portion of each paycheck before taxes hit — and in many cases, your employer will match what you put in. If you're not contributing enough to capture that full match, you're leaving part of your compensation on the table.</p>

<h3>How a 401(k) Match Works</h3>
<p>The most common matching structure is something like "50% match on contributions up to 6% of salary." On a $60,000 salary, that means: you contribute 6% ($3,600/year), your employer adds 50% of that ($1,800/year) for free. That's an immediate 50% return on your first $3,600 invested before a single index fund even gains a cent.</p>
<p>The minimum you should always contribute: <strong>enough to get the full employer match</strong>. If you contribute 4% when the match requires 6%, you're leaving $600/year behind. There is no financial product that can beat a 50–100% guaranteed return.</p>

<h3>Traditional 401(k) vs. Roth 401(k)</h3>
<p>Many employers now offer both options:</p>
<ul>
  <li><strong>Traditional 401(k):</strong> Contributions are pre-tax — your taxable income goes down now, but you pay ordinary income taxes on withdrawals in retirement.</li>
  <li><strong>Roth 401(k):</strong> Contributions are after-tax — no immediate tax break, but all growth and withdrawals in retirement are completely tax-free.</li>
</ul>
<p>Early in your career, when you're likely in the 12% or 22% tax bracket, the Roth 401(k) is often the better choice. You pay taxes now at a low rate, then never again — including on decades of compounding growth. If your income grows significantly over your career (it likely will), future-you will be in a higher bracket. Locking in today's low rate is usually the smart move.</p>

<h3>Contribution Limits</h3>
<p>For 2025, the IRS allows you to contribute up to <strong>$23,500</strong> to your 401(k) (employee contributions only). Employer contributions don't count toward this limit. Most people starting out won't hit this ceiling — but aim to increase your contribution rate by 1% every year, or whenever you get a raise.</p>

<h3>What Is Vesting?</h3>
<p>Your own contributions are always 100% yours immediately. But employer matching contributions may be subject to a <strong>vesting schedule</strong> — meaning you only keep the employer money if you stay at the company for a minimum period.</p>
<p>Common vesting types:</p>
<ul>
  <li><strong>Cliff vesting:</strong> You own 0% of employer contributions until a certain date (e.g., 3 years), then suddenly 100%.</li>
  <li><strong>Graded vesting:</strong> You earn ownership gradually — e.g., 20% per year for 5 years.</li>
  <li><strong>Immediate vesting:</strong> Employer contributions are yours right away.</li>
</ul>
<p>Before you leave a job, always check your vesting status. Leaving before you're fully vested means walking away from free money.</p>

<h3>What to Invest In</h3>
<p>Most 401(k) plans offer a menu of mutual funds. If you're overwhelmed by the options, look for a <strong>target-date fund</strong> (usually named something like "Target Retirement 2065 Fund"). These automatically hold a diversified mix of stocks and bonds and gradually shift to more conservative allocations as the target year approaches. They're not perfect, but they're a sensible default that requires zero ongoing decisions from you.</p>
<p>If you want more control, a basic two- or three-fund approach works well: a broad US stock market index fund plus an international index fund. Keep expense ratios under 0.20% — your plan's cheapest options are usually the best ones.</p>

<h3>One More Thing: Don't Touch It Early</h3>
<p>Withdrawing from a 401(k) before age 59½ triggers a 10% penalty on top of ordinary income tax. A $10,000 early withdrawal can cost you $3,000–$4,000 in taxes and penalties. More importantly, you lose the compounding on that money forever. The only legitimate early exit is a 401(k) loan (which you must repay with interest) or specific hardship provisions. Treat your 401(k) as completely untouchable until retirement.</p>
""",
        'references': [
            {
                'title': '401(k) and Profit-Sharing Plan Contribution Limits',
                'url': 'https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-401k-and-profit-sharing-plan-contribution-limits',
                'source': 'IRS.gov',
            },
            {
                'title': 'Types of Retirement Plans',
                'url': 'https://www.dol.gov/general/topic/retirement/typesofplans',
                'source': 'U.S. Department of Labor',
            },
            {
                'title': 'Choosing a Retirement Plan',
                'url': 'https://www.irs.gov/retirement-plans/choosing-a-retirement-plan',
                'source': 'IRS.gov',
            },
            {
                'title': '401(k) Vesting Rules',
                'url': 'https://www.dol.gov/sites/dolgov/files/ebsa/about-ebsa/our-activities/resource-center/publications/understanding-retirement-plan-fees-and-expenses.pdf',
                'source': 'U.S. Department of Labor',
            },
        ],
    },
    {
        'slug': 'credit-score-101',
        'category': 'Credit',
        'category_color': 'orange',
        'title': 'Credit Scores: What They Are and How to Build Yours Fast',
        'summary': 'Your credit score affects your apartment, car loan, and eventually your mortgage rate. Understand the 5 factors that make up your score and the exact habits that will push it past 750.',
        'read_time': '5 min',
        'tags': ['credit', 'credit score', 'beginner'],
        'body': """
<p>Your credit score is a three-digit number (300–850) that summarizes your history of borrowing and repaying money. Lenders, landlords, and sometimes even employers use it to assess how risky you are to work with. A high score means lower interest rates on everything from car loans to mortgages — saving you tens of thousands of dollars over your lifetime.</p>

<h3>The Five Factors of Your FICO Score</h3>
<p>The FICO score (used by ~90% of lenders) is calculated from five factors, each weighted differently:</p>
<ul>
  <li><strong>Payment history (35%)</strong> — The single biggest factor. Every on-time payment helps; every missed or late payment hurts significantly. Even one 30-day late payment can drop your score by 50–100 points.</li>
  <li><strong>Credit utilization (30%)</strong> — How much of your available credit you're using. If you have a $5,000 credit limit and carry a $2,000 balance, your utilization is 40%. Aim to stay below 30%, and ideally below 10%, for maximum score benefit.</li>
  <li><strong>Length of credit history (15%)</strong> — How long you've had credit accounts, including the age of your oldest account and the average age of all accounts. This is why you should keep your oldest credit card open even if you rarely use it.</li>
  <li><strong>Credit mix (10%)</strong> — Having a variety of credit types (credit cards, auto loan, student loan) shows you can manage different forms of debt. Not worth taking on debt just to improve this factor, but good to understand.</li>
  <li><strong>New credit (10%)</strong> — Each time you apply for credit, a "hard inquiry" appears on your report and temporarily dings your score by a few points. Don't apply for multiple new accounts within a short window.</li>
</ul>

<h3>How to Check Your Score for Free</h3>
<p>You're entitled to one free credit report per year from each of the three major bureaus (Equifax, Experian, TransUnion) at <strong>AnnualCreditReport.com</strong> — the only federally authorized site. During the COVID era this was expanded to weekly free reports, and that remains available as of 2025.</p>
<p>Many credit cards and banks also show your FICO or VantageScore for free in their app. Check yours at least quarterly so you catch errors early.</p>

<h3>What Score Ranges Mean</h3>
<ul>
  <li><strong>800–850: Exceptional</strong> — Best rates on everything</li>
  <li><strong>740–799: Very Good</strong> — Near-best rates, easy approvals</li>
  <li><strong>670–739: Good</strong> — Approved for most things, decent rates</li>
  <li><strong>580–669: Fair</strong> — Higher interest rates, some rejections</li>
  <li><strong>300–579: Poor</strong> — Difficulty getting approved; secured cards only</li>
</ul>

<h3>The Fastest Ways to Build Credit Early</h3>
<p><strong>1. Pay your full balance every month.</strong> Set up autopay for the statement balance. This prevents late payments (the #1 score killer) and avoids interest entirely. A credit card you pay in full is a completely free tool.</p>
<p><strong>2. Keep utilization low.</strong> If possible, pay your balance mid-cycle (before the statement closes) to lower the reported balance. Or request a credit limit increase — it lowers your utilization ratio without changing your spending.</p>
<p><strong>3. Don't close old accounts.</strong> Even a card you don't use contributes to your available credit and history length. Downgrade it to a no-fee version if necessary, but keep it open.</p>
<p><strong>4. Become an authorized user.</strong> If a parent or trusted family member with good credit adds you to their old account, their history helps your score immediately — even if you never use the card.</p>
<p><strong>5. Check for errors.</strong> One study found errors on 1 in 5 credit reports. Dispute anything incorrect at AnnualCreditReport.com — a removed negative item can boost your score significantly within 30 days.</p>

<h3>Common Myths</h3>
<p><strong>Myth: Checking your own score hurts it.</strong> False. Checking your own score is a "soft inquiry" and has zero impact. Only hard inquiries (when a lender pulls your credit) temporarily affect your score.</p>
<p><strong>Myth: You need to carry a balance to build credit.</strong> False and expensive. Paying in full every month while using the card builds credit just as effectively — without the interest charges.</p>
""",
        'references': [
            {
                'title': 'What is a credit score?',
                'url': 'https://www.consumerfinance.gov/ask-cfpb/what-is-a-credit-score-en-315/',
                'source': 'Consumer Financial Protection Bureau',
            },
            {
                'title': 'Free Annual Credit Reports',
                'url': 'https://www.annualcreditreport.com/',
                'source': 'AnnualCreditReport.com (authorized by federal law)',
            },
            {
                'title': "What's in Your FICO Score",
                'url': 'https://www.myfico.com/credit-education/whats-in-your-credit-score',
                'source': 'myFICO',
            },
            {
                'title': 'How to Improve Your Credit Scores',
                'url': 'https://www.consumerfinance.gov/ask-cfpb/how-do-i-get-and-keep-a-good-credit-score-en-318/',
                'source': 'Consumer Financial Protection Bureau',
            },
        ],
    },
    {
        'slug': '50-30-20-rule',
        'category': 'Budgeting',
        'category_color': 'green',
        'title': 'The 50/30/20 Rule: A Budget for People Who Hate Budgeting',
        'summary': "Split your take-home pay: 50% needs, 30% wants, 20% savings and debt. It's not perfect, but it's a solid starting framework when you're figuring things out for the first time.",
        'read_time': '3 min',
        'tags': ['budgeting', 'beginner'],
        'body': """
<p>Most people know they should budget but don't. Detailed category-by-category spreadsheets feel like a part-time job, and the specificity is often an excuse to procrastinate. The 50/30/20 rule is a framework that takes about five minutes to set up and actually gets used — which makes it better than a perfect system that sits in a spreadsheet unused.</p>

<h3>The Three Buckets</h3>
<p>The rule divides your <strong>after-tax income</strong> (what lands in your bank account, not your gross salary) into three buckets:</p>
<ul>
  <li><strong>50% — Needs:</strong> Non-negotiable expenses. Rent, utilities, groceries, minimum debt payments, insurance, transportation to work. If life would meaningfully fall apart without it, it's a need.</li>
  <li><strong>30% — Wants:</strong> Everything that improves your quality of life but isn't essential. Dining out, streaming subscriptions, gym membership, travel, shopping. These are the discretionary choices.</li>
  <li><strong>20% — Savings and debt repayment:</strong> Emergency fund, retirement contributions, extra debt payments above minimums, investing. This is how you build wealth.</li>
</ul>

<h3>Running the Numbers</h3>
<p>Take your monthly take-home pay and divide it. If you bring home $3,500/month:</p>
<ul>
  <li>$1,750 — needs</li>
  <li>$1,050 — wants</li>
  <li>$700 — savings and debt</li>
</ul>
<p>Now compare that to what you're actually spending. Most people find that "wants" has been silently eating their savings budget. The exercise of categorizing one month of bank transactions is usually eye-opening.</p>

<h3>The Limitations</h3>
<p>The 50/30/20 rule was popularized by Senator Elizabeth Warren in her book <em>All Your Worth</em> (2005) and is designed for median-income earners. Two major caveats:</p>
<p><strong>High cost-of-living cities</strong> — If you're in New York, San Francisco, or Seattle, rent alone might eat 40–50% of your take-home. In that case, the "needs" bucket is just bigger. Don't give up on the framework; adjust the ratios (60/20/20, for instance) and track whether you're making progress.</p>
<p><strong>High student loan debt</strong> — Large loan payments are technically a "need" if they're minimum payments, or a savings priority if you're paying extra. Be honest about which category each debt payment belongs in.</p>

<h3>Practical Setup</h3>
<p>You don't need special software. Open your bank's transaction history for the last 30 days, categorize each transaction as needs/wants/savings, and total each bucket. Compare to your take-home. Then set up two or three transfers on payday to automate the savings portion before you have a chance to spend it.</p>
<p>The goal isn't perfection — it's awareness. Most people who start tracking have a different relationship with money within 60 days. They're not spending less on everything; they're spending intentionally, which means cutting things that weren't actually making them happy and spending more on what does.</p>

<h3>When to Move Beyond 50/30/20</h3>
<p>The 50/30/20 rule is a great starting framework, but as your income and financial picture grow more complex, you may want to graduate to zero-based budgeting (every dollar has a job) or a more detailed category system. Tools like YNAB (You Need a Budget) are worth the monthly fee for people who find the rule too imprecise. But start simple and build the habit first.</p>
""",
        'references': [
            {
                'title': 'How to Create a Budget',
                'url': 'https://www.consumerfinance.gov/consumer-tools/budget/',
                'source': 'Consumer Financial Protection Bureau',
            },
            {
                'title': 'What is the 50/20/30 Rule?',
                'url': 'https://www.investopedia.com/ask/answers/022916/what-502030-budget-rule.asp',
                'source': 'Investopedia',
            },
            {
                'title': "Spending Tracker Worksheet",
                'url': 'https://www.consumerfinance.gov/consumer-tools/budget/worksheet/',
                'source': 'Consumer Financial Protection Bureau',
            },
        ],
    },
    {
        'slug': 'roth-vs-traditional',
        'category': 'Investing',
        'category_color': 'purple',
        'title': 'Roth IRA vs. Traditional IRA: Which One Is Right for You Right Now?',
        'summary': "Early in your career is almost always the best time to open a Roth IRA. Here's the tax math explained simply, the 2025 contribution limits, and how to open one in under 20 minutes.",
        'read_time': '7 min',
        'tags': ['roth ira', 'investing', 'retirement'],
        'body': """
<p>An IRA (Individual Retirement Account) is a tax-advantaged account you open yourself, separate from any employer plan. You can have both a 401(k) and an IRA — and for most people early in their careers, maxing out both makes sense. The key question is which type of IRA to choose.</p>

<h3>The Core Difference: When You Pay Taxes</h3>
<p>Both accounts let your investments grow without annual tax drag. The difference is when the IRS gets its cut:</p>
<ul>
  <li><strong>Traditional IRA:</strong> You contribute pre-tax dollars (or take a deduction if eligible). Your investments grow tax-deferred. You pay ordinary income taxes when you withdraw in retirement.</li>
  <li><strong>Roth IRA:</strong> You contribute after-tax dollars — no deduction now. But all growth is completely tax-free, and qualified withdrawals in retirement are entirely tax-free.</li>
</ul>
<p>The question is simple: do you expect to be in a higher or lower tax bracket in retirement than you are now?</p>

<h3>Why Roth Usually Wins Early in Your Career</h3>
<p>If you're 22–30 years old and starting out, you're likely in the 12% or 22% federal tax bracket. In retirement — with a lifetime of savings, Social Security income, and potentially required minimum distributions from traditional accounts — many people end up in the 22–32% bracket. Paying 12% now to lock in decades of tax-free growth is almost always the better trade.</p>
<p>There's also a psychological and practical benefit: Roth contributions (not earnings) can be withdrawn at any time without penalty. This makes a Roth IRA a decent backup emergency fund in a true crisis — though you should avoid touching it.</p>

<h3>2025 Contribution Limits</h3>
<ul>
  <li>Under 50: <strong>$7,000/year</strong> total across all IRAs</li>
  <li>50 or older: <strong>$8,000/year</strong> (catch-up contribution)</li>
  <li>You can split this between a Roth and Traditional IRA, but the combined total can't exceed the limit.</li>
</ul>

<h3>Income Limits for Roth IRA</h3>
<p>High earners can't contribute directly to a Roth IRA. In 2025:</p>
<ul>
  <li>Single filers: phase-out begins at $150,000 MAGI; no direct contributions above $165,000</li>
  <li>Married filing jointly: phase-out begins at $236,000; no direct contributions above $246,000</li>
</ul>
<p>If you're just starting out, you're almost certainly under the limit. But note this for later: if your income eventually exceeds the cap, a "backdoor Roth" conversion is still an option.</p>

<h3>Traditional IRA: When It Makes Sense</h3>
<p>A Traditional IRA is better if you're currently in a high tax bracket and expect to be in a lower one in retirement (e.g., you're a late-career high earner). It can also make sense if your Traditional IRA contribution is tax-deductible and your income isn't covered by an employer plan. The deduction phases out if you have a workplace retirement plan and your income exceeds certain thresholds.</p>

<h3>How to Open a Roth IRA in 20 Minutes</h3>
<p>The three most recommended brokerages for Roth IRAs are Fidelity, Vanguard, and Charles Schwab — all offer no-fee accounts, no minimums (Fidelity and Schwab), and excellent low-cost index funds.</p>
<ol>
  <li>Go to Fidelity.com, Vanguard.com, or Schwab.com and click "Open an Account"</li>
  <li>Select "Roth IRA" as the account type</li>
  <li>Provide your SSN, bank account info for funding, and beneficiary</li>
  <li>Fund the account and invest in a target-date index fund or a total market index fund (e.g., FSKAX at Fidelity, VTSAX at Vanguard)</li>
</ol>
<p>Set up a recurring monthly contribution. Even $100/month adds up to $1,200/year and builds the habit before you feel like you can afford more.</p>

<h3>One Important Rule: Earned Income Requirement</h3>
<p>You can only contribute to an IRA (either type) if you have earned income — wages, salary, freelance income, etc. You cannot contribute more than you earned that year. If you're a full-time student with a part-time job earning $4,000, your IRA contribution is capped at $4,000.</p>
""",
        'references': [
            {
                'title': 'Roth IRAs',
                'url': 'https://www.irs.gov/retirement-plans/roth-iras',
                'source': 'IRS.gov',
            },
            {
                'title': 'Traditional IRAs',
                'url': 'https://www.irs.gov/retirement-plans/traditional-iras',
                'source': 'IRS.gov',
            },
            {
                'title': 'IRA Contribution Limits',
                'url': 'https://www.irs.gov/retirement-plans/retirement-plans-faqs-regarding-iras-contributions',
                'source': 'IRS.gov',
            },
            {
                'title': 'IRA Deduction Limits',
                'url': 'https://www.irs.gov/retirement-plans/ira-deduction-limits',
                'source': 'IRS.gov',
            },
        ],
    },
    {
        'slug': 'good-debt-bad-debt',
        'category': 'Debt',
        'category_color': 'red',
        'title': 'Good Debt vs. Bad Debt: Not All Debt Is Created Equal',
        'summary': 'A mortgage can build wealth. Credit card debt at 24% APR destroys it. Learn which debts to pay off aggressively, which to pay slowly, and why putting extra money in a 401(k) sometimes beats paying off student loans.',
        'read_time': '5 min',
        'tags': ['debt', 'student loans', 'credit cards'],
        'body': """
<p>Most personal finance advice treats all debt as something to avoid. The reality is more nuanced. Some debt can increase your net worth over time; other debt is purely destructive. Understanding the difference helps you make smarter decisions about where to put extra dollars.</p>

<h3>What Makes Debt "Good" or "Bad"</h3>
<p>The distinction usually comes down to three factors:</p>
<ul>
  <li><strong>Interest rate:</strong> Low rates (below your expected investment return of ~7%) mean the math often favors investing instead of rushing to pay off the debt. High rates mean the opposite.</li>
  <li><strong>Purpose:</strong> Does the debt fund an asset that appreciates or generates income (a house, education, a business), or does it fund consumption that depreciates immediately (a vacation, a phone, a car lease)?</li>
  <li><strong>Terms:</strong> Fixed vs. variable rate, recourse vs. non-recourse, bankruptcy dischargeability — all affect risk.</li>
</ul>

<h3>Good Debt (Generally)</h3>
<p><strong>Mortgage:</strong> A 30-year fixed mortgage at 6.5% is borrowing at a known rate to purchase an asset that has historically appreciated. You also build equity with each payment and get a tax deduction on mortgage interest. Still, it only qualifies as "good" if you're not over-leveraged — borrowing more than you can comfortably repay is risky regardless of the asset.</p>
<p><strong>Student loans:</strong> Education debt is complicated. A $30,000 loan for a nursing or engineering degree is likely good debt — the credential generates earnings that far exceed the loan cost. The same loan for a low-return program with poor job placement is harder to justify. Evaluate based on expected salary increase, not just that it's "investing in yourself."</p>
<p><strong>Small business loan:</strong> Borrowing to start a business with a realistic path to profitability is the classic good-debt case. The debt funds an asset (the business) that can generate returns exceeding the interest rate.</p>

<h3>Bad Debt (Generally)</h3>
<p><strong>Credit card debt:</strong> The average credit card APR is around 24% as of 2025. If you're carrying a balance, you're losing 24 cents on every dollar of debt every year. There is no realistic investment that reliably returns 24% annually. This debt should be eliminated before anything else except a minimal emergency fund and 401(k) match.</p>
<p><strong>Payday loans:</strong> Annualized APRs often exceed 300–400%. These are designed to trap borrowers in cycles of renewal. Avoid entirely.</p>
<p><strong>Auto loans for depreciating vehicles:</strong> A modest loan for a used, reliable car is often unavoidable. But financing an expensive new car at 8% APR while it loses 20% of its value the moment you drive off the lot is a double hit. Keep car payments well under 15% of take-home pay.</p>

<h3>The Priority Order for Extra Dollars</h3>
<p>When you have extra cash after covering essentials, the math-optimal order is usually:</p>
<ol>
  <li><strong>Capture full 401(k) match</strong> — guaranteed 50–100% return, beats everything else</li>
  <li><strong>Eliminate high-interest debt (above ~7%)</strong> — credit cards, high-rate personal loans</li>
  <li><strong>Build emergency fund to 3–6 months</strong></li>
  <li><strong>Max Roth IRA ($7,000/year)</strong></li>
  <li><strong>Max 401(k) ($23,500/year)</strong></li>
  <li><strong>Moderate-interest debt (4–7%)</strong> — at this range it's roughly a wash vs. investing; personal preference matters</li>
  <li><strong>Low-interest debt (under 4%)</strong> — pay minimums and invest the rest</li>
</ol>

<h3>The Student Loan Dilemma</h3>
<p>Federal student loans issued after 2020 have rates in the 5–8% range. Whether to pay extra on these or invest is legitimately a close call. At 5%, the expected stock market return of 7–8% (long-term average) is slightly higher — suggesting investing may come out ahead over decades. At 7–8%, it's essentially a coin flip, and paying off the debt offers a guaranteed, risk-free "return."</p>
<p>The psychological component matters too. The stress of carrying debt has real value to eliminate. Do what you can sustain.</p>
""",
        'references': [
            {
                'title': 'Understanding Debt',
                'url': 'https://www.consumerfinance.gov/consumer-tools/debt-repayment/',
                'source': 'Consumer Financial Protection Bureau',
            },
            {
                'title': 'Average Credit Card Interest Rates',
                'url': 'https://www.federalreserve.gov/releases/g19/current/',
                'source': 'Federal Reserve',
            },
            {
                'title': 'Student Loan Interest Rates',
                'url': 'https://studentaid.gov/understand-aid/types/loans/interest-rates',
                'source': 'Federal Student Aid',
            },
            {
                'title': 'Debt Avalanche vs. Debt Snowball',
                'url': 'https://www.investopedia.com/articles/personal-finance/080716/debt-avalanche-vs-debt-snowball-which-best.asp',
                'source': 'Investopedia',
            },
        ],
    },
    {
        'slug': 'student-loans',
        'category': 'Debt',
        'category_color': 'red',
        'title': 'Student Loan Repayment Plans Explained (IDR, PSLF, and More)',
        'summary': 'Standard, graduated, income-driven — the repayment plan you choose will determine how much you pay in total. Plus: who qualifies for Public Service Loan Forgiveness and how to find out if your employer counts.',
        'read_time': '8 min',
        'tags': ['student loans', 'debt', 'repayment'],
        'body': """
<p>More than 43 million Americans carry federal student loan debt. The repayment plan you choose — most people just end up on the default — can mean paying tens of thousands of dollars more or less over the life of the loan. Understanding your options is worth the hour it takes to research them.</p>

<h3>Federal vs. Private Loans: A Critical Distinction</h3>
<p>Federal loans (Direct Subsidized, Direct Unsubsidized, PLUS) are managed through the government and come with income-driven repayment options, public service forgiveness, deferment, and forbearance protections. Private loans (from banks or credit unions) generally have none of these. Everything in this article applies to federal loans only.</p>

<h3>The Standard 10-Year Plan</h3>
<p>If you do nothing, you're placed on the Standard Repayment Plan: fixed monthly payments over 10 years. For most borrowers, this results in the lowest total interest paid. If you can afford it without financial strain, it's often the simplest path.</p>
<p>Example: $30,000 in loans at 6.5% → Standard plan payment: ~$340/month → Total paid: ~$40,800</p>

<h3>Income-Driven Repayment (IDR) Plans</h3>
<p>IDR plans cap your monthly payment at a percentage of your discretionary income and forgive any remaining balance after 20–25 years (though forgiven amounts may be taxable as income). The main options:</p>
<ul>
  <li><strong>SAVE (Saving on a Valuable Education):</strong> The newest plan, which replaced REPAYE. Payments are 5% of discretionary income for undergraduate loans (10% for graduate). Interest doesn't capitalize while on the plan. If your payment doesn't cover accruing interest, the government covers the difference — your balance won't grow. Forgiveness after 10 years for borrowers with balances under $12,000. Note: some SAVE provisions are under legal challenge as of 2025; check studentaid.gov for current status.</li>
  <li><strong>IBR (Income-Based Repayment):</strong> Payments are 10–15% of discretionary income. Forgiveness after 20–25 years.</li>
  <li><strong>PAYE (Pay As You Earn):</strong> Payments are 10% of discretionary income, capped at the Standard Plan amount. Forgiveness after 20 years. Only for new borrowers as of October 2007.</li>
</ul>
<p>IDR plans make sense if your loan balance is high relative to your income. They do not make sense if you have a low balance and a good salary — you'll pay far more in total interest dragging out repayment over 20 years.</p>

<h3>Public Service Loan Forgiveness (PSLF)</h3>
<p>PSLF is a federal program that forgives the remaining balance on Direct Loans after <strong>120 qualifying payments</strong> (10 years) while working full-time for a qualifying employer. The forgiven amount is not taxable as income.</p>
<p><strong>Qualifying employers include:</strong></p>
<ul>
  <li>Federal, state, local, and tribal government agencies</li>
  <li>501(c)(3) non-profit organizations</li>
  <li>Other non-profits that provide qualifying public services (public safety, public health, public education, etc.)</li>
</ul>
<p><strong>Qualifying employment does NOT include:</strong> For-profit companies, most partisan political organizations, most labor unions.</p>
<p>To qualify, you must be on an IDR plan or the Standard 10-Year Plan (though the Standard Plan will usually pay off the loan before 120 payments, so IDR is the effective choice). You must submit an Employment Certification Form annually (now called the PSLF Form) to track progress.</p>

<h3>Is PSLF Worth It?</h3>
<p>Run the numbers for your situation. If you have $80,000 in graduate school debt and will work in public health at $55,000/year, PSLF likely saves you $40,000–$60,000. For a $25,000 balance with a $75,000 salary in private industry, the standard plan will probably pay it off before 10 years anyway.</p>
<p>Use the Loan Simulator at studentaid.gov to compare plans side-by-side with your actual numbers.</p>

<h3>Refinancing: Be Careful</h3>
<p>Refinancing replaces your federal loans with a private loan — potentially at a lower interest rate. The catch: you permanently lose access to all federal protections (IDR, PSLF, deferment, forbearance). Refinancing makes sense only if you have no plans to pursue PSLF, your income is stable, and you qualify for a meaningfully lower rate.</p>

<h3>The Grace Period</h3>
<p>Federal loans have a 6-month grace period after graduation before repayment begins. Interest on unsubsidized loans continues to accrue during this period (though it doesn't capitalize until repayment starts). Subsidized loans don't accrue interest during grace periods. Use this window to select your repayment plan and get organized — not to ignore the loans.</p>
""",
        'references': [
            {
                'title': 'Repayment Plans',
                'url': 'https://studentaid.gov/manage-loans/repayment/plans',
                'source': 'Federal Student Aid',
            },
            {
                'title': 'Public Service Loan Forgiveness',
                'url': 'https://studentaid.gov/manage-loans/forgiveness-cancellation/public-service',
                'source': 'Federal Student Aid',
            },
            {
                'title': 'SAVE Plan Information',
                'url': 'https://studentaid.gov/announcements-events/save-plan',
                'source': 'Federal Student Aid',
            },
            {
                'title': 'Loan Simulator',
                'url': 'https://studentaid.gov/loan-simulator/',
                'source': 'Federal Student Aid',
            },
            {
                'title': 'Income-Driven Repayment Plans',
                'url': 'https://studentaid.gov/manage-loans/repayment/plans/income-driven',
                'source': 'Federal Student Aid',
            },
        ],
    },
    {
        'slug': 'health-insurance',
        'category': 'Benefits',
        'category_color': 'teal',
        'title': 'Health Insurance at Work: HMO, PPO, HSA — What to Pick',
        'summary': "Open enrollment is not the time to just click the default option. Learn the difference between plan types, why a high-deductible plan + HSA is often the best move for healthy 20-somethings, and what all those acronyms mean.",
        'read_time': '6 min',
        'tags': ['health insurance', 'benefits', 'hsa'],
        'body': """
<p>Open enrollment at a new job typically gives you 30 days to choose your health insurance plan. Most people click the default or pick whichever plan their coworker mentioned. It's worth taking 30 minutes to actually read your options — the difference between plans can be thousands of dollars per year.</p>

<h3>Key Terms You Need to Know</h3>
<ul>
  <li><strong>Premium:</strong> What you pay every month for coverage, regardless of whether you use it. Deducted pre-tax from your paycheck.</li>
  <li><strong>Deductible:</strong> The amount you pay out-of-pocket before insurance starts covering most costs. A $2,000 deductible means you pay the first $2,000 of medical bills each year.</li>
  <li><strong>Copay:</strong> A fixed amount you pay per visit (e.g., $20 for a primary care visit) after meeting certain conditions.</li>
  <li><strong>Coinsurance:</strong> After the deductible, you and the insurer split costs by percentage (e.g., 20% you, 80% insurer) until the out-of-pocket maximum is reached.</li>
  <li><strong>Out-of-pocket maximum:</strong> The most you'll pay in a year. After you hit this, insurance covers 100% for the rest of the year. This is your catastrophic protection.</li>
  <li><strong>In-network vs. out-of-network:</strong> Using a doctor in your plan's network costs far less. Always check before a visit.</li>
</ul>

<h3>HMO (Health Maintenance Organization)</h3>
<p>With an HMO, you choose a primary care physician (PCP) who coordinates all your care. You need referrals to see specialists. Out-of-network care is not covered except in emergencies. HMOs typically have lower premiums and simple, predictable costs, but less flexibility. Good for people who have established doctors in the network and prefer simplicity.</p>

<h3>PPO (Preferred Provider Organization)</h3>
<p>PPOs give you more flexibility — you can see any doctor without a referral, and out-of-network care is covered (at higher cost). Premiums are higher than HMOs. Good for people who travel frequently, have complex health needs, or want maximum flexibility in provider choice.</p>

<h3>HDHP (High-Deductible Health Plan)</h3>
<p>HDHPs have lower monthly premiums but higher deductibles (minimum $1,650 for self-only coverage in 2025). The key benefit: HDHPs qualify you for a Health Savings Account (HSA), which is one of the most powerful financial tools available.</p>

<h3>The HSA Triple Tax Advantage</h3>
<p>An HSA (Health Savings Account) is a savings account for medical expenses with three tax benefits stacked on top of each other:</p>
<ol>
  <li><strong>Contributions are pre-tax</strong> — reduces your taxable income</li>
  <li><strong>Growth is tax-free</strong> — invest the balance in index funds and it grows without taxes</li>
  <li><strong>Withdrawals for medical expenses are tax-free</strong> — permanently</li>
</ol>
<p>After age 65, you can withdraw for any purpose (like a Traditional IRA). This makes a fully funded HSA essentially a second retirement account. 2025 HSA contribution limits: $4,300 for self-only, $8,550 for family.</p>

<h3>Why HDHP + HSA is Often the Best Choice for Healthy 20-Somethings</h3>
<p>If you're generally healthy and don't have planned major medical expenses, consider this strategy:</p>
<ol>
  <li>Enroll in the HDHP</li>
  <li>Contribute the premium savings vs. the PPO to your HSA</li>
  <li>Invest the HSA in a low-cost index fund</li>
  <li>Pay current medical expenses out-of-pocket (to preserve HSA balance for growth)</li>
  <li>Save receipts — you can reimburse yourself from the HSA years later</li>
</ol>
<p>Example: If the PPO costs $200/month in premiums and the HDHP costs $80/month, you save $1,440/year in premiums. Contribute that to your HSA, invest it, and it compounds tax-free for decades.</p>

<h3>FSA vs. HSA</h3>
<p>An FSA (Flexible Spending Account) is different from an HSA. FSAs are "use it or lose it" — you must spend the balance by year-end (with some grace periods allowed). They don't roll over like HSAs, aren't portable if you change jobs, and can't be invested. They're still tax-advantaged but far less powerful. FSAs are available with any plan type; HSAs are only available with HDHPs.</p>

<h3>What to Do if You Miss Open Enrollment</h3>
<p>Once you miss open enrollment, you generally can't change your plan until the next enrollment period — unless you have a qualifying life event (marriage, birth, loss of other coverage). Take it seriously and make a deliberate choice.</p>
""",
        'references': [
            {
                'title': 'Choosing a Health Insurance Plan',
                'url': 'https://www.healthcare.gov/choose-a-plan/plan-types/',
                'source': 'HealthCare.gov',
            },
            {
                'title': 'Health Savings Accounts (HSAs)',
                'url': 'https://www.irs.gov/publications/p969',
                'source': 'IRS.gov (Publication 969)',
            },
            {
                'title': 'What is a Health Savings Account?',
                'url': 'https://www.consumerfinance.gov/ask-cfpb/what-is-a-health-savings-account-hsa-en-1945/',
                'source': 'Consumer Financial Protection Bureau',
            },
            {
                'title': 'HSA Contribution Limits 2025',
                'url': 'https://www.irs.gov/newsroom/irs-announces-2025-health-savings-account-limits',
                'source': 'IRS.gov',
            },
        ],
    },
    {
        'slug': 'compound-interest',
        'category': 'Investing',
        'category_color': 'purple',
        'title': 'Compound Interest: Why Starting at 22 Beats Starting at 32',
        'summary': '$200/month from age 22 grows to more than $200/month from age 32 — by a lot. See the real numbers, understand why time is your biggest investing advantage, and why waiting "until you make more money" is the #1 investing mistake.',
        'read_time': '4 min',
        'tags': ['investing', 'compound interest', 'beginner'],
        'body': """
<p>Compound interest is interest earned on both your original principal and on all previously earned interest. In other words, your returns generate their own returns. Over short periods the effect is modest. Over decades, it becomes the most powerful force in personal finance.</p>

<h3>The Math, Made Simple</h3>
<p>Imagine you invest $10,000 at a 7% annual return (the approximate long-term average of the US stock market after inflation):</p>
<ul>
  <li>After 10 years: ~$19,672</li>
  <li>After 20 years: ~$38,697</li>
  <li>After 30 years: ~$76,123</li>
  <li>After 40 years: ~$149,745</li>
</ul>
<p>You contributed $10,000 once. After 40 years, the interest on interest alone has added $139,745. Notice that the growth accelerates — you gain more in the last 10 years than in the first 30 combined. This is the compounding curve in action.</p>

<h3>The Cost of Waiting: A Direct Comparison</h3>
<p>Let's compare two people investing $200/month at 7% annual return:</p>
<p><strong>Alex starts at 22</strong> and invests until 65 (43 years):</p>
<ul>
  <li>Total contributed: $103,200</li>
  <li>Final balance: ~$620,000</li>
</ul>
<p><strong>Jordan starts at 32</strong> and invests until 65 (33 years):</p>
<ul>
  <li>Total contributed: $79,200</li>
  <li>Final balance: ~$303,000</li>
</ul>
<p>Alex contributed only $24,000 more but ends up with over $300,000 more — because 10 years of early compounding is worth more than hundreds of thousands of additional contributions later. Time in the market isn't a minor advantage; it's the primary variable.</p>

<h3>The Rule of 72</h3>
<p>A useful mental shortcut: divide 72 by your annual return to estimate how many years it takes to double your money.</p>
<ul>
  <li>At 6%: 72 ÷ 6 = <strong>12 years to double</strong></li>
  <li>At 7%: 72 ÷ 7 = <strong>~10 years to double</strong></li>
  <li>At 10%: 72 ÷ 10 = <strong>7.2 years to double</strong></li>
</ul>
<p>A $50,000 investment at 7% becomes $100,000 in ~10 years, $200,000 in ~20 years, $400,000 in ~30 years, and $800,000 in ~40 years. Starting late halves or worse the number of doublings you get.</p>

<h3>Why Fees Compound Too</h3>
<p>Compounding works against you when it comes to fees. A 1% annual expense ratio on a mutual fund sounds small, but over 30 years it can consume 25–30% of your final portfolio value compared to a 0.03% index fund. On a $500,000 portfolio, the difference between a 1% fee and a 0.05% fee is roughly $180,000 over 30 years. This is why low-cost index funds are so consistently recommended — it's not just about annual returns, it's about what doesn't get compounded away in fees.</p>

<h3>"I'll Start When I Make More Money"</h3>
<p>The most common reason people delay investing is income — they're waiting until they feel comfortable. The problem is that lifestyle inflation tends to absorb every raise, and "comfortable" is a moving target. Starting with $50/month is dramatically better than starting with $500/month in 5 years. The early years are the most valuable, not the most comfortable.</p>
<p>Automate a small amount now. Increase it by 1% each year or with each raise. The habit matters more than the amount in the early years.</p>
""",
        'references': [
            {
                'title': 'Compound Interest Calculator',
                'url': 'https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator',
                'source': 'Investor.gov (U.S. SEC)',
            },
            {
                'title': 'The Power of Compound Interest',
                'url': 'https://www.sec.gov/investor/pubs/compound.htm',
                'source': 'U.S. Securities and Exchange Commission',
            },
            {
                'title': 'Start Saving Early',
                'url': 'https://www.dol.gov/sites/dolgov/files/ebsa/about-ebsa/our-activities/resource-center/publications/top-10-ways-to-prepare-for-retirement.pdf',
                'source': 'U.S. Department of Labor',
            },
        ],
    },
    {
        'slug': 'negotiating-salary',
        'category': 'Career',
        'category_color': 'blue',
        'title': 'How to Negotiate Your Salary (Without Feeling Awkward)',
        'summary': "Most companies expect you to negotiate, and the first offer is rarely the final one. A practical script for asking for more, what to do if they say no, and why even a $3k raise compounds into tens of thousands over your career.",
        'read_time': '5 min',
        'tags': ['career', 'salary', 'negotiation'],
        'body': """
<p>Most people accept the first offer they receive. This is statistically a mistake. Hiring managers almost universally expect negotiation and routinely leave room in offers for it. A 10-minute conversation can add thousands of dollars to your annual income — and every future raise is typically calculated as a percentage of your current salary, so the effect compounds over your entire career.</p>

<h3>Do Your Research First</h3>
<p>Don't negotiate from gut feeling — negotiate from data. Before any conversation, research the market rate for your role, level, location, and industry using multiple sources:</p>
<ul>
  <li><strong>Glassdoor Salaries</strong> — user-reported data by company and role</li>
  <li><strong>LinkedIn Salary</strong> — filters by location, experience, education</li>
  <li><strong>Levels.fyi</strong> — especially useful for tech roles; includes equity and bonus</li>
  <li><strong>Bureau of Labor Statistics Occupational Outlook</strong> — government data on median wages by occupation</li>
  <li><strong>Peers and recruiters</strong> — talking to people in similar roles is often the most accurate data source</li>
</ul>
<p>Build a range: know the 25th, 50th, and 75th percentile for your role. Aim for at or above the median unless you have no prior experience in the field.</p>

<h3>When to Negotiate</h3>
<p>The best moment to negotiate is <strong>after you have a written offer but before you've accepted it</strong>. Don't negotiate during the interview. Don't accept verbally and then try to renegotiate. Don't email a counter-offer — have the conversation by phone or in person. Urgency to accept immediately is almost always a pressure tactic; you are entitled to a few days to consider any offer.</p>

<h3>A Practical Script</h3>
<p>Keep it simple, positive, and grounded in data:</p>
<p><em>"Thank you so much — I'm genuinely excited about this role and the team. Based on my research and the experience I bring [brief 1-sentence reference to specific skills], I was expecting something closer to [target number]. Is there flexibility to get there?"</em></p>
<p>Then stop talking. Let them respond. You don't need to justify at length. The silence feels more awkward to you than to them — they've had this conversation hundreds of times.</p>

<h3>What If They Say No?</h3>
<p>A "no" to base salary doesn't end the negotiation. There are other levers:</p>
<ul>
  <li><strong>Signing bonus:</strong> Often easier to get than base salary increases because it's a one-time cost and doesn't affect ongoing payroll benchmarks.</li>
  <li><strong>Earlier performance review:</strong> Ask for a review at 6 months instead of 12, with a clear target for a raise.</li>
  <li><strong>Remote work or schedule flexibility</strong></li>
  <li><strong>Paid time off</strong></li>
  <li><strong>Professional development budget</strong></li>
  <li><strong>Equity or stock options</strong></li>
</ul>
<p>Even if none of these moves, you've learned the offer is firm. Accepting it doesn't put you at a disadvantage — you now have a market data point for your next negotiation in 12–18 months.</p>

<h3>The Lifetime Math</h3>
<p>Say you negotiate an extra $5,000 on your first job offer (not unusual). Assume 3% annual raises going forward. After 10 years, that $5,000 starting gap has grown to ~$6,720 in annual salary difference — because all raises have compounded on the higher base. Over 30 years of a career, a $5,000 starting salary difference can mean over $250,000 in cumulative additional earnings.</p>
<p>That is the return on a 10-minute conversation.</p>

<h3>Negotiation Is Professional, Not Adversarial</h3>
<p>Many people — particularly women and first-generation professionals — are socialized to feel that negotiating is rude or presumptuous. Employers do not feel this way. Hiring managers expect it. Asking for a higher salary does not cause offers to be rescinded. It signals confidence and self-awareness. You are not asking for a favor; you are participating in a normal professional process.</p>
""",
        'references': [
            {
                'title': 'Occupational Employment and Wage Statistics',
                'url': 'https://www.bls.gov/oes/',
                'source': 'Bureau of Labor Statistics',
            },
            {
                'title': 'Salary Research',
                'url': 'https://www.glassdoor.com/Salaries/index.htm',
                'source': 'Glassdoor',
            },
            {
                'title': 'Technology Compensation Data',
                'url': 'https://www.levels.fyi/',
                'source': 'Levels.fyi',
            },
            {
                'title': 'Negotiating a Job Offer',
                'url': 'https://www.dol.gov/agencies/wb/equalpay/negotiating',
                'source': 'U.S. Department of Labor, Women\'s Bureau',
            },
        ],
    },
    {
        'slug': 'index-funds',
        'category': 'Investing',
        'category_color': 'purple',
        'title': 'Index Funds: The Boring Strategy That Beats Most Professionals',
        'summary': "You don't need to pick stocks. A simple three-fund portfolio of low-cost index funds outperforms the majority of actively managed funds over any 20-year period. Here's exactly what to buy and where to put it.",
        'read_time': '6 min',
        'tags': ['investing', 'index funds', 'stocks'],
        'body': """
<p>Financial media is filled with stock picks, hot sectors, and fund managers claiming to know what the market will do next. The data, compiled over decades, tells a very different story. The overwhelming majority of professional stock-pickers underperform a simple index fund. Yet investing in index funds requires no financial expertise, no market predictions, and about 30 minutes to set up for life.</p>

<h3>What Is an Index Fund?</h3>
<p>An index fund is a mutual fund or ETF (exchange-traded fund) that tracks a market index — like the S&P 500, which holds the 500 largest US companies, or the total US stock market index. Instead of a manager deciding which stocks to buy and sell, the fund just holds everything in the index in proportion to its size.</p>
<p>The result: you own a tiny slice of hundreds or thousands of companies instantly. When the market goes up, you go up. When it goes down, you go down — but so does everyone else, including the professionals trying to beat it.</p>

<h3>Why Index Funds Beat Active Management</h3>
<p>According to the S&P SPIVA report (the most comprehensive long-term study of fund performance), <strong>over 15 years, approximately 90% of actively managed US stock funds underperform their benchmark index</strong>. This isn't a bad year or a fluke — it's consistent across decades and geographies.</p>
<p>Why? Two compounding reasons:</p>
<ol>
  <li><strong>Costs:</strong> Active funds charge 0.5–1.5% annually in expense ratios, plus trading costs. Index funds charge 0.01–0.20%. On a $100,000 portfolio, a 1% fee difference costs $1,000 per year — and that $1,000 doesn't compound in your favor.</li>
  <li><strong>Information efficiency:</strong> Markets are highly efficient. By the time an analyst identifies an undervalued stock, that information is already priced in by thousands of other participants. Consistently "beating" the market requires being right more than the aggregate of every other market participant — which virtually no one sustains over decades.</li>
</ol>

<h3>The Three-Fund Portfolio</h3>
<p>The "three-fund portfolio" is a popular approach championed by the Bogleheads (followers of Vanguard founder John Bogle) that covers everything you need:</p>
<ol>
  <li><strong>US Total Stock Market Index Fund</strong> — captures all US companies, large and small (e.g., FSKAX at Fidelity, VTSAX at Vanguard, SWTSX at Schwab)</li>
  <li><strong>International Stock Market Index Fund</strong> — diversifies across developed and emerging markets outside the US (e.g., FTIHX, VXUS, SWISX)</li>
  <li><strong>US Bond Market Index Fund</strong> — lower risk, lower return; increases in allocation as you approach retirement (e.g., FXNAX, VBTLX, SWAGX)</li>
</ol>
<p>A common allocation early in your career: 60–70% US stocks, 20–30% international stocks, 10% bonds. As you approach retirement, shift gradually toward more bonds.</p>

<h3>Where to Put Index Funds</h3>
<p>Account type matters as much as fund selection:</p>
<ul>
  <li><strong>401(k):</strong> First, contribute enough to get the full employer match. Pick the index fund with the lowest expense ratio in your plan's menu.</li>
  <li><strong>Roth IRA:</strong> Next priority (up to $7,000/year). Tax-free growth makes this the best account for high-growth assets like stock index funds.</li>
  <li><strong>Taxable brokerage account:</strong> After maxing tax-advantaged accounts. Use ETF versions of index funds for better tax efficiency.</li>
</ul>

<h3>Dollar-Cost Averaging</h3>
<p>Invest a fixed amount on a regular schedule (monthly, biweekly) regardless of market conditions. This approach, called dollar-cost averaging, means you automatically buy more shares when prices are low and fewer when prices are high. It also removes the psychological burden of trying to time the market — which, as noted, professionals can't reliably do either.</p>

<h3>What to Actually Do This Week</h3>
<ol>
  <li>Open a Roth IRA at Fidelity, Vanguard, or Schwab if you haven't</li>
  <li>Fund it with whatever you can, even $50</li>
  <li>Buy FSKAX (Fidelity) or VTSAX (Vanguard) — a total US market index fund</li>
  <li>Set up a monthly automatic contribution</li>
  <li>Leave it alone and let compound interest do its work</li>
</ol>
""",
        'references': [
            {
                'title': 'SPIVA U.S. Scorecard',
                'url': 'https://www.spglobal.com/spdji/en/research-insights/spiva/',
                'source': 'S&P Global (SPIVA)',
            },
            {
                'title': 'Three-Fund Portfolio',
                'url': 'https://www.bogleheads.org/wiki/Three-fund_portfolio',
                'source': 'Bogleheads Wiki',
            },
            {
                'title': 'What is Investing?',
                'url': 'https://www.investor.gov/introduction-investing/getting-started/what-investing',
                'source': 'Investor.gov (U.S. SEC)',
            },
            {
                'title': 'Mutual Funds and ETFs',
                'url': 'https://www.sec.gov/investor/pubs/sec-guide-to-mutual-funds.pdf',
                'source': 'U.S. Securities and Exchange Commission',
            },
        ],
    },
]

ARTICLES_BY_SLUG = {a['slug']: a for a in ARTICLES}
