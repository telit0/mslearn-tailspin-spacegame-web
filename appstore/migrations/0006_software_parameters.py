# Generated by Django 3.1.2 on 2020-10-31 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0005_software_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='parameters',
            field=models.JSONField(blank=True, default='{}'),
        ),
    ]
