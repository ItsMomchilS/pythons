# Generated by Django 3.1.3 on 2021-07-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20210714_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
