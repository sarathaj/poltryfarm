# Generated by Django 3.2.15 on 2022-08-16 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_alter_bill_transaction_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer_manager_query',
            name='q_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='farmer_manager_query',
            name='query',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='farmer_manager_query',
            name='r_time',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='farmer_manager_query',
            name='reply',
            field=models.CharField(max_length=500),
        ),
    ]
