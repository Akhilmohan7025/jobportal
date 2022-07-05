# Generated by Django 4.0.2 on 2022-03-15 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0009_remove_candiateprofile_cv_alter_jobs_company_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidateprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(null=True, upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('dob', models.DateField(null=True)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female'), ('Other', 'other')], max_length=200, null=True)),
                ('mobile', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('resume', models.FileField(null=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='candiateprofile',
        ),
    ]