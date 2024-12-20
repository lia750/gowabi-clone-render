# Generated by Django 5.0.3 on 2024-11-30 09:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Vendor",
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
                ("business_name", models.CharField(max_length=200)),
                ("business_description", models.TextField()),
                ("phone_number", models.CharField(max_length=15)),
                ("location", models.CharField(max_length=255)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("duration", models.IntegerField(help_text="Duration in minutes")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("spa", "Spa"),
                            ("face", "Face"),
                            ("eyelash", "Eyelash & Eyebrow"),
                            ("nails", "Nails"),
                            ("hair", "Hair"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="services",
                        to="vendor_app.vendor",
                    ),
                ),
            ],
        ),
    ]
