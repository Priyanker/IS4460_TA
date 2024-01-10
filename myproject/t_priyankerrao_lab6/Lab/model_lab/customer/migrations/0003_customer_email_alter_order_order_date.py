# Generated by Django 4.2.7 on 2024-01-09 22:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.date(2024, 1, 9)),
        ),
    ]
