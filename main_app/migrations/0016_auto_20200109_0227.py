# Generated by Django 2.2.6 on 2020-01-09 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_auto_20200109_0225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eater',
            old_name='least',
            new_name='least_fav_cuisine',
        ),
        migrations.RenameField(
            model_name='eater',
            old_name='sec',
            new_name='sec_fav_cuisine',
        ),
        migrations.RenameField(
            model_name='eater',
            old_name='third',
            new_name='third_fav_cuisine',
        ),
        migrations.RenameField(
            model_name='eater',
            old_name='top',
            new_name='top_fav_cuisine',
        ),
        migrations.AlterField(
            model_name='eater',
            name='taste',
            field=models.CharField(choices=[('1', 'Sweet'), ('2', 'Savory'), ('3', 'Both')], default=('1', 'Sweet'), max_length=6),
        ),
    ]
