# Generated by Django 4.0.2 on 2022-04-03 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0019_alter_my_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_application',
            name='status',
            field=models.CharField(choices=[('order_placed', 'order_placed'), ('Intransit', 'Intransit'), ('cancel', 'cancel'), ('delivered', 'delivered'), ('Dispatched', 'Dispatched')], default='order_placed', max_length=120),
        ),
    ]
