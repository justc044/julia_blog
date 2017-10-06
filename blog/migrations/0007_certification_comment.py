# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20171006_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='comment',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
