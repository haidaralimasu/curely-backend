# Generated by Django 5.0.7 on 2024-07-31 16:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testimonials", "0003_alter_testimonial_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testimonial",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 31, 16, 17, 12, 624637, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="testimonial",
            name="updated_at",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 7, 31, 16, 17, 12, 624637, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
