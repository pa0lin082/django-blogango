# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import markupfield.fields
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('tag_line', models.CharField(max_length=100)),
                ('entries_per_page', models.IntegerField(default=10)),
                ('recents', models.IntegerField(default=5)),
                ('recent_comments', models.IntegerField(default=5)),
            ],
        ),
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('text', markupfield.fields.MarkupField()),
                ('text_markup_type', models.CharField(default=b'plain', max_length=30, choices=[(b'html', b'html'), (b'plain', b'plain'), (b'markdown', b'markdown'), (b'restructuredtext', b'restructuredtext'), (b'textile', b'textile')])),
                ('summary', models.TextField()),
                ('_text_rendered', models.TextField(editable=False)),
                ('created_on', models.DateTimeField(default=datetime.datetime(9999, 12, 31, 23, 59, 59, 999999), editable=False)),
                ('is_page', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=True)),
                ('publish_date', models.DateTimeField(null=True)),
                ('comments_allowed', models.BooleanField(default=True)),
                ('is_rte', models.BooleanField(default=False)),
                ('meta_keywords', models.TextField(null=True, blank=True)),
                ('meta_description', models.TextField(null=True, blank=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-created_on'],
                'verbose_name_plural': 'Blog entries',
            },
        ),
        migrations.CreateModel(
            name='BlogRoll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(unique=True)),
                ('text', models.CharField(max_length=100)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user_url', models.URLField()),
                ('email_id', models.EmailField(max_length=254)),
                ('is_spam', models.BooleanField(default=False)),
                ('is_public', models.NullBooleanField()),
                ('user_ip', models.IPAddressField(null=True)),
                ('user_agent', models.CharField(default=b'', max_length=200)),
                ('comment_for', models.ForeignKey(to='blogango.BlogEntry')),
                ('created_by', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['created_on'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user_name', models.CharField(max_length=100)),
                ('user_url', models.URLField()),
                ('reaction_id', models.CharField(max_length=200, serialize=False, primary_key=True)),
                ('source', models.CharField(max_length=200)),
                ('profile_image', models.URLField(null=True, blank=True)),
                ('comment_for', models.ForeignKey(to='blogango.BlogEntry')),
            ],
            options={
                'ordering': ['created_on'],
                'abstract': False,
            },
        ),
    ]
