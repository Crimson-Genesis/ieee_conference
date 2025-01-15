# Generated by Django 4.2.18 on 2025-01-15 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_rename_conferencetracks_conferencetrack_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="keymilestone",
            options={"ordering": ["date"]},
        ),
        migrations.AlterField(
            model_name="keymilestone",
            name="date",
            field=models.DateField(verbose_name="Milestone Date"),
        ),
        migrations.AlterField(
            model_name="keymilestone",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Milestone Name"),
        ),
    ]