# Generated by Django 4.2.18 on 2025-01-15 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_alter_keymilestone_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="keymilestone",
            name="date",
            field=models.DateField(verbose_name="Milestone Date"),
        ),
    ]
