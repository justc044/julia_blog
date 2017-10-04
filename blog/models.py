# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Course(models.Model):
    student = models.ForeignKey('auth.User')
    source = models.CharField(max_length=500)
    school = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)
    # sections
    # notes
    # assignments
    # projects
    # resources

    def publish(self):
        self.save

    def __str__(self):
        return self.title

class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=400)
