# Generated by Django 2.2.6 on 2020-01-09 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20200109_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eater',
            name='least_fav_cuisine',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='eater',
            name='location',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='eater',
            name='sec_fav_cuisine',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='eater',
            name='taste',
            field=models.CharField(choices=[('1', 'Sweet'), ('2', 'Savory'), ('3', 'Both')], default=('3', 'Both'), max_length=6),
        ),
        migrations.AlterField(
            model_name='eater',
            name='third_fav_cuisine',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='eater',
            name='top_fav_cuisine',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]
