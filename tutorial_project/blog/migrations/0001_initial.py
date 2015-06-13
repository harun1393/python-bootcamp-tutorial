# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=127)),
                ('last_name', models.CharField(max_length=127)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('bio', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=127)),
                ('description', models.TextField(null=True, blank=True)),
                ('owner', models.ForeignKey(to='blog.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('body', models.TextField()),
                ('commenter', models.ForeignKey(to='blog.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('posted_at', models.DateField(default=django.utils.timezone.now)),
                ('title', models.CharField(max_length=127, db_index=True)),
                ('content', models.TextField()),
                ('is_draft', models.BooleanField(default=True)),
                ('blog', models.ForeignKey(to='blog.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=127, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blog.Post'),
        ),
    ]
