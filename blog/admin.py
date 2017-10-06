# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import Post, Course, Section, Certification, Event, Goal, Resource, Interests, Skills

admin.site.register(Post)
admin.site.register(Course)
admin.site.register(Section)
admin.site.register(Certification)
admin.site.register(Event)
admin.site.register(Goal)
admin.site.register(Resource)
admin.site.register(Interests)
admin.site.register(Skills)
