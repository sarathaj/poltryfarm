# Generated by Django 3.2.15 on 2022-08-10 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20220809_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_details',
            name='company_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctor_details',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
