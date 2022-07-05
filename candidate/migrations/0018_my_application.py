# Generated by Django 4.0.2 on 2022-03-29 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0017_jobs_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='my_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('address', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('cancel', 'cancel'), ('order_placed', 'order_placed'), ('delivered', 'delivered'), ('Intransit', 'Intransit'), ('Dispatched', 'Dispatched')], default='order_placed', max_length=120)),
                ('excepted_delivery_date', models.DateField(null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidate.jobs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]