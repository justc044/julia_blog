# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171006_0629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='skills',
            name='category',
            field=models.CharField(default='TE', max_length=2, choices=[('TE', 'Technical'), ('SO', 'Soft')]),
        ),
    ]
