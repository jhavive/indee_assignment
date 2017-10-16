# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CategoryTaskMap',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('category', models.ForeignKey(to='todo.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='categorytaskmap',
            name='task',
            field=models.ForeignKey(to='todo.Task'),
        ),
        migrations.AddField(
            model_name='categorytaskmap',
            name='user',
            field=models.ForeignKey(to='todo.AppUser'),
        ),
    ]
