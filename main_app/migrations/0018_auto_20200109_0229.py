# Generated by Django 2.2.6 on 2020-01-09 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_auto_20200109_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eater',
            name='taste',
            field=models.CharField(choices=[('1', 'Sweet'), ('2', 'Savory'), ('3', 'Both')], default='Both', max_length=6),
        ),
    ]