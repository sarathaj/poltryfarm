# Generated by Django 3.2.15 on 2022-08-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_doctor_consultation_doctor_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='farmer_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_id', models.IntegerField()),
                ('medicine_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
