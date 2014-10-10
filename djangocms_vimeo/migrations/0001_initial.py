# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='VimeoVideo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('movie_url', models.CharField(help_text='Vimeo video url. Example: https://vimeo.com/50516814', max_length=255, null=True, verbose_name='movie url', blank=True)),
                ('width', models.PositiveSmallIntegerField(verbose_name='width')),
                ('height', models.PositiveSmallIntegerField(verbose_name='height')),
                ('auto_play', models.BooleanField(default=False, verbose_name='auto play')),
                ('loop', models.BooleanField(default=False, verbose_name='loop')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
