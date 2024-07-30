# Generated by Django 5.0.7 on 2024-07-30 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0007_alter_newsletter_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newsletter",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 30, 16, 49, 19, 16866, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="newsletter",
            name="updated_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 30, 16, 49, 19, 16866, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
