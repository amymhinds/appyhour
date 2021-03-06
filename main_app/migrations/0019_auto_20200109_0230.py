# Generated by Django 2.2.6 on 2020-01-09 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_auto_20200109_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eater',
            name='interestedIn',
            field=models.CharField(choices=[('1', 'Anything that eats'), ('2', 'Men'), ('3', 'Women'), ('4', 'Men and Women'), ('5', 'Non-Binary')], default='Anything that eats', max_length=18),
        ),
        migrations.AlterField(
            model_name='eater',
            name='sex',
            field=models.CharField(choices=[('P', 'Prefer not to say'), ('F', 'Female'), ('M', 'Male'), ('NB', 'Non-Binary')], default='Prefer not to say', max_length=17),
        ),
    ]
