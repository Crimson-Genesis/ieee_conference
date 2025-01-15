# Generated by Django 4.2.18 on 2025-01-15 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_sponsor"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConferenceTracks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("track_name", models.CharField(max_length=100)),
                ("description", models.TextField(default="No Body.", max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name="KeyMilestones",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="KeynoteSpeakers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="")),
                ("topic", models.CharField(max_length=500)),
                ("description", models.TextField(default="No Body.", max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name="events",
            name="description",
            field=models.TextField(default="No Body.", max_length=1000),
        ),
        migrations.AddField(
            model_name="events",
            name="event_name",
            field=models.CharField(default="Zero", max_length=100),
        ),
        migrations.AlterField(
            model_name="sponsor",
            name="dark_logo",
            field=models.URLField(
                default="https://duckduckgo.com/i/742895b2644223c0.jpg"
            ),
        ),
        migrations.AlterField(
            model_name="sponsor",
            name="light_logo",
            field=models.URLField(
                default="https://duckduckgo.com/i/742895b2644223c0.jpg"
            ),
        ),
    ]