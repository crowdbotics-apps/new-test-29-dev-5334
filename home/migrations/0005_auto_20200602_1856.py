# Generated by Django 2.2.12 on 2020-06-02 18:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("home", "0004_auto_20200602_1854"),
    ]

    operations = [
        migrations.RemoveField(model_name="customtext", name="r1",),
        migrations.AddField(
            model_name="customtext",
            name="r3",
            field=models.ManyToManyField(
                blank=True, related_name="customtext_r3", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="customtext",
            name="r2",
            field=models.ManyToManyField(
                blank=True, related_name="customtext_r2", to="home.Test"
            ),
        ),
    ]
