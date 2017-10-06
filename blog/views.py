# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.utils import timezone
from .models import Post, Course, Goal

def home(request):
    return render(request, 'blog/home.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'blog/course_list.html', {'courses': courses})

def goal_list(request):
    goals = Goal.objects.all()
    return render(request, 'blog/goals.html', {'goals': goals})
