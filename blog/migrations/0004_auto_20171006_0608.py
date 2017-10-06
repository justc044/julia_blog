# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_certifications'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Certifications',
            new_name='Certification',
        ),
    ]
