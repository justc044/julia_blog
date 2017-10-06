# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_event_goals'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Goals',
            new_name='Goal',
        ),
    ]
