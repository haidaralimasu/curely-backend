# Generated by Django 5.0.7 on 2024-07-28 13:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0003_alter_newsletter_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsletter",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 28, 13, 2, 1, 593094, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="newsletter",
            name="updated_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 28, 13, 2, 1, 593094, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
