# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 17:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0005_remove_note_is_important'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video_subject',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]