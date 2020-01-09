# Generated by Django 2.2.6 on 2020-01-09 02:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_auto_20200109_0222'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='stars',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='eater',
            name='least_fav_cuisine',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eater',
            name='location',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eater',
            name='sec_fav_cuisine',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eater',
            name='third_fav_cuisine',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eater',
            name='top_fav_cuisine',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]