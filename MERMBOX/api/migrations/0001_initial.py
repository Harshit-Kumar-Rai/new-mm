# Generated by Django 4.1.7 on 2024-03-21 05:23

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Master",
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
                ("macid", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=180)),
                ("email", models.EmailField(max_length=254)),
                ("contact", models.CharField(max_length=13)),
                ("address", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=120)),
                ("pincode", models.CharField(max_length=6)),
                ("state", models.CharField(max_length=50)),
            ],
        ),
    ]