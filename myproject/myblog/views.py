# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from .models import Article, Category, Feed
from collections import OrderedDict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
# Create your views here.

def index(request):
    '''
    view index page.
    '''
    categorys = Category.objects.all().order_by('name')
    
    context = OrderedDict()
    for item in Category.objects.all().order_by('name'):
        context[item.name] = Category.objects.get(id=item.id).article_set.all()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'myblog/index.html',
        {'categorys': categorys, 'context': context}
    )

def list(request, category_id):
    categorys = Category.objects.all().order_by('name')
    article_list = Category.objects.get(id=category_id).article_set.all()
    
    page = request.GET.get('page', 1)
    paginator = Paginator(article_list, 10)

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(
        request,
        'myblog/list.html',
        {'category_id': category_id, 'categorys': categorys, 'articles': articles}
    )

def detail(request, article_id):
    categorys = Category.objects.all().order_by('name')

    article = Article.objects.get(id=article_id)
    feeds = Feed.objects.all().filter(article_id=article_id)
    category = Category.objects.get(article=article_id)
    
    return render(
        request,
        'myblog/detail.html',
        {'category_id': category.id, 'categorys': categorys, 'article': article, 'feeds': feeds}
    )

def feed(request, article_id):
    writer = request.POST['writer']
    content = request.POST['content']

    feed = Feed(writer=writer, content=content, article_id=article_id)
    feed.save()

    redirectUrl = '/myblog/article/' + article_id
    print redirectUrl
    return redirect(redirectUrl)