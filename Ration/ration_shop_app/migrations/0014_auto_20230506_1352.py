# Generated by Django 3.2.5 on 2023-05-06 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ration_shop_app', '0013_auto_20230506_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='cust',
        ),
        migrations.AddField(
            model_name='member',
            name='cust',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ration_shop_app.customer'),
        ),
    ]
