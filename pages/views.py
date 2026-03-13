from django.shortcuts import render


def home_view(request):
    return render(request, 'pages/home.html')


def learn_view(request):
    articles = [
        {
            'slug': 'first-paycheck',
            'category': 'Taxes',
            'category_color': 'blue',
            'title': 'Your First Paycheck: Why It Looks Smaller Than You Expected',
            'summary': 'You negotiated $60,000 — so why did only $3,800 hit your account? A quick breakdown of federal tax, FICA, state tax, and pre-tax deductions so nothing surprises you.',
            'read_time': '4 min',
            'icon': '💸',
            'tags': ['taxes', 'paycheck', 'beginner'],
        },
        {
            'slug': 'emergency-fund',
            'category': 'Saving',
            'category_color': 'green',
            'title': 'Build Your Emergency Fund Before Anything Else',
            'summary': 'Before investing, before extra loan payments, before lifestyle upgrades — you need 3–6 months of expenses in cash. Here\'s why, and the fastest way to get there on an entry-level salary.',
            'read_time': '5 min',
            'icon': '🛡️',
            'tags': ['saving', 'emergency fund', 'beginner'],
        },
        {
            'slug': '401k-basics',
            'category': 'Investing',
            'category_color': 'purple',
            'title': 'Your 401(k): Don\'t Leave Free Money on the Table',
            'summary': 'If your employer matches contributions and you\'re not contributing, you\'re turning down free money. Learn how to set up your 401(k), what "vesting" means, and how much to contribute.',
            'read_time': '6 min',
            'icon': '📈',
            'tags': ['401k', 'investing', 'retirement'],
        },
        {
            'slug': 'credit-score-101',
            'category': 'Credit',
            'category_color': 'orange',
            'title': 'Credit Scores: What They Are and How to Build Yours Fast',
            'summary': 'Your credit score affects your apartment, car loan, and eventually your mortgage rate. Understand the 5 factors that make up your score and the exact habits that will push it past 750.',
            'read_time': '5 min',
            'icon': '⭐',
            'tags': ['credit', 'credit score', 'beginner'],
        },
        {
            'slug': '50-30-20-rule',
            'category': 'Budgeting',
            'category_color': 'green',
            'title': 'The 50/30/20 Rule: A Budget for People Who Hate Budgeting',
            'summary': 'Split your take-home pay: 50% needs, 30% wants, 20% savings and debt. It\'s not perfect, but it\'s a solid starting framework when you\'re figuring things out for the first time.',
            'read_time': '3 min',
            'icon': '📊',
            'tags': ['budgeting', 'beginner'],
        },
        {
            'slug': 'roth-vs-traditional',
            'category': 'Investing',
            'category_color': 'purple',
            'title': 'Roth IRA vs. Traditional IRA: Which One Is Right for You Right Now?',
            'summary': 'Early in your career is almost always the best time to open a Roth IRA. Here\'s the tax math explained simply, the 2025 contribution limits, and how to open one in under 20 minutes.',
            'read_time': '7 min',
            'icon': '🏦',
            'tags': ['roth ira', 'investing', 'retirement'],
        },
        {
            'slug': 'good-debt-bad-debt',
            'category': 'Debt',
            'category_color': 'red',
            'title': 'Good Debt vs. Bad Debt: Not All Debt Is Created Equal',
            'summary': 'A mortgage can build wealth. Credit card debt at 24% APR destroys it. Learn which debts to pay off aggressively, which to pay slowly, and why putting extra money in a 401(k) sometimes beats paying off student loans.',
            'read_time': '5 min',
            'icon': '⚖️',
            'tags': ['debt', 'student loans', 'credit cards'],
        },
        {
            'slug': 'student-loans',
            'category': 'Debt',
            'category_color': 'red',
            'title': 'Student Loan Repayment Plans Explained (IDR, PSLF, and More)',
            'summary': 'Standard, graduated, income-driven — the repayment plan you choose will determine how much you pay in total. Plus: who qualifies for Public Service Loan Forgiveness and how to find out if your employer counts.',
            'read_time': '8 min',
            'icon': '🎓',
            'tags': ['student loans', 'debt', 'repayment'],
        },
        {
            'slug': 'health-insurance',
            'category': 'Benefits',
            'category_color': 'teal',
            'title': 'Health Insurance at Work: HMO, PPO, HSA — What to Pick',
            'summary': 'Open enrollment is not the time to just click the default option. Learn the difference between plan types, why a high-deductible plan + HSA is often the best move for healthy 20-somethings, and what all those acronyms mean.',
            'read_time': '6 min',
            'icon': '🏥',
            'tags': ['health insurance', 'benefits', 'hsa'],
        },
        {
            'slug': 'compound-interest',
            'category': 'Investing',
            'category_color': 'purple',
            'title': 'Compound Interest: Why Starting at 22 Beats Starting at 32',
            'summary': '$200/month from age 22 grows to more than $200/month from age 32 — by a lot. See the real numbers, understand why time is your biggest investing advantage, and why waiting "until you make more money" is the #1 investing mistake.',
            'read_time': '4 min',
            'icon': '🌱',
            'tags': ['investing', 'compound interest', 'beginner'],
        },
        {
            'slug': 'negotiating-salary',
            'category': 'Career',
            'category_color': 'blue',
            'title': 'How to Negotiate Your Salary (Without Feeling Awkward)',
            'summary': 'Most companies expect you to negotiate, and the first offer is rarely the final one. A practical script for asking for more, what to do if they say no, and why even a $3k raise compounds into tens of thousands over your career.',
            'read_time': '5 min',
            'icon': '🤝',
            'tags': ['career', 'salary', 'negotiation'],
        },
        {
            'slug': 'index-funds',
            'category': 'Investing',
            'category_color': 'purple',
            'title': 'Index Funds: The Boring Strategy That Beats Most Professionals',
            'summary': 'You don\'t need to pick stocks. A simple three-fund portfolio of low-cost index funds outperforms the majority of actively managed funds over any 20-year period. Here\'s exactly what to buy and where to put it.',
            'read_time': '6 min',
            'icon': '📉',
            'tags': ['investing', 'index funds', 'stocks'],
        },
    ]

    categories = ['All', 'Budgeting', 'Saving', 'Investing', 'Credit', 'Debt', 'Taxes', 'Benefits', 'Career']

    return render(request, 'pages/learn.html', {
        'articles': articles,
        'categories': categories,
    })
