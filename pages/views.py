from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .article_content import ARTICLES, ARTICLES_BY_SLUG


def home_view(request):
    return render(request, 'pages/home.html')


def learn_view(request):
    categories = ['All', 'Budgeting', 'Saving', 'Investing', 'Credit', 'Debt', 'Taxes', 'Benefits', 'Career']
    return render(request, 'pages/learn.html', {
        'articles': ARTICLES,
        'categories': categories,
    })


def article_view(request, slug):
    article = ARTICLES_BY_SLUG.get(slug)
    if article is None:
        raise Http404
    return render(request, 'pages/article_detail.html', {'article': article})
