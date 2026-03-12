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
        }
        if (goalDate === ""){
            alert("Please enter a target date.");
        }
        if (interestRate === ""){
            alert("Please enter an interest rate.");
        }
        
        fetch(`/budgets/projected-budget/${savingsGoal}/${interestRate}/${goalDate}/`)
        .then(Response => Response.json())
        .then(data => {
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
        }
        if (monthlyDeposit === ""){
            alert("Please enter a monthly deposit amount.");
        }
        if (goalAmount === ""){
            alert("Please enter a goal amount.")
        }    
        if(isNaN(monthlyDeposit)){
            alert("Please enter a valid number for Monthly Deposit.");
        }
        if(isNaN(goalAmount)){
            alert("Please enter a valid number for Goal.");
        }
        if(isNaN(interestRate)){
            alert("Please enter a valid number for Interest Rate.");
        }
        fetch(`/budgets/monthly-deposit-project/${monthlyDeposit}/${goalAmount}/${interestRate}/`)
        .then(Response => Response.json())
        .then(data => {
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
        })
        //alert('calculating months to achieve savings goal...');
        
   
    });

