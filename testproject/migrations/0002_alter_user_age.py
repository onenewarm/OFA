# Generated by Django 3.2.8 on 2021-11-08 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]