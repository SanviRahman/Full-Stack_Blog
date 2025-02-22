# Generated by Django 5.1.5 on 2025-02-10 04:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_sliderone_author'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderTwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='sliderTwo/')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_title', models.CharField(blank=True, max_length=200, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sliderTwo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
