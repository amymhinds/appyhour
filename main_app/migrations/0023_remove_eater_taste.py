# Generated by Django 2.2.6 on 2020-01-09 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0022_auto_20200109_0234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eater',
            name='taste',
        ),
    ]