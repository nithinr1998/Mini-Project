# Generated by Django 4.2.6 on 2023-11-27 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ration_shop_app', '0016_customer_total_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
