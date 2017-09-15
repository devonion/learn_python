# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Article
from .models import Feed
from .models import Category

# Register your models here.
# admin.site.register(Article)
# admin.site.register(Feed)
# admin.site.register(Category)

# Define the admin class
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_category', 'writer', 'created', 'last_modified')
    list_filter = ['category']

@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ('writer', 'created', 'article')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
