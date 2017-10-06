# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_course_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400, null=True)),
                ('studystartdate', models.DateTimeField(null=True, blank=True)),
                ('estimatedacquiremonth', models.DateTimeField(null=True, blank=True)),
                ('acquired', models.BooleanField(default=False)),
            ],
        ),
    ]
