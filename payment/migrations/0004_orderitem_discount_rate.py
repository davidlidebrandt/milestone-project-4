# Generated by Django 3.1.7 on 2021-04-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_orderitem_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='discount_rate',
            field=models.FloatField(default=1.0),
        ),
    ]
