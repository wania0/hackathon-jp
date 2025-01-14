# Generated by Django 5.1.1 on 2024-11-09 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_employeer_email_remove_jobseeker_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('job_description', models.TextField(blank=True, max_length=500, null=True)),
                ('required_skills', models.TextField(blank=True, max_length=500, null=True)),
                ('salary_range', models.IntegerField(blank=True, null=True)),
                ('Employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employeer')),
            ],
        ),
    ]
