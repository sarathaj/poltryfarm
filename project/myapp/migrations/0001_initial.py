# Generated by Django 4.0.6 on 2022-07-22 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bill_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.IntegerField()),
                ('medicine_id', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='bill_transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(max_length=100)),
                ('farmer_id', models.CharField(max_length=100)),
                ('card_no', models.IntegerField()),
                ('cvv', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('dt', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='chicken_batch_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('company_id', models.CharField(max_length=50)),
                ('total_count', models.IntegerField()),
                ('total_load', models.IntegerField()),
                ('dt', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('no_of_days', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='company_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
                ('email', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('dt', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='daily_batchlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_id', models.CharField(max_length=100)),
                ('avg_weight', models.IntegerField()),
                ('total_death', models.IntegerField()),
                ('dt', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='daily_feedinglog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_id', models.CharField(max_length=100)),
                ('feed_name', models.CharField(max_length=100)),
                ('feed_quantity', models.IntegerField()),
                ('time', models.IntegerField()),
                ('dt', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='doctor_consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_id', models.CharField(max_length=100)),
                ('batch_id', models.CharField(max_length=100)),
                ('query', models.CharField(max_length=100)),
                ('dt', models.CharField(max_length=50)),
                ('time', models.IntegerField()),
                ('prescription', models.CharField(max_length=100)),
                ('p_date', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='doctor_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='farmer_batch_sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_id', models.CharField(max_length=100)),
                ('company_id', models.CharField(max_length=100)),
                ('total_count', models.IntegerField()),
                ('total_weight', models.IntegerField()),
                ('price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('dt', models.CharField(max_length=100)),
                ('time', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='farmer_manager_query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_id', models.CharField(max_length=100)),
                ('manager_id', models.CharField(max_length=100)),
                ('query', models.CharField(max_length=100)),
                ('q_dt', models.CharField(max_length=100)),
                ('q_time', models.IntegerField()),
                ('reply', models.CharField(max_length=50)),
                ('r_dt', models.CharField(max_length=100)),
                ('r_time', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='general_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('desc', models.IntegerField()),
                ('dt', models.CharField(max_length=100)),
                ('time', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='manager_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='medicineshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('medicine_shop_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('pin', models.IntegerField()),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='shop_farmer_sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_no', models.IntegerField()),
                ('bill_date', models.CharField(max_length=100)),
                ('total_amount', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='shop_medicine_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=100)),
                ('medicine_company', models.CharField(max_length=100)),
                ('batch_code', models.CharField(max_length=100)),
                ('medicine_description', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='store_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('desc', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('dt', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('pin', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('passwd', models.CharField(max_length=25)),
                ('u_type', models.CharField(max_length=10)),
            ],
        ),
    ]