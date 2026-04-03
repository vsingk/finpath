
function isDecimal(value){
    return /^-?(?:\d+|\d*\.\d+)$/.test(value);
}
document.addEventListener('DOMContentLoaded', function(){
    const submitButton = document.getElementById('submitSavingsGoal');
    let chart = null;
    let chart2 = null;

    submitButton.addEventListener('click', function(e){
        e.preventDefault();
        const savingsGoal = document.getElementById('savingsGoal').value;
        const goalDate = document.getElementById('goalDate').value;
        const interestRate = document.getElementById('interestRate').value;
        // console.log('Savings Goal:', savingsGoal);
        // console.log('Goal Date:', goalDate);
        // console.log('Interest Rate:', interestRate);
        if (savingsGoal === ""){
            alert("Please enter an Savings Goal.");
            return;
        }
        if (goalDate === ""){
            alert("Please enter a target date.");
            return;
        }
        if (interestRate === ""){
            alert("Please enter an interest rate.");
            return;
        }
        console.log("passed initial tests")
        if (!isDecimal(savingsGoal)){
            alert("Please enter a valid number for Savings Goal.");3
            return;
        }
        if (!isDecimal(interestRate)){
            alert("Please enter only decimal for Interest Rate.")
            return;
        }
        submitButton.disabled = true;
        submitButton.textContent = 'Loading...';
        fetch(`/budgets/projected-budget/${savingsGoal}/${interestRate}/${goalDate}/`)
        .then(Response => Response.json())
        .then(data => {
            submitButton.disabled = false;
            submitButton.textContent = 'Submit';
            // console.log("data",data);
            
            
            
            const result = document.getElementById('result');
            const chartCard = document.querySelector('.chart-card');
            chartCard.style.display = 'block';
            result.textContent = `Result: $${data['projected amount per month']} a month to reach your goal!`;
            const savingsGoalChart = document.getElementById('savingsGoalChart');
            const ctx = savingsGoalChart.getContext('2d');
            //savingsGoalChart.destroy();
            if (chart){
                chart.destroy();
                chart = null;
            }
            chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: 'projected amount per month',
                    labels: data.labels,
                    datasets: [{

                        label: 'Projected Savings Over Time',
                        
                        data: data.data,
                        
                        borderColor: 'rgba(75, 192, 192, 1)',
                        backgroundColor: 'rgba(75,192,192,0.2)',
                        fill: true,
                        tension: 0.3
                    }]
                
                },
                options: {
                    plugins:{
                        legend: {
                            onClick:()=>{}
                        }
                    },
                    responsive: true,
                    scales: {
                        x: {
                            type: 'linear',

                            title: {

                                display: true,
                                text: 'Number of Months'
                            },
                            ticks: {
                                
                                stepSize: 6

                            }
                        },
                        y:{
                            title:{
                                display: true,
                                text: 'Projected Savings ($)'
                            }
                        }
                    }
                    
                }
                

            })
        })
        .catch(() => {
            submitButton.disabled = false;
            submitButton.textContent = 'Submit';
        });
        //alert('calculating months to achieve savings goal...');
        // Handle form submission logic here

    });

    


    const submitMonthlyButton = document.getElementById("submitDepositGoal");
    submitMonthlyButton.addEventListener('click', function(e){
        //alert("clicked")
        e.preventDefault();
        const monthlyDeposit = document.getElementById('savingsAmount').value;
        const goalAmount = document.getElementById('goalAmount').value;
        const interestRate = document.getElementById('interestRate2').value;
        // console.log('Mont', monthlyDeposit)
        // console.log('Goal Amount:', goalAmount);
        // console.log('Interest Rate:', interestRate);
        if (interestRate === ""){
            alert("Please enter an interest rate.");
            return;
        }
        if (monthlyDeposit === ""){
            alert("Please enter a monthly deposit amount.");
            return;
        }
        if (goalAmount === ""){
            alert("Please enter a goal amount.")
            return;
        }    
        if(isNaN(monthlyDeposit)){
            alert("Please enter a valid number for Monthly Deposit.");
            return;
        }
        if(isNaN(goalAmount)){
            alert("Please enter a valid number for Goal.");
            return;
        }
        if(isNaN(interestRate)){
            alert("Please enter a valid number for Interest Rate.");
            return;
        }
        console.log("passed initial tests")
        if (!isDecimal(monthlyDeposit)){
            alert("Please enter a valid number for Monthly Deposit.");3
            return;
        }
        if (!isDecimal(interestRate)){
            alert("Please enter only decimal for Interest Rate.")
            return;
        }
        submitMonthlyButton.disabled = true;
        submitMonthlyButton.textContent = 'Loading...';
        fetch(`/budgets/monthly-deposit-project/${monthlyDeposit}/${goalAmount}/${interestRate}/`)
        .then(Response => Response.json())
        .then(data => {
            submitMonthlyButton.disabled = false;
            submitMonthlyButton.textContent = 'Submit';
            //console.log("data",data);
            const result2 = document.getElementById('result2');
            console.log("months... ",data.months)
            const years = Math.floor(data.months / 12);
            const remainingMonths = Math.ceil(data.months % 12)
            if (years === 0){
                result2.textContent = `Result: ${data.months} months to reach your goal!`;
            }
            else if (years === 1){
                if (remainingMonths === 0){
                    result2.textContent = `Result: ${years} year to reach your goal!`;
                }
                else{
                     result2.textContent = `Result: ${years} year and ${remainingMonths} months to reach your goal!`;
                }
            }else{
                if (remainingMonths === 0){
                    result2.textContent = `Result: ${years} years to reach your goal!`;
                }else{
                    result2.textContent = `Result: ${years} years and ${remainingMonths} months to reach your goal!`;
                }
            }
            

            const chartCard = document.querySelector('#chart-card-monthly');
            chartCard.style.display = 'block';
            //result2.textContent = `Result: $${data['projected amount per month']} a month to reach your goal!`;
            const savingsGoalChart = document.getElementById('projectedChart');
            const ctx = savingsGoalChart.getContext('2d');
            //savingsGoalChart.destroy();
            if (chart2){
                chart2.destroy();
                chart2 = null;
            }
            chart2 = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: 'projected amount per month',
                    labels: data.labels,
                    datasets: [{

                        label: 'Projected Savings Over Time',
                        
                        data: data.data,
                        
                        borderColor: 'rgba(75, 192, 192, 1)',
                        backgroundColor: 'rgba(75,192,192,0.2)',
                        fill: true,
                        tension: 0.3
                    }]
                
                },
                options: {
                    plugins:{
                        legend: {
                            onClick:()=>{}
                        }
                    },
                    responsive: true,
                    scales: {
                        x: {
                            type: 'linear',

                            title: {

                                display: true,
                                text: 'Number of Months'
                            },
                            ticks: {
                                
                                stepSize: 6

                            }
                        },
                        y:{
                            title:{
                                display: true,
                                text: 'Projected Savings ($)'
                            }
                        }
                    }
                    
                }
                

            })
        })
        .catch(() => {
            submitMonthlyButton.disabled = false;
            submitMonthlyButton.textContent = 'Submit';
        });
        //alert('calculating months to achieve savings goal...');

    });

    const toggleSavings = document.querySelector('.toggleSavingsGoal');
    const toggleMonthly = document.querySelector('.toggleMonthly');
    const savingsGoal = document.querySelector('.SavingsGoal');
    const monthlyAmount = document.querySelector('.MonthlyAmount');
    const savingsCanvas = document.querySelector('#chart-card-savings');
    const monthlyCanvas = document.querySelector('#chart-card-monthly');
    const savingsCanvasActual = document.querySelector('#savingsGoalChart');
    const monthlyCanvasActual = document.querySelector('#projectedChart');
    
    toggleSavings.addEventListener('click', function(){
        if (savingsGoal.style.display === 'none'){
            savingsGoal.style.display = 'block';
            monthlyAmount.style.display = 'none';
            toggleSavings.style.backgroundColor = '#148a48';
            toggleSavings.style.color = 'white';
            toggleMonthly.style.backgroundColor = '#f7f9f7'
            toggleMonthly.style.color = '#148a48';
            
            savingsCanvas.style.display = 'block';
            monthlyCanvas.style.display = 'none';
            
                        
            
        }
    })
    toggleMonthly.addEventListener('click', function(){
        if (monthlyAmount.style.display === 'none'){
            monthlyAmount.style.display = 'block';
            savingsGoal.style.display = 'none';
            toggleMonthly.style.backgroundColor = '#148a48';
            toggleMonthly.style.color = 'white';
            toggleSavings.style.backgroundColor = '#f7f9f7';
            toggleSavings.style.color = '#148a48';
            
           
            savingsCanvas.style.display = 'none';
            monthlyCanvas.style.display = 'block';
            
            
        }
    })
});
