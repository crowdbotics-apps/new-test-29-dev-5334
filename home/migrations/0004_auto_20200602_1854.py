# Generated by Django 2.2.12 on 2020-06-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='r1',
            field=models.ManyToManyField(blank=True, related_name='customtext_r1', to='home.Test'),
        ),
        migrations.AddField(
            model_name='customtext',
            name='r2',
            field=models.ManyToManyField(blank=True, related_name='customtext_r2', to='home.HomePage'),
        ),
    ]