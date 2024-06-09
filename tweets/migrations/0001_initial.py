# Generated by Django 4.2.11 on 2024-05-23 07:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tweet",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=50)),
                ("content", models.CharField(max_length=200)),
            ],
        ),
    ]