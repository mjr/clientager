# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Subscription',
        ),
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name': 'inscrição', 'ordering': ['created_at'], 'verbose_name_plural': 'inscrições'},
        ),
    ]
