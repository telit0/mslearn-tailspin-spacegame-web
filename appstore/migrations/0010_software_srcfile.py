# Generated by Django 3.1.2 on 2020-10-31 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0009_auto_20201031_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='srcFile',
            field=models.CharField(default='', max_length=255),
        ),
    ]
