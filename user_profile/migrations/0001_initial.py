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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, verbose_name='name', blank=True)),
                ('about', models.TextField(null=True, verbose_name='about', blank=True)),
                ('location', models.CharField(max_length=40, null=True, verbose_name='location', blank=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(default=b'/media/default_user.jpg', upload_to=b'bookworm/originals/', blank=True)),
                ('genre_scores', models.TextField(null=True, blank=True)),
                ('likes', models.TextField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
