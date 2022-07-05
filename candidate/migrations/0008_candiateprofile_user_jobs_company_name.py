# Generated by Django 4.0.2 on 2022-03-15 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0007_candiateprofile_delete_candiate_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='candiateprofile',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candiate', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='jobs',
            name='Company_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='candidate.company_profile'),
        ),
    ]
