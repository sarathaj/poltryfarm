"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
urlpatterns = [

    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    ######################***-----ADMIN-----***######################

    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('admin_doctor_add', views.admin_doctor_add, name='admin_doctor_add'),
    path('admin_doctor_edit', views.admin_doctor_edit, name='admin_doctor_edit'),
    path('admin_doctor_view', views.admin_doctor_view, name='admin_doctor_view'),
    path('admin_doctor_delete', views.admin_doctor_delete, name='admin_doctor_delete'),

    path('admin_company_details_add', views.admin_company_details_add, name='admin_company_details_add'),
    path('admin_company_details_edit', views.admin_company_details_edit, name='admin_company_details_edit'),
    path('admin_company_details_view', views.admin_company_details_view, name='admin_company_details_view'),
    path('admin_company_details_delete', views.admin_company_details_delete, name='admin_company_details_delete'),

    path('admin_medicineshop_add', views.admin_medicineshop_add, name='admin_medicineshop_add'),
    path('admin_medicineshop_edit', views.admin_medicineshop_edit, name='admin_medicineshop_edit'),
    path('admin_medicineshop_view', views.admin_medicineshop_view, name='admin_medicineshop_view'),
    path('admin_medicineshop_delete', views.admin_medicineshop_delete, name='admin_medicineshop_delete'),


    ######################***-----MANAGER-----***######################

    path('manager_login', views.manager_login, name='manager_login'),
    path('manager_home', views.manager_home, name='manager_home'),
    path('manager_logout', views.manager_logout, name='manager_logout'),
    path('manager_changepassword', views.manager_changepassword, name='manager_changepassword'),

    path('manager_farmer_add', views.manager_farmer_add, name='manager_farmer_add'),
    path('manager_farmer_edit', views.manager_farmer_edit, name='manager_farmer_edit'),
    path('manager_farmer_view', views.manager_farmer_view, name='manager_farmer_view'),
    path('manager_farmer_delete', views.manager_farmer_delete, name='manager_farmer_delete'),

    path('manager_supervisor_add', views.manager_supervisor_add, name='manager_supervisor_add'),
    path('manager_supervisor_edit', views.manager_supervisor_edit, name='manager_supervisor_edit'),
    path('manager_supervisor_view', views.manager_supervisor_view, name='manager_supervisor_view'),
    path('manager_supervisor_delete', views.manager_supervisor_delete, name='manager_supervisor_delete'),

    path('manager_general_info_add', views.manager_general_info_add, name='manager_general_info_add'),
    path('manager_general_info_view', views.manager_general_info_view, name='manager_general_info_view'),
    path('manager_general_info_edit', views.manager_general_info_edit, name='manager_general_info_edit'),
    path('manager_general_info_delete', views.manager_general_info_delete, name='manager_general_info_delete'),

    path('manager_batch_details_view', views.manager_batch_details_view, name='manager_batch_details_view'),
    path('manager_daily_feedlog_view', views.manager_daily_feedlog_view, name='manager_daily_feedlog_view'),
    path('manager_daily_batch_log_view', views.manager_daily_batch_log_view, name='manager_daily_batch_log_view'),

    path('manager_farmer_query_view', views.manager_farmer_query_view, name='manager_farmer_query_view'),
    path('manager_farmer_query_reply', views.manager_farmer_query_reply, name='manager_farmer_query_reply'),



    ######################***-----COMPANY-----***######################

    path('company_login', views.company_login, name='company_login'),
    path('company_home', views.company_home, name='company_home'),
    path('company_logout', views.company_logout, name='company_logout'),
    path('company_changepassword', views.company_changepassword, name='company_changepassword'),

    path('company_manager_details_add', views.company_manager_details_add, name='company_manager_details_add'),
    path('company_manager_details_edit', views.company_manager_details_edit, name='company_manager_details_edit'),
    path('company_manager_details_view', views.company_manager_details_view, name='company_manager_details_view'),
    path('company_manager_details_delete', views.company_manager_details_delete, name='company_manager_details_delete'),

    path('company_doctor_details_add', views.company_doctor_details_add, name='company_doctor_details_add'),
    path('company_doctor_details_view', views.company_doctor_details_view, name='company_doctor_details_view'),
    path('company_doctor_details_edit', views.company_doctor_details_edit, name='company_doctor_details_edit'),
    path('company_doctor_details_delete', views.company_doctor_details_delete, name='company_doctor_details_delete'),


    ####################***-----SUPERVISOR-----***####################

    path('supervisor_logout', views.supervisor_logout, name='supervisor_logout'),
    path('supervisor_changepassword', views.supervisor_changepassword, name='supervisor_changepassword'),
    path('supervisor_home', views.supervisor_home, name='supervisor_home'),
    path('supervisor_login', views.supervisor_login, name='supervisor_login'),

    path('supervisor_farmer_details_view', views.supervisor_farmer_details_view, name='supervisor_farmer_details_view'),
    path('supervisor_batch_details_add', views.supervisor_batch_details_add, name='supervisor_batch_details_add'),
    path('supervisor_batch_details_view', views.supervisor_batch_details_view, name='supervisor_batch_details_view'),

    path('supervisor_general_info_view', views.supervisor_general_info_view, name='supervisor_general_info_view'),

    path('supervisor_daily_batch_log_view', views.supervisor_daily_batch_log_view, name='supervisor_daily_batch_log_view'),
    path('supervisor_daily_feedlog_view', views.supervisor_daily_feedlog_view, name='supervisor_daily_feedlog_view'),

    ######################***-----FARMER-----***######################

    path('farmer_login', views.farmer_login, name='farmer_login'),
    path('farmer_home', views.farmer_home, name='farmer_home'),
    path('farmer_logout', views.farmer_logout, name='farmer_logout'),
    path('farmer_changepassword', views.farmer_changepassword, name='farmer_changepassword'),

    path('farmer_batch_details_view', views.farmer_batch_details_view, name='farmer_batch_details_view'),

    path('farmer_daily_batch_log_add', views.farmer_daily_batch_log_add, name='farmer_daily_batch_log_add'),
    path('farmer_daily_batch_log_view', views.farmer_daily_batch_log_view, name='farmer_daily_batch_log_view'),
    path('farmer_daily_batch_log_edit', views.farmer_daily_batch_log_edit, name='farmer_daily_batch_log_edit'),

    path('farmer_daily_feedlog_add', views.farmer_daily_feedlog_add, name='farmer_daily_feedlog_add'),
    path('farmer_daily_feedlog_view', views.farmer_daily_feedlog_view, name='farmer_daily_feedlog_view'),
    path('farmer_daily_feedlog_edit', views.farmer_daily_feedlog_edit, name='farmer_daily_feedlog_edit'),

    path('farmer_general_info_view', views.farmer_general_info_view, name='farmer_general_info_view'),

    path('farmer_doctor_details_view', views.farmer_doctor_details_view, name='farmer_doctor_details_view'),
    path('farmer_doctor_consultation_add', views.farmer_doctor_consultation_add, name='farmer_doctor_consultation_add'),
    path('farmer_doctor_consultation_view', views.farmer_doctor_consultation_view, name='farmer_doctor_consultation_view'),
    path('farmer_doctor_consultation_delete', views.farmer_doctor_consultation_delete,
         name='farmer_doctor_consultation_delete'),
    path('farmer_medicine_details_view', views.farmer_medicine_details_view,
         name='farmer_medicine_details_view'),
    path('farmer_medicine_to_cart_add', views.farmer_medicine_to_cart_add,
         name='farmer_medicine_to_cart_add'),
    path('farmer_medicine_to_cart_view', views.farmer_medicine_to_cart_view,
         name='farmer_medicine_to_cart_view'),
    path('farmer_remove_medicine_from_cart', views.farmer_remove_medicine_from_cart,
         name='farmer_remove_medicine_from_cart'),
    path('farmer_medicine_purchase_add', views.farmer_medicine_purchase_add,
         name='farmer_medicine_purchase_add'),

    path('farmer_transaction_details_view', views.farmer_transaction_details_view,
         name='farmer_transaction_details_view'),
    path('farmer_transaction_details_view1', views.farmer_transaction_details_view1,
         name='farmer_transaction_details_view1'),

    path('farmer_company_details_view', views.farmer_company_details_view,
         name='farmer_company_details_view'),

    path('farmer_manager_details_view', views.farmer_manager_details_view,
         name='farmer_manager_details_view'),

    path('farmer_manager_query_add', views.farmer_manager_query_add,
         name='farmer_manager_query_add'),

    path('farmer_manager_query_view', views.farmer_manager_query_view, name='farmer_manager_query_view'),
    path('farmer_batch_sales_add', views.farmer_batch_sales_add, name='farmer_batch_sales_add'),
    path('farmer_batch_sales_view', views.farmer_batch_sales_view, name='farmer_batch_sales_view'),


    ######################***-----DOCTOR-----***######################

    path('doctor_login', views.doctor_login, name='doctor_login'),
    path('doctor_home', views.doctor_home, name='doctor_home'),
    path('doctor_logout', views.doctor_logout, name='doctor_logout'),
    path('doctor_changepassword', views.doctor_changepassword, name='doctor_changepassword'),

    path('doctor_farmer_consultation_view', views.doctor_farmer_consultation_view,
         name='doctor_farmer_consultation_view'),
    path('doctor_farmer_consultation_reply', views.doctor_farmer_consultation_reply,
         name='doctor_farmer_consultation_reply'),
    path('doctor_farmer_consultation_history', views.doctor_farmer_consultation_history,
         name='doctor_farmer_consultation_history'),

    path('doctor_batch_details_view', views.doctor_batch_details_view, name='doctor_batch_details_view'),
    path('doctor_daily_batch_log_view', views.doctor_daily_batch_log_view,
         name='doctor_daily_batch_log_view'),
    path('doctor_daily_feedlog_view', views.doctor_daily_feedlog_view,
         name='doctor_daily_feedlog_view'),
    ###################***-----MEDICINESHOP-----***###################

    path('medicineshop_login', views.medicineshop_login, name='medicineshop_login'),
    path('medicineshop_home', views.medicineshop_home, name='medicineshop_home'),
    path('medicineshop_logout', views.medicineshop_logout, name='medicineshop_logout'),
    path('medicineshop_changepassword', views.medicineshop_changepassword, name='medicineshop_changepassword'),

    path('medicineshop_medicine_add', views.medicineshop_medicine_add, name='medicineshop_medicine_add'),
    path('medicineshop_medicine_edit', views.medicineshop_medicine_edit, name='medicineshop_medicine_edit'),
    path('medicineshop_medicine_view', views.medicineshop_medicine_view, name='medicineshop_medicine_view'),
    path('medicineshop_medicine_delete', views.medicineshop_medicine_delete, name='medicineshop_medicine_delete'),

    path('medicineshop_transaction_details_view', views.medicineshop_transaction_details_view,
         name='medicineshop_transaction_details_view'),
    path('medicineshop_transaction_details_view1', views.medicineshop_transaction_details_view1,
         name='medicineshop_transaction_details_view1'),
    path('company_farmer_batch_sales_view', views.company_farmer_batch_sales_view, name='company_farmer_batch_sales_view'),
    path('company_farmer_payment_add', views.company_farmer_payment_add, name='company_farmer_payment_add'),


    #######################***-----USER-----***#######################

    path('user_home', views.user_home, name='user_home'),
    path('user_login', views.user_login_check, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),


]
