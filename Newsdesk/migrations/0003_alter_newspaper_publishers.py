# Generated by Django 5.1.5 on 2025-01-20 00:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "Newsdesk",
            "0002_alter_newspaper_published_date_alter_newspaper_topic_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="newspaper",
            name="publishers",
            field=models.ManyToManyField(
                related_name="newspapers", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
