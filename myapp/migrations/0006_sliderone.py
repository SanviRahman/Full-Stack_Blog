# Generated by Django 5.1.5 on 2025-02-10 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_delete_newsletter'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderOne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='sliderone/')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_title', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
