from django.db import models

# Create your models here.
class user_login(models.Model):
    #id
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.uname},{self.id}'

    #
    # def __str__(self):
    #     return self.fname


# Create your models here.
class user_details(models.Model):
    #id
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=50)
    pin = models.IntegerField()
    email = models.CharField(max_length=50)
    contact = models.IntegerField()
    #pwd = models.CharField(max_length=100)



class store_details(models.Model):
    #id = models.CharField(max_length=100)
    store_name = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    pin = models.IntegerField()
    desc = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.IntegerField()
    dt = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

class doctor_details(models.Model):
    #id = models.CharField(max_length=100)
    user_id = models.IntegerField()
    company_id = models.IntegerField()
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    pin = models.IntegerField()
    email = models.CharField(max_length=50)
    contact = models.IntegerField()

class farmer_details(models.Model):
    #id = models.CharField(max_length=100)
    user_id = models.IntegerField(default=0)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=50)
    pin = models.IntegerField()
    email = models.CharField(max_length=50)
    contact = models.IntegerField()


class company_details(models.Model):
     #id = models.CharField(max_length=100)
     user_id = models.IntegerField(default=0)
     name = models.CharField(max_length=100)
     desc = models.CharField(max_length=50)
     address = models.CharField(max_length=50)
     pin = models.CharField(max_length=50)
     email = models.CharField(max_length=50)
     contact = models.IntegerField()
     dt = models.CharField(max_length=50)
     status = models.CharField(max_length=50)


class chicken_batch_details(models.Model):
    #id = models.CharField(max_length=100)
    user_id = models.IntegerField()
    company_id= models.IntegerField()
    total_count = models.IntegerField()
    total_load = models.IntegerField()
    dt = models.CharField(max_length=50)
    status= models.CharField(max_length=50)
    no_of_days = models.IntegerField()


class daily_batchlog(models.Model):
    #id = models.CharField(max_length=100)
    batch_id = models.IntegerField()
    avg_weight = models.IntegerField()
    total_death = models.IntegerField()
    dt = models.CharField(max_length=50)
    status= models.CharField(max_length=50)

class daily_feedinglog(models.Model):
    #id = models.CharField(max_length=100)
    batch_id = models.IntegerField()
    feed_name = models.CharField(max_length=100)
    feed_quantity = models.IntegerField()
    time= models.CharField(max_length=50)
    dt = models.CharField(max_length=50)
    status= models.CharField(max_length=50)

class doctor_consultation(models.Model):
    #id = models.CharField(max_length=100)
    doctor_id = models.IntegerField()
    farmer_id = models.IntegerField()
    batch_id = models.IntegerField()
    query = models.CharField(max_length=100)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    prescription= models.CharField(max_length=100)
    p_date=models.CharField(max_length=100)
    status= models.CharField(max_length=50)

class shop_medicine_stock(models.Model):
    #id = models.CharField(max_length=100)
    medicine_name = models.CharField(max_length=100)
    medicine_company = models.CharField(max_length=100)
    batch_code= models.CharField(max_length=100)
    medicine_description= models.CharField(max_length=50)
    stock = models.IntegerField()
    amount = models.IntegerField()


class medicineshop(models.Model):
    user_id = models.IntegerField()
    medicine_shop_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    pin = models.IntegerField()
    contact = models.IntegerField()


class farmer_cart(models.Model):
    farmer_id = models.IntegerField()
    medicine_id = models.IntegerField()
    quantity = models.IntegerField()
    amount= models.IntegerField()


class shop_farmer_sales(models.Model):
    #id = models.CharField(max_length=100)
    farmer_id = models.IntegerField()
    bill_no = models.IntegerField()
    bill_date = models.CharField(max_length=100)
    total_amount= models.FloatField()
    status= models.CharField(max_length=50)


class bill_details(models.Model):
    #id = models.CharField(max_length=100)
    bill_id = models.IntegerField()
    medicine_id = models.IntegerField()
    quantity = models.IntegerField()
    amount= models.IntegerField()

class bill_transaction(models.Model):
    #id = models.CharField(max_length=100)
    bill_id = models.IntegerField()
    farmer_id = models.IntegerField()
    card_no = models.IntegerField()
    cvv = models.IntegerField()
    amount = models.FloatField()
    dt= models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    remarks = models.CharField(max_length=100)
    status= models.CharField(max_length=50)


class farmer_manager_query(models.Model):
    #id = models.CharField(max_length=100)
    farmer_id = models.IntegerField()
    manager_id = models.IntegerField()
    query= models.CharField(max_length=500)
    q_dt = models.CharField(max_length=100)
    q_time = models.CharField(max_length=100)
    reply = models.CharField(max_length=500)
    r_dt = models.CharField(max_length=100)
    r_time = models.CharField(max_length=100)
    status=models.CharField(max_length=100)


class farmer_batch_sales(models.Model):
    #id = models.CharField(max_length=100)
    farmer_id = models.IntegerField()
    company_id = models.IntegerField()
    total_count= models.IntegerField()
    total_weight = models.FloatField()
    price = models.FloatField()
    total_price= models.FloatField()
    dt = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    status=models.CharField(max_length=100)



class general_info(models.Model):
    #id = models.CharField(max_length=100)
    manager_id = models.IntegerField()
    title= models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    dt = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class manager_details(models.Model):
    #id = models.CharField(max_length=100)
    user_id = models.IntegerField()
    company_id = models.IntegerField()
    f_name = models.CharField(max_length=100)
    l_name= models.CharField(max_length=100)
    gender= models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    pin= models.IntegerField()
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.IntegerField()



class supervisor_details(models.Model):
    #id = models.CharField(max_length=100)
    user_id = models.IntegerField()
    company_id = models.IntegerField()
    f_name = models.CharField(max_length=100)
    l_name= models.CharField(max_length=100)
    gender= models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    pin= models.IntegerField()
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.IntegerField()



