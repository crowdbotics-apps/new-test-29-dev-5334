# Generated by Django 2.2.12 on 2020-06-03 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0011_auto_20200603_1707"),
    ]

    operations = [
        migrations.CreateModel(
            name="R67",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("r1", models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Rt",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("r1", models.BigIntegerField()),
            ],
        ),
    ]
