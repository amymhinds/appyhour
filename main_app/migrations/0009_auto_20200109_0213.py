# Generated by Django 2.2.6 on 2020-01-09 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20200109_0212'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.AddField(
            model_name='eater',
            name='leastFavCuisine',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='eater',
            name='secFavCuisine',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='eater',
            name='taste',
            field=models.CharField(choices=[(
                '1', 'Sweet'), ('2', 'Savory'), ('3', 'Both')], default='Both', max_length=7),
        ),
        migrations.AddField(
            model_name='eater',
            name='thirdFavCuisine',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
        migrations.AddField(
            model_name='eater',
            name='topFavCuisine',
            field=models.CharField(blank=True, max_length=35, null=True),
        ),
    ]
