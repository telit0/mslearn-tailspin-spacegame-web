# Generated by Django 3.1.2 on 2020-10-28 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0004_auto_20201028_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
