# Generated by Django 2.2.6 on 2020-01-09 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20200108_0158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodinterests',
            name='favCuisine',
        ),
        migrations.AddField(
            model_name='foodinterests',
            name='secFavCuisine',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='foodinterests',
            name='thirdFavCuisine',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='foodinterests',
            name='topFavCuisine',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]
