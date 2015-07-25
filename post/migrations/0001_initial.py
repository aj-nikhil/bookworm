# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(verbose_name='name')),
                ('photo', models.ImageField(default=b'/media/default_user.jpg', upload_to=b'bookworm/originals/', blank=True)),
                ('genre_scores', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(verbose_name='title')),
                ('year', models.IntegerField(default=0, null=True, blank=True)),
                ('country', models.CharField(max_length=40, null=True, verbose_name='country', blank=True)),
                ('photo', models.ImageField(default=b'/media/default_user.jpg', upload_to=b'bookworm/originals/', blank=True)),
                ('download_link', models.URLField(blank=True)),
                ('download_count', models.IntegerField(default=0, null=True, blank=True)),
                ('genre_scores', models.TextField(null=True, blank=True)),
                ('author', models.ForeignKey(to='post.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='text')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(verbose_name='title')),
                ('text', models.TextField(verbose_name='text')),
                ('time_to_read', models.CharField(max_length=50, null=True, verbose_name='time_to_read', blank=True)),
                ('likes', models.IntegerField(default=0, null=True, blank=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(to='post.Book')),
                ('submiter', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='post.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='submiter',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
