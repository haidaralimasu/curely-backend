# Generated by Django 5.0.7 on 2024-07-31 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_blogpost_created_at_alter_blogpost_updated_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 31, 16, 16, 11, 99358, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="updated_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 31, 16, 16, 11, 99358, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
