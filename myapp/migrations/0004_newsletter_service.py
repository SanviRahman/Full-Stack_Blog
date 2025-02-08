# Generated by Django 5.1.5 on 2025-02-08 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service', to='myapp.services'),
        ),
    ]
