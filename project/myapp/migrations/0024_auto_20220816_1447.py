# Generated by Django 3.2.15 on 2022-08-16 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_auto_20220816_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer_batch_sales',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='farmer_batch_sales',
            name='time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='farmer_batch_sales',
            name='total_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='farmer_batch_sales',
            name='total_weight',
            field=models.FloatField(),
        ),
    ]
