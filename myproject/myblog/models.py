# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def display_category(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ category.name for category in self.category.all() ])

    display_category.short_description = 't_category'

class Feed(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    writer = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.content