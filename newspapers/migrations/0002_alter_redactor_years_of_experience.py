# Generated by Django 5.0.7 on 2024-08-04 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newspapers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="redactor",
            name="years_of_experience",
            field=models.IntegerField(default=0),
        ),
    ]
