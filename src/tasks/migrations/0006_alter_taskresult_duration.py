# Generated by Django 3.2.25 on 2024-05-10 13:34

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0005_acquisition_data_encrypted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="taskresult",
            name="duration",
            field=models.DurationField(
                default=datetime.timedelta(0),
                help_text="Task duration, in %H:%M:%S.%f format",
            ),
        ),
    ]
