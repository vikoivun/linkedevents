# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-13 07:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0012_manytomany_audience'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeywordSet',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Name')),
                ('name_fi', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Name')),
                ('name_sv', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Name')),
                ('name_en', models.CharField(db_index=True, max_length=255, null=True, verbose_name='Name')),
                ('origin_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, verbose_name='Origin ID')),
                ('created_time', models.DateTimeField(blank=True, null=True)),
                ('last_modified_time', models.DateTimeField(blank=True, null=True)),
                ('usage', models.SmallIntegerField(choices=[(1, 'Any'), (2, 'Keyword'), (3, 'Audience')], default=1, verbose_name='Intended keyword usage')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_keywordset_created_by', to=settings.AUTH_USER_MODEL)),
                ('data_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.DataSource')),
                ('keywords', models.ManyToManyField(related_name='sets', to='events.Keyword')),
                ('last_modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_keywordset_modified_by', to=settings.AUTH_USER_MODEL)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.Organization', verbose_name='Organization which uses this set')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
