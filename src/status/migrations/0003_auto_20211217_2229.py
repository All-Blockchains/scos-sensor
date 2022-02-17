# Generated by Django 3.0.14 on 2021-12-17 22:29

import json

from django.db import migrations

from sensor.settings import SENSOR_DEFINITION_FILE


def load_location(apps, schema_editor):
    with open(SENSOR_DEFINITION_FILE) as f:
        sensor_def = json.load(f)
    if "location" in sensor_def:
        location = sensor_def["location"]
        Location = apps.get_model("status", "Location")
        height = location["z"] if "z" in location else None
        Location.objects.create(
            gps=False,
            description=location["description"],
            latitude=location["y"],
            longitude=location["x"],
            height=height,
        )


class Migration(migrations.Migration):

    dependencies = [
        ("status", "0002_location_height"),
    ]

    operations = [migrations.RunPython(load_location)]
