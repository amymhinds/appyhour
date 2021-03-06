# Generated by Django 2.2.6 on 2020-01-09 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_auto_20200109_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eater',
            name='interestedIn',
            field=models.CharField(choices=[('1', 'Anything that eats'), ('2', 'Men'), ('3', 'Women'), ('4', 'Men and Women'), ('5', 'Non-Binary')], default='1', max_length=18),
        ),
        migrations.AlterField(
            model_name='eater',
            name='sex',
            field=models.CharField(choices=[('P', 'Prefer not to say'), ('F', 'Female'), ('M', 'Male'), ('NB', 'Non-Binary')], default='P', max_length=17),
        ),
        migrations.AlterField(
            model_name='eater',
            name='taste',
            field=models.CharField(choices=[('1', 'Sweet'), ('2', 'Savory'), ('3', 'Both')], default='1', max_length=6),
        ),
    ]
