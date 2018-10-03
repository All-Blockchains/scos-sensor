# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-08-20 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id',
                 models.AutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('task_id',
                 models.IntegerField(
                     help_text=b'The id of the task relative to the result')),
                ('started',
                 models.DateTimeField(help_text=b'The time the task started')),
                ('finished',
                 models.DateTimeField(
                     help_text=b'The time the task finished')),
                ('duration',
                 models.DurationField(help_text=b'Task duration in seconds')),
                ('result',
                 models.CharField(
                     choices=[(1, b'success'), (2, b'failure')],
                     help_text=b'"success" or "failure"',
                     max_length=7)),
                ('detail',
                 models.CharField(
                     blank=True,
                     help_text=b'Arbitrary detail string',
                     max_length=512)),
                ('schedule_entry',
                 models.ForeignKey(
                     help_text=b'The schedule entry relative to the result',
                     on_delete=django.db.models.deletion.CASCADE,
                     related_name='results',
                     to='schedule.ScheduleEntry')),
            ],
            options={
                'ordering': ('task_id', ),
            },
        ),
        migrations.AlterUniqueTogether(
            name='taskresult',
            unique_together=set([('schedule_entry', 'task_id')]),
        ),
    ]
