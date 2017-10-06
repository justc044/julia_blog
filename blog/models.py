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

class Event(models.Model):
    year = models.DecimalField(max_digits=4, decimal_places=0)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Goal(models.Model):
    year = models.DecimalField(max_digits=4, decimal_places=0)
    description = models.TextField()

    def __str__(self):
        return self.description

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

    def __str__(self):
        return self.name

class Certification(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400, null=True)
    comment = models.CharField(max_length=400, null=True)
    studystartdate = models.DateTimeField(blank=True, null=True)
    estimatedacquiremonth = models.DateTimeField(blank=True, null=True)
    acquired = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Resource(models.Model):
    name = models.CharField(max_length=400)
    url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Projects(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField()
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    resources = models.ForeignKey(Resource, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Interests(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Skills(models.Model):
    TECHNICAL = 'TE'
    SOFT = 'SO'
    CATEGORY_CHOICES = (
        (TECHNICAL, 'Technical'),
        (SOFT, 'Soft')
    )
    description = models.CharField(max_length=400)
    startdate = models.DateTimeField(blank=True, null=True)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=TECHNICAL,
    )

    def __str__(self):
        return self.description
