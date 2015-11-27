# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='nome')),
                ('cpf', models.CharField(unique=True, max_length=11, verbose_name='CPF')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='telefone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('paid', models.BooleanField(default=False, verbose_name='Pago')),
            ],
            options={
                'verbose_name_plural': 'clientes',
                'ordering': ['created_at'],
                'verbose_name': 'cliente',
            },
        ),
    ]
