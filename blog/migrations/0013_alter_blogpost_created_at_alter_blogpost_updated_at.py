# Generated by Django 5.0.7 on 2024-08-01 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_alter_blogpost_created_at_alter_blogpost_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 8, 1, 12, 27, 29, 749911, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="updated_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 8, 1, 12, 27, 29, 749911, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
