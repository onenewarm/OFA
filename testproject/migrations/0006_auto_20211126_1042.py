# Generated by Django 3.2.8 on 2021-11-26 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testproject', '0005_auto_20211125_1120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='user_id',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='recommendsub',
            old_name='user_id',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='date',
            field=models.DateField(default='1126'),
        ),
    ]
