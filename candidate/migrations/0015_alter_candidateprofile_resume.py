# Generated by Django 4.0.2 on 2022-03-17 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0014_alter_jobs_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateprofile',
            name='resume',
            field=models.FileField(null=True, upload_to='resumes'),
        ),
    ]
