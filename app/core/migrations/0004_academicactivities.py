# Generated by Django 4.1.13 on 2024-05-20 10:52

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_programme_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicActivities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('related_information', models.CharField(max_length=255)),
                ('image', models.ImageField(null=True, upload_to=core.models.academic_activities_image_file_path)),
            ],
        ),
    ]