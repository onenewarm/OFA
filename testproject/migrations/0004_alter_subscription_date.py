# Generated by Django 3.2.8 on 2021-11-25 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testproject', '0003_auto_20211112_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='date',
            field=models.DateField(default='1125'),
        ),
    ]