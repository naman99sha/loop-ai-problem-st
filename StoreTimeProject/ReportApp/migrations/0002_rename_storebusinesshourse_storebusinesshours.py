# Generated by Django 4.2.3 on 2023-07-26 06:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ReportApp", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="StoreBusinessHourse",
            new_name="StoreBusinessHours",
        ),
    ]