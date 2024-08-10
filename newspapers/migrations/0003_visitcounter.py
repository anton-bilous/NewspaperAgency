# Generated by Django 5.0.7 on 2024-08-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newspapers", "0002_alter_redactor_years_of_experience"),
    ]

    operations = [
        migrations.CreateModel(
            name="VisitCounter",
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
                ("total_count", models.IntegerField(default=0)),
                ("logged_in_count", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
