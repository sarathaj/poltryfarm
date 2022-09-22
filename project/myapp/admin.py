from django.contrib import admin

# Register your models here.
# Register your models here.
from . models import  user_login,store_details,doctor_details,company_details,chicken_batch_details,\
    daily_batchlog,daily_feedinglog,doctor_consultation,shop_medicine_stock,shop_farmer_sales
from . models import bill_details,bill_transaction,farmer_manager_query,farmer_batch_sales,general_info,farmer_cart
from . models import manager_details,medicineshop,farmer_details,supervisor_details









admin.site.register(user_login)
admin.site.register(store_details)
admin.site.register(doctor_details)
admin.site.register(company_details)
admin.site.register(chicken_batch_details)
admin.site.register(daily_batchlog)
admin.site.register(daily_feedinglog)
admin.site.register(doctor_consultation)
admin.site.register(shop_medicine_stock)
admin.site.register(shop_farmer_sales)
admin.site.register(bill_details)
admin.site.register(bill_transaction)
admin.site.register(farmer_manager_query)
admin.site.register(farmer_batch_sales)
admin.site.register(general_info)
admin.site.register(manager_details)
admin.site.register(medicineshop)
admin.site.register(farmer_details)
admin.site.register(supervisor_details)
admin.site.register(farmer_cart)

