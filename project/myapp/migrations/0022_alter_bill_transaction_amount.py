# Generated by Django 3.2.15 on 2022-08-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_alter_shop_farmer_sales_total_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill_transaction',
            name='amount',
            field=models.FloatField(),
        ),
    ]