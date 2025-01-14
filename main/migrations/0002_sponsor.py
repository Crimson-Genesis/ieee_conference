# Generated by Django 5.1.4 on 2025-01-14 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sponsor",
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
                ("site", models.URLField(default="http://127.0.0.1:8000/")),
                (
                    "light_logo",
                    models.URLField(
                        default="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.OAIcrS0Wq9Qrp1920SdZZAHaHa%26pid%3DApi&f=1&ipt=a1055d68c933fe529fb1826cfa1a18f9872e262177a65e0c66f4333151a3b482&ipo=images"
                    ),
                ),
                (
                    "dark_logo",
                    models.URLField(
                        default="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.OAIcrS0Wq9Qrp1920SdZZAHaHa%26pid%3DApi&f=1&ipt=a1055d68c933fe529fb1826cfa1a18f9872e262177a65e0c66f4333151a3b482&ipo=images"
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
