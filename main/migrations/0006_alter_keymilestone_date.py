# Generated by Django 4.2.18 on 2025-01-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0005_alter_keymilestone_options_alter_keymilestone_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="keymilestone",
            name="date",
            field=models.DateTimeField(verbose_name="Milestone Date"),
        ),
    ]
