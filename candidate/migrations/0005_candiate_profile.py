# Generated by Django 4.0.2 on 2022-03-15 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0004_jobs_delete_candiate_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='candiate_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Candidate_photo', models.ImageField(upload_to='images')),
                ('Candidate_name', models.CharField(max_length=100)),
                ('Cv', models.FileField(upload_to='')),
                ('Skills', models.CharField(max_length=200)),
                ('Experience', models.CharField(max_length=200)),
            ],
        ),
    ]
