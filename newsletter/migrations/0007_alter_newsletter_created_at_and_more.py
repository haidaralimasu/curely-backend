# Generated by Django 5.0.7 on 2024-07-29 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0006_alter_newsletter_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsletter",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 29, 14, 12, 9, 277895, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="newsletter",
            name="updated_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 29, 14, 12, 9, 277895, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
