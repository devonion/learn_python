from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^articles/category/(?P<category_id>[0-9]+)/$', views.list, name='list'),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^feed/(?P<article_id>[0-9]+)/$', views.feed, name='feed'),
]