# Generated by Django 4.1.13 on 2024-01-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vulnerabilities", "0053_alter_packagechangelog_software_version_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="packagechangelog",
            name="software_version",
            field=models.CharField(
                default="34.0.0rc2",
                help_text="Version of the software at the time of change",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="vulnerabilitychangelog",
            name="software_version",
            field=models.CharField(
                default="34.0.0rc2",
                help_text="Version of the software at the time of change",
                max_length=100,
            ),
        ),
    ]