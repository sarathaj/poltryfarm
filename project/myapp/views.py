import datetime

from django.shortcuts import render

# Create your views here.
from django.db.models import Max
from .models import user_login, doctor_details, shop_medicine_stock, medicineshop, company_details, farmer_details, \
    supervisor_details


def index(request):
    return render(request, './myapp/index.html')


def about(request):
    return render(request, './myapp/about.html')


def contact(request):
    return render(request, './myapp/contact.html')

############################************ADMIN**************#####################################

def admin_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='admin')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/admin_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/admin_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/admin_login.html',context)


def admin_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/admin_home.html')


def admin_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return admin_login(request)
    else:
        return admin_login(request)


def admin_changepassword(request):
    if request.method == 'POST':
        opasswd = request.POST.get('opasswd')
        npasswd = request.POST.get('npasswd')
        cpasswd = request.POST.get('cpasswd')
        uname = request.session['user_name']
        try:
            ul = user_login.objects.get(uname=uname,passwd=opasswd,u_type='admin')
            if ul is not None:
                ul.passwd=npasswd
                ul.save()
                context = {'msg': 'Password Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/admin_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Err Not Changed'}
            return render(request, './myapp/admin_changepassword.html', context)
    else:
        context = {'msg': ''}
        return render(request, './myapp/admin_changepassword.html', context)



def admin_company_details_add(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = '1234'
        uname = email
        # status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='company')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = company_details(user_id=user_id, name=name, address=addr, pin=pin, contact=contact, email=email, )
        ud.save()

        print(user_id)
        context = {'msg': 'Company Owner Registered'}
        return render(request, 'myapp/admin_company_details_add.html', context)

    else:
        return render(request, 'myapp/admin_company_details_add.html')




def admin_company_details_edit(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        name = request.POST.get('name')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        c_obj = company_details.objects.get(id=int(user_id))
        c_obj.name = name
        c_obj.addr= addr
        c_obj.pin = pin
        c_obj.email = email
        c_obj.contact=contact
        c_obj.save()
        msg = 'companyowner record Updated'
        context = {'msg': msg}
        return render(request, 'myapp/admin_company_details_edit.html', context)
    else:
        id = request.GET.get('id')
        c_obj = company_details.objects.get(id=int(id))
        context = {'c_obj': c_obj, 'user_id': c_obj.id}
        return render(request, './myapp/admin_company_details_edit.html', context)


def admin_company_details_view(request):
    company_list = company_details.objects.all()
    context = {'company_list': company_list, 'msg': ''}
    return render(request, 'myapp/admin_company_details_view.html', context)


def admin_company_details_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    cg = company_details.objects.get(id=int(id))
    cg.delete()
    msg = "Company Deleted"

    company_list=company_details.objects.all()
    context = {'company_list': company_list,'msg':msg}
    return render(request,'./myapp/admin_company_details_view.html',context)


def admin_doctor_edit(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        fname = request.POST.get('f_name')
        lname = request.POST.get('l_name')
        gender= request.POST.get('gender')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        d_obj = doctor_details.objects.get(id=int(user_id))
        d_obj.f_name = fname
        d_obj.l_name = lname
        d_obj.gender= gender
        d_obj.dob = dob
        d_obj.addr= addr
        d_obj.pin = pin
        d_obj.email = email
        d_obj.contact=contact
        d_obj.save()
        msg = 'Doctor record Updated'
        context = {'msg': msg}
        return render(request, 'myapp/admin_doctor_edit.html', context)
    else:
        id = request.GET.get('id')
        d_obj = doctor_details.objects.get(id=int(id))
        context = {'d_obj': d_obj, 'user_id': d_obj.id}
        return render(request, './myapp/admin_doctor_edit.html', context)


def admin_doctor_view(request):
    doctor_list = doctor_details.objects.all()
    context = {'doctor_list': doctor_list, 'msg': ''}
    return render(request, 'myapp/admin_doctor_view.html', context)


def admin_doctor_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    cg = doctor_details.objects.get(id=int(id))
    cg.delete()
    msg = "Doctor deleted"

    doctor_list=doctor_details.objects.all()
    context = {'doctor list': doctor_list,'msg':msg}
    return render(request,'./myapp/admin_doctor_view.html',context)


def admin_medicineshop_edit(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        name = request.POST.get('msname')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        contact = request.POST.get('contact')
        ms_obj = medicineshop.objects.get(id=int(user_id))
        ms_obj.medicine_shop_name = name
        ms_obj.address= addr
        ms_obj.pin = pin
        ms_obj.contact=contact
        ms_obj.save()
        msg = 'Medicineshop Record Updated'
        context = {'msg': msg,'ms_obj': ms_obj,'user_id': ms_obj.id}
        return render(request, 'myapp/admin_medicineshop_edit.html', context)
    else:
        id = request.GET.get('id')
        ms_obj = medicineshop.objects.get(id=int(id))
        context = {'ms_obj': ms_obj, 'user_id': ms_obj.id}
        return render(request, './myapp/admin_medicineshop_edit.html', context)


def admin_medicineshop_view(request):
    medicineshop_list = medicineshop.objects.all()
    context = {'medicineshop_list': medicineshop_list, 'msg': ''}
    return render(request, 'myapp/admin_medicineshop_view.html', context)


def admin_medicineshop_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    cg = medicineshop.objects.get(id=int(id))
    cg.delete()
    msg = "Medicineshop Deleted"

    medicineshop_list=medicineshop.objects.all()
    context = {'medicineshop list': medicineshop_list,'msg':msg}
    return render(request,'./myapp/admin_medicineshop_view.html',context)




def admin_doctor_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')

        password = '1234'
        uname = email
        # status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='doctor')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = doctor_details(user_id=user_id, f_name=fname, l_name=lname, gender=gender, dob=dob, address=addr, pin=pin,
                            contact=contact, email=email)
        ud.save()

        print(user_id)
        context = {'msg': 'Doctor Registered'}
        return render(request, 'myapp/admin_doctor_add.html', context)

    else:
        return render(request, 'myapp/admin_doctor_add.html')


def admin_medicineshop_add(request):
    if request.method == 'POST':

        msname = request.POST.get('msname')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        contact = request.POST.get('contact')
        password = '1234'
        uname = msname
        # status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='medshop')
        ul.save()
        user_id = user_login.objects.latest('id').id
        print('..........', user_id)

        ud = medicineshop(user_id=user_id, medicine_shop_name=msname, address=addr, pin=pin, contact=contact)
        ud.save()

        context = {'msg': 'medicine shop Registered'}
        return render(request, 'myapp/admin_medicineshop_add.html', context)

    else:
        return render(request, 'myapp/admin_medicineshop_add.html')





################################***--MANAGER--***################################


def manager_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='manager')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/manager_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/manager_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/manager_login.html',context)


def manager_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/manager_home.html')


def manager_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)


def manager_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/manager_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/manager_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/manager_changepassword.html', context)
    else:
        return render(request, './myapp/manager_changepassword.html')


def manager_supervisor_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')

        password = '1234'
        uname = email
        # status = "new"
        manager_id = request.session['user_id']
        md = manager_details.objects.get(user_id=manager_id)

        ul = user_login(uname=uname, passwd=password, u_type='supervisor')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = supervisor_details(user_id=user_id, company_id=md.company_id,f_name=fname, l_name=lname, gender=gender, dob=dob, address=addr,
                                pin=pin, contact=contact, email=email)
        ud.save()

        print(user_id)
        context = {'msg': ' Supervisor Registered'}
        return render(request, 'myapp/manager_supervisor_add.html', context)

    else:
        return render(request, 'myapp/manager_supervisor_add.html')


def manager_supervisor_view(request):
    supervisor_list = supervisor_details.objects.all()
    context = {'supervisor_list': supervisor_list, 'msg': ''}
    return render(request, 'myapp/manager_supervisor_view.html', context)


def manager_supervisor_edit(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        fname = request.POST.get('f_name')
        lname = request.POST.get('l_name')
        gender= request.POST.get('gender')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        ms_obj = supervisor_details.objects.get(id=int(user_id))
        ms_obj.f_name = fname
        ms_obj.l_name = lname
        ms_obj.gender= gender
        ms_obj.dob = dob
        ms_obj.addr= addr
        ms_obj.pin = pin
        ms_obj.email = email
        ms_obj.contact=contact
        ms_obj.save()
        msg = 'Supervisor record Updated'
        context = {'msg': msg, 'ms_obj': ms_obj,'user_id': ms_obj.id}
        return render(request, 'myapp/manager_supervisor_edit.html', context)
    else:
        id = request.GET.get('id')
        ms_obj = supervisor_details.objects.get(id=int(id))
        context = {'ms_obj': ms_obj, 'user_id': ms_obj.id}
        return render(request, './myapp/manager_supervisor_edit.html', context)


def manager_supervisor_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    cg = supervisor_details.objects.get(id=int(id))
    cg.delete()
    msg = "supervisor deleted"

    supervisor_list = supervisor_details.objects.all()
    context = {'supervisor list': supervisor_list,'msg':msg}
    return render(request,'./myapp/manager_supervisor_view.html',context)


def manager_farmer_add(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        lname = request.POST.get('lname')

        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')

        password = '1234'
        uname = email
        # status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='farmer')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = farmer_details(user_id=user_id, f_name=fname, l_name=lname, gender=gender, dob=dob, address=addr, pin=pin,
                            contact=contact, email=email)
        ud.save()

        print(user_id)
        context = {'msg': ' Farmer Registered'}
        return render(request, 'myapp/manager_farmer_add.html', context)

    else:
        return render(request, 'myapp/manager_farmer_add.html')


def manager_farmer_edit(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        fname = request.POST.get('f_name')
        lname = request.POST.get('l_name')
        gender= request.POST.get('gender')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        mf_obj = farmer_details.objects.get(id=int(user_id))
        mf_obj.f_name = fname
        mf_obj.l_name = lname
        mf_obj.gender= gender
        mf_obj.dob = dob
        mf_obj.addr= addr
        mf_obj.pin = pin
        mf_obj.email = email
        mf_obj.contact=contact
        mf_obj.save()
        msg = 'Farmer record Updated'
        context = {'msg': msg, 'mf_obj': mf_obj}
        return render(request, 'myapp/manager_farmer_edit.html', context)
    else:
        id = request.GET.get('id')
        mf_obj = farmer_details.objects.get(id=int(id))
        context = {'mf_obj': mf_obj, 'user_id': mf_obj.id}
        return render(request, './myapp/manager_farmer_edit.html', context)


def manager_farmer_view(request):
    farmer_list = farmer_details.objects.all()
    context = {'farmer_list': farmer_list, 'msg': ''}
    return render(request, 'myapp/manager_farmer_view.html', context)


def manager_farmer_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    cg = farmer_details.objects.get(id=int(id))
    fd = user_login.objects.get(id=cg.user_id)
    fd.delete()
    cg.delete()
    msg = "Farmer deleted"

    farmer_list=farmer_details.objects.all()
    context = {'farmer list': farmer_list,'msg':msg}
    return render(request,'./myapp/manager_farmer_view.html',context)

from . models import general_info

def manager_general_info_add(request):
    if request.method == 'POST':
        manager_id = request.session['user_id']
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        dt = datetime.datetime.today().strftime('%Y-%m-%d')
        time = datetime.datetime.today().strftime('%H:%M:%S')
        # status = 'new'
        general_info(manager_id=manager_id, title=title, desc=desc, dt=dt, time=time).save()
        msg = 'General Info Added'
        context = {'msg':msg}
        return render(request, './myapp/manager_general_info_add.html', context)
    else:
        return render(request, './myapp/manager_general_info_add.html')



def manager_general_info_view(request):
    manager_id = request.session['user_id']
    news_list = general_info.objects.filter(manager_id=manager_id)
    context = {'news_list':news_list}
    return render(request, './myapp/manager_general_info_view.html', context)


def manager_general_info_delete(request):
    id = request.GET.get('id')
    gn = general_info.objects.get(id=id)
    gn.delete()
    manager_id = request.session['user_id']
    news_list = general_info.objects.filter(manager_id=manager_id)
    context = {'news_list':news_list}
    return render(request, './myapp/manager_general_info_view.html', context)


def manager_general_info_edit(request):
    if request.method == 'POST':
        id = request.POST.get('gn_id')
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        # status = 'new'
        gn = general_info.objects.get(id=id)
        gn.title=title
        gn.desc=desc
        gn.save()
        msg = 'General Info Updated'
        context = {'msg':msg,'gn': gn, 'gn_id': gn.id}
        return render(request, './myapp/manager_general_info_edit.html', context)
    else:
        id = request.GET.get('id')
        gn = general_info.objects.get(id=id)
        context = {'gn':gn, 'gn_id':gn.id}
        return render(request, './myapp/manager_general_info_edit.html',context)



def manager_batch_details_view(request):

    user_id = request.GET.get('farmer_id')
    b_l = chicken_batch_details.objects.filter(user_id=user_id)

    #############################################################################
    dict1 ={}
    result = 0
    for b in b_l:
        feed_log = daily_feedinglog.objects.filter(batch_id=b.id)
        tot_feed = 0
        for f in feed_log:
            tot_feed = tot_feed + f.feed_quantity
        print(tot_feed)
        batch_log_id = daily_batchlog.objects.filter(batch_id=b.id).aggregate(Max('id'))['id__max']
        if batch_log_id is not None:
            bt = daily_batchlog.objects.get(id=batch_log_id)
            print('bt.id', bt.id)
            result = (tot_feed / bt.avg_weight) * 100
            dict1[b.id]=round(result,3)
        else:
            result = 0
        print('dict1-----------',dict1)
    #############################################################################


    context = {'batch_list':b_l,'farmer_id':user_id,'result':str(result),'dict1':dict1}
    return render(request, './myapp/manager_batch_details_view.html', context)



def manager_daily_batch_log_view(request):
    batch_id = request.GET.get('batch_id')
    print('bid',batch_id)
    batch_log = daily_batchlog.objects.filter(batch_id=batch_id)
    print(len(batch_log))
    context = {'batch_log':batch_log,'batch_id':batch_id}
    return render(request, './myapp/manager_daily_batch_log_view.html',context)


def manager_daily_feedlog_view(request):
    batch_id = request.GET.get('batch_id')
    print('bid',batch_id)
    feed_log = daily_feedinglog.objects.filter(batch_id=batch_id)
    context = {'feed_log':feed_log,'batch_id':batch_id}
    return render(request, './myapp/manager_daily_feedlog_view.html',context)



def manager_farmer_query_view(request):
    manager_id = request.session['user_id']
    fm_q = farmer_manager_query.objects.filter(manager_id = manager_id)
    fd = farmer_details.objects.all()
    context = {'message_list':fm_q,'farmer_list':fd}
    return render(request, './myapp/manager_farmer_query_view.html', context)



def manager_farmer_query_reply(request):
    if request.method == 'POST':
        manager_id = request.session['user_id']
        query_id = request.POST.get('query_id')
        fm_q = farmer_manager_query.objects.get(id=query_id)
        r_dt = datetime.today().strftime('%Y-%m-%d')
        r_time = datetime.today().strftime('%H:%M:%S')
        reply = request.POST.get('reply')
        fm_q.reply = reply
        fm_q.r_dt = r_dt
        fm_q.r_time = r_time
        fm_q.status = 'Replied'
        fm_q.save()
        msg = 'Replied...'
        context = {'query_id':query_id,'msg':msg}
        return render(request, './myapp/manager_farmer_query_reply.html', context)
    else:
        id = request.GET.get('id')
        context = {'query_id':id}
        return render(request, './myapp/manager_farmer_query_reply.html', context)





############################***--COMPANY--***#################################################
#todo:Company
def company_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='company')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/company_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/company_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/company_login.html',context)


def company_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/company_home.html')


def company_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)


def company_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/company_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/company_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/company_changepassword.html', context)
    else:
        return render(request, './myapp/company_changepassword.html')



from . models import manager_details


def company_manager_details_add(request):
    if request.method == 'POST':
        company_id = request.session['user_id']
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = '1234'
        uname=email
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='manager')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = manager_details(user_id=user_id,company_id=company_id,f_name=fname, l_name=lname, gender=gender,dob=dob,address=addr, pin=pin, contact=contact, email=email, )
        ud.save()

        print(user_id)
        context = {'msg': 'Manager Registered'}
        return render(request, 'myapp/company_manager_details_add.html',context)

    else:
        return render(request, 'myapp/company_manager_details_add.html')


def company_manager_details_edit(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        fname = request.POST.get('f_name')
        lname = request.POST.get('l_name')
        gender= request.POST.get('gender')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        md_obj = manager_details.objects.get(id=int(user_id))
        md_obj.f_name = fname
        md_obj.l_name = lname
        md_obj.gender= gender
        md_obj.dob = dob
        md_obj.addr= addr
        md_obj.pin = pin
        md_obj.email = email
        md_obj.contact=contact
        md_obj.save()
        msg = 'Manager record Updated'
        context = {'msg': msg, 'md_obj':md_obj, 'user_id': user_id}
        return render(request, 'myapp/company_manager_details_edit.html', context)
    else:
        id = request.GET.get('id')
        md_obj = manager_details.objects.get(id=int(id))
        context = {'md_obj': md_obj, 'user_id': md_obj.id}
        return render(request, './myapp/company_manager_details_edit.html', context)


def company_manager_details_view(request):
    company_id = request.session['user_id']
    manager_list = manager_details.objects.filter(company_id=int(company_id))
    context = {'manager_list': manager_list, 'msg': ''}
    return render(request, 'myapp/company_manager_details_view.html', context)


def company_manager_details_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    cg = manager_details.objects.get(id=int(id))
    cg.delete()
    msg = "Manager Deleted"
    company_id = request.session['user_id']
    manager_list = manager_details.objects.filter(company_id=int(company_id))
    context = {'manager list': manager_list,'msg':msg}
    return render(request,'./myapp/company_manager_details_view.html',context)

def company_doctor_details_add(request):
    if request.method == 'POST':
        company_id = request.session['user_id']
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')

        password = '1234'
        uname = email
        # status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='doctor')
        ul.save()
        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = doctor_details(company_id=company_id, user_id=user_id, f_name=fname, l_name=lname, gender=gender, dob=dob, address=addr,
                            pin=pin,
                            contact=contact, email=email)
        ud.save()

        print(user_id)
        context = {'msg': 'Doctor Registered'}
        return render(request, 'myapp/company_doctor_details_add.html', context)

    else:
        return render(request, 'myapp/company_doctor_details_add.html')



def company_doctor_details_view(request):
    company_id = request.session['user_id']
    doctor_list = doctor_details.objects.filter(company_id=company_id)
    context = {'doctor_list': doctor_list, 'msg': ''}
    return render(request, 'myapp/company_doctor_details_view.html', context)

def company_doctor_details_edit(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        fname = request.POST.get('f_name')
        lname = request.POST.get('l_name')
        gender= request.POST.get('gender')
        dob = request.POST.get('dob')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        d_obj = doctor_details.objects.get(id=int(doctor_id))
        d_obj.f_name = fname
        d_obj.l_name = lname
        d_obj.gender= gender
        d_obj.dob = dob
        d_obj.addr= addr
        d_obj.pin = pin
        d_obj.email = email
        d_obj.contact=contact
        d_obj.save()
        msg = 'Doctor record Updated'
        context = {'msg': msg,'d_obj': d_obj}
        return render(request, 'myapp/company_doctor_details_edit.html', context)
    else:
        doctor_id = request.GET.get('id')
        d_obj = doctor_details.objects.get(id=int(doctor_id))
        context = {'d_obj': d_obj, 'doctor_id': d_obj.id}
        return render(request, './myapp/company_doctor_details_edit.html', context)

def company_doctor_details_delete(request):
    id = request.GET.get('id')
    print('id = '+id)
    cg = doctor_details.objects.get(id=int(id))
    cg.delete()
    msg = "Doctor deleted"

    company_id = request.session['user_id']
    doctor_list = doctor_details.objects.filter(company_id=company_id)
    context = {'doctor_list': doctor_list, 'msg': msg}
    return render(request,'./myapp/company_doctor_details_view.html',context)

############################***--SUPERVISOR--***############################

def supervisor_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='supervisor')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/supervisor_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/supervisor_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/supervisor_login.html',context)


def supervisor_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/supervisor_home.html')


def supervisor_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)


def supervisor_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))
        try:
            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/supervisor_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/supervisor_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/supervisor_changepassword.html', context)
    else:
        return render(request, './myapp/supervisor_changepassword.html')



def supervisor_farmer_details_view(request):
    farmer_list = farmer_details.objects.all()
    context = {'farmer_list':farmer_list}
    return render(request, './myapp/supervisor_farmer_details_view.html', context)


from . models import chicken_batch_details
def supervisor_batch_details_add(request):
    if request.method == 'POST':
        sup_id = request.session['user_id']
        sp = supervisor_details.objects.get(user_id = sup_id)
        user_id = request.POST.get('farmer_id')
        # company_id = request.POST.get('company_id')
        total_count = request.POST.get('totcount')
        total_load = request.POST.get('totload')
        dt = datetime.today().strftime('%Y-%m-%d')
        status = 'New'
        no_of_days = request.POST.get('no_days')
        cbd = chicken_batch_details(user_id=user_id, company_id=sp.company_id, total_count=total_count, total_load=total_load, dt=dt, status=status,
                                    no_of_days=no_of_days)
        cbd.save()
        msg = 'New Batch Added'
        context  = {'msg':msg}
        return render(request, './myapp/supervisor_batch_details_add.html', context)
    else:
        farmer_id = request.GET.get('farmer_id')
        context = {'farmer_id':farmer_id}
        return render(request, './myapp/supervisor_batch_details_add.html',context)




def supervisor_batch_details_view(request):
    user_id = request.GET.get('farmer_id')
    b_l = chicken_batch_details.objects.filter(user_id=user_id)
    context = {'batch_list':b_l,'farmer_id':user_id}
    return render(request, './myapp/supervisor_batch_details_view.html', context)



def supervisor_general_info_view(request):
    gen_info = general_info.objects.all()
    context = {'gen_info':gen_info}
    return render(request, './myapp/supervisor_general_info_view.html', context)



def supervisor_daily_batch_log_view(request):
    batch_id = request.GET.get('batch_id')
    print('bid',batch_id)
    batch_log = daily_batchlog.objects.filter(batch_id=batch_id)
    print(len(batch_log))
    context = {'batch_log':batch_log,'batch_id':batch_id}
    return render(request, './myapp/supervisor_daily_batch_log_view.html',context)


def supervisor_daily_feedlog_view(request):
    batch_id = request.GET.get('batch_id')
    print('bid',batch_id)
    feed_log = daily_feedinglog.objects.filter(batch_id=batch_id)
    context = {'feed_log':feed_log,'batch_id':batch_id}
    return render(request, './myapp/supervisor_daily_feedlog_view.html',context)

############################***--DOCTOR--***####################################


def doctor_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='doctor')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/doctor_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/doctor_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/doctor_login.html',context)


def doctor_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return doctor_login(request)
    else:
        return render(request,'./myapp/doctor_home.html')


def doctor_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return doctor_login(request)
    else:
        return doctor_login(request)


def doctor_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/doctor_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/doctor_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/doctor_changepassword.html', context)
    else:
        return render(request, './myapp/doctor_changepassword.html')


def doctor_farmer_consultation_view(request):
    doctor_id = request.session['user_id']
    print(doctor_id)
    con_list = doctor_consultation.objects.filter(doctor_id=doctor_id,status='No Reply')
    farmer_list = farmer_details.objects.all()
    context={'con_list':con_list,'farmer_list':farmer_list}
    return render(request, './myapp/doctor_farmer_consultation_view.html', context)

def doctor_farmer_consultation_history(request):
    doctor_id = request.session['user_id']
    print(doctor_id)
    con_list = doctor_consultation.objects.filter(doctor_id=doctor_id,status='Replied')
    farmer_list = farmer_details.objects.all()
    context={'con_list':con_list,'farmer_list':farmer_list}
    return render(request, './myapp/doctor_farmer_consultation_view.html', context)

def doctor_farmer_consultation_reply(request):
    if request.method == 'POST':
        c_id = request.POST.get('c_id')
        prescription = request.POST.get('prescription')
        p_date = datetime.datetime.today().strftime('%Y-%m-%d')
        dc = doctor_consultation.objects.get(id=c_id)
        dc.prescription = prescription
        dc.p_date = p_date
        dc.status = 'Replied'
        dc.save()
        context = {'msg':'Reply Sent..'}
        return render(request, './myapp/doctor_farmer_consultation_reply.html', context)
    else:
        id=request.GET.get('id')
        context = {'c_id':id}
        return render(request, './myapp/doctor_farmer_consultation_reply.html', context)


def doctor_farmer_consultation_search(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        return render(request, './myapp/doctor_farmer_consultation_search.html', )
    else:
        return render(request, './myapp/doctor_farmer_consultation_search.html', )


def doctor_batch_details_view(request):
    id = request.GET.get('id')
    b_l = chicken_batch_details.objects.filter(id=id)
    context = {'batch_list':b_l}
    return render(request, './myapp/doctor_batch_details_view.html', context)


def doctor_daily_batch_log_view(request):
    batch_id = request.GET.get('batch_id')
    print('bid',batch_id)
    batch_log = daily_batchlog.objects.filter(batch_id=batch_id)
    print(len(batch_log))
    context = {'batch_log':batch_log,'batch_id':batch_id}
    return render(request, './myapp/doctor_daily_batch_log_view.html',context)


def doctor_daily_feedlog_view(request):
    batch_id = request.GET.get('batch_id')
    print('bid',batch_id)
    feed_log = daily_feedinglog.objects.filter(batch_id=batch_id)
    context = {'feed_log':feed_log,'batch_id':batch_id}
    return render(request, './myapp/doctor_daily_feedlog_view.html',context)


############################***--FARMER--***####################################

def farmer_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='farmer')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/farmer_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/farmer_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/farmer_login.html',context)


def farmer_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return admin_login(request)
    else:
        return render(request,'./myapp/farmer_home.html')


def farmer_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)


def farmer_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/farmer_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/farmer_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/farmer_changepassword.html', context)
    else:
        return render(request, './myapp/farmer_changepassword.html')




def farmer_batch_details_view(request):
    user_id = request.session['user_id']
    cbd = chicken_batch_details.objects.filter(user_id=user_id)
    cd = company_details.objects.all()
    context = {'batch_list':cbd, 'comp_list':cd}
    return render(request, './myapp/farmer_batch_details_view.html', context)


from . models import daily_batchlog
def farmer_daily_batch_log_add(request):
    if request.method == 'POST':
        batch_id = request.POST.get('batch_id')
        avg_weight = request.POST.get('avg_weight')
        total_death = request.POST.get('total_death')
        dt = datetime.today().strftime('%Y-%m-%d')
        status = 'New'
        db_l = daily_batchlog(batch_id=batch_id, avg_weight=avg_weight,total_death=total_death,
                              dt=dt, status=status)
        db_l.save()
        msg = 'Log Added'
        context = {'msg':msg,'batch_id':batch_id}
        return render(request, './myapp/farmer_daily_batch_log_add.html', context)
    else:
        batch_id = request.GET.get('batch_id')
        context = {'batch_id':batch_id}
        return render(request, './myapp/farmer_daily_batch_log_add.html', context)



def farmer_daily_batch_log_view(request):
    batch_id = request.GET.get('batch_id')
    print('bid',batch_id)
    batch_log = daily_batchlog.objects.filter(batch_id=batch_id)
    print(len(batch_log))
    context = {'batch_log':batch_log,'batch_id':batch_id}
    return render(request, './myapp/farmer_daily_batch_log_view.html',context)


def farmer_daily_batch_log_edit(request):
    if request.method == 'POST':
        log_id = request.POST.get('log_id')
        avg_weight = request.POST.get('avg_weight')
        total_death = request.POST.get('total_death')
        dt = datetime.datetime.today().strftime('%Y-%m-%d')
        status = 'New'
        db_l = daily_batchlog.objects.get(id=log_id)
        # db_l.batch_id=batch_id
        db_l.avg_weight=avg_weight
        db_l.total_death=total_death
        db_l.save()
        msg = 'Log Updated'
        context = {'msg':msg,'log_id':log_id,'dbl':db_l }
        return render(request, './myapp/farmer_daily_batch_log_edit.html', context)
    else:
        id = request.GET.get('id')
        dbl = daily_batchlog.objects.get(id=id)
        context = {'log_id':id,'dbl':dbl}
        return render(request, './myapp/farmer_daily_batch_log_edit.html', context)


from . models import daily_feedinglog
def farmer_daily_feedlog_add(request):
    if request.method == 'POST':
        batch_id = request.POST.get('batch_id')
        feed_name = request.POST.get('feed_name')
        feed_quantity = request.POST.get('feed_quantity')
        time = datetime.today().strftime('%H:%M:%S')
        dt = datetime.today().strftime('%Y-%m-%d')
        status = 'New'
        df_l = daily_feedinglog(batch_id=batch_id, feed_name=feed_name,feed_quantity=feed_quantity,
                              dt=dt, time=time, status=status)
        df_l.save()
        msg = 'Log Added'
        context = {'msg':msg,'batch_id':batch_id}
        return render(request, './myapp/farmer_daily_feedlog_add.html', context)
    else:
        batch_id = request.GET.get('batch_id')
        context = {'batch_id': batch_id}
        return render(request, './myapp/farmer_daily_feedlog_add.html', context)


def farmer_daily_feedlog_view(request):
    batch_id = request.GET.get('batch_id')
    print('bid',batch_id)
    feed_log = daily_feedinglog.objects.filter(batch_id=batch_id)
    context = {'feed_log':feed_log,'batch_id':batch_id}
    return render(request, './myapp/farmer_daily_feedlog_view.html',context)


def farmer_daily_feedlog_edit(request):
    if request.method == 'POST':
        f_log_id = request.POST.get('f_log_id')
        feed_name = request.POST.get('feed_name')
        feed_quantity = request.POST.get('feed_quantity')
        # time = datetime.datetime.today().strftime('%H:%M:%S')
        # dt = datetime.datetime.today().strftime('%Y-%m-%d')
        # status = 'New'
        df_l = daily_feedinglog.objects.get(id=f_log_id)
        df_l.feed_name=feed_name
        df_l.feed_quantity=feed_quantity
        # df_l.dt=dt
        # df_l.time=time
        df_l.save()
        msg = 'Log Edited'
        context = {'msg':msg,'f_log_id':f_log_id,'df_l':df_l}
        return render(request, './myapp/farmer_daily_feedlog_edit.html', context)
    else:
        f_log_id = request.GET.get('id')
        fl = daily_feedinglog.objects.get(id=f_log_id)
        context = {'f_log_id': f_log_id,'df_l':fl}
        return render(request, './myapp/farmer_daily_feedlog_edit.html', context)


def farmer_general_info_view(request):
    gen_info = general_info.objects.all()
    context = {'gen_info':gen_info}
    return render(request, './myapp/farmer_general_info_view.html', context)



def farmer_doctor_details_view(request):
    d_obj = doctor_details.objects.all()
    context = {'doctor_list':d_obj}
    return render(request, './myapp/farmer_doctor_details_view.html', context)


from . models import doctor_consultation
def farmer_doctor_consultation_add(request):
    if request.method == 'POST':
        farmer_id = request.session['user_id']
        batch_id = request.POST.get('batch_id')
        query = request.POST.get('query')
        dt = datetime.datetime.today().strftime('%Y-%m-%d')
        tm = datetime.datetime.today().strftime('%H:%M:%S')
        prescription = ''
        p_date = ''
        status = 'No Reply'
        dc = doctor_consultation(farmer_id=farmer_id, batch_id=batch_id, query=query,dt=dt , tm=tm, status=status)
        dc.save()
        context={'msg':'Query Added'}
        return render(request, './myapp/farmer_doctor_consultation_add.html', context)
    else:
        batch_id = request.GET.get('batch_id')
        context = {'batch_id':batch_id}
        return render(request, './myapp/farmer_doctor_consultation_add.html',context)

def farmer_doctor_consultation_view(request):
    farmer_id = request.session['user_id']
    con_list = doctor_consultation.objects.filter(farmer_id=farmer_id)
    context={'con_list':con_list}
    return render(request, './myapp/farmer_doctor_consultation_view.html', context)

def farmer_doctor_consultation_delete(request):
    id = request.GET.get('id')
    d = doctor_consultation.objects.get(id=id)
    d.delete()
    msg = 'Query Deleted'
    farmer_id = request.session['user_id']
    con_list = doctor_consultation.objects.filter(farmer_id=farmer_id)
    context={'con_list':con_list, 'msg':msg}
    return render(request, './myapp/farmer_doctor_consultation_view.html', context)


def farmer_medicine_details_view(request):
    med_list = shop_medicine_stock.objects.all()
    context = {'med_list':med_list}
    return render(request, './myapp/farmer_medicine_details_view.html', context)


from . models import farmer_cart
def farmer_medicine_to_cart_add(request):
    medicine_id = request.GET.get('id')
    farmer_id = request.session['user_id']
    med = shop_medicine_stock.objects.get(id=medicine_id)
    if med.stock != 0:
        c_l = farmer_cart.objects.filter(farmer_id=farmer_id,medicine_id=medicine_id)
        if len(c_l) != 0:
            cll = farmer_cart.objects.get(farmer_id=farmer_id, medicine_id=medicine_id)
            cll.quantity=cll.quantity+1
            cll.amount = cll.amount+med.amount
            cll.save()
            med.stock = med.stock-1
            med.save()
            msg = 'Added To Cart'
        else:
            cl = farmer_cart(farmer_id=farmer_id, medicine_id=medicine_id,quantity=1,amount=med.amount)
            cl.save()
            med.stock = med.stock - 1
            med.save()
            msg = 'Added To Cart'

    else:
        msg = 'Sorry No Stock'



    med_list = shop_medicine_stock.objects.all()
    context = {'med_list': med_list,'msg':msg}
    return render(request, './myapp/farmer_medicine_details_view.html', context)


def farmer_medicine_to_cart_view(request):
    farmer_id = request.session['user_id']
    cl = farmer_cart.objects.filter(farmer_id=farmer_id)
    med_l = shop_medicine_stock.objects.all()
    tot_amt = 0
    for amt in cl:
        tot_amt = tot_amt + amt.amount


    context = {'cart_list':cl, 'med_l':med_l,'tot_amt':tot_amt}
    return render(request, './myapp/farmer_medicine_to_cart_view.html', context)


def farmer_remove_medicine_from_cart(request):
    id = request.GET.get('id')
    med = farmer_cart.objects.get(id=id)
    if med.quantity == 1:
        # med.quantity = med.quantity - 1
        sms = shop_medicine_stock.objects.get(id=med.medicine_id)
        # med.amount = med.amount - sms.amount
        sms.stock = sms.stock + 1
        sms.save()
        med.delete()
    elif med.quantity > 1:
        med.quantity = med.quantity - 1
        sms = shop_medicine_stock.objects.get(id=med.medicine_id)
        med.amount = med.amount-sms.amount
        sms.stock = sms.stock + 1
        sms.save()
        med.save()
    else:
        pass



    msg = 'Item Removed'
    farmer_id = request.session['user_id']
    cl = farmer_cart.objects.filter(farmer_id=farmer_id)
    med_l = shop_medicine_stock.objects.all()
    tot_amt = 0
    for amt in cl:
        tot_amt = tot_amt + amt.amount
    context = {'cart_list':cl, 'med_l':med_l,'msg':msg,'tot_amt':tot_amt}
    return render(request, './myapp/farmer_medicine_to_cart_view.html', context)
from datetime import datetime
from . models import shop_farmer_sales,bill_details,bill_transaction
def farmer_medicine_purchase_add(request):
    if request.method == 'POST':
        amt = request.POST.get('tot_amt')
        card_no = request.POST.get('card_no')
        cvv = request.POST.get('cvv')

        dt = datetime.today().strftime('%Y-%m-%d')
        tm = datetime.today().strftime('%H:%M:%S')
        status = 'ok'
        qty = 1
        farmer_id = request.session['user_id']



        bm = shop_farmer_sales(farmer_id=int(farmer_id), bill_no=0, bill_date=dt,
                         total_amount=float(amt), status='Payed')
        bm.save()

        bill_id = shop_farmer_sales.objects.all().aggregate(Max('id'))['id__max']

        pm = bill_transaction(bill_id=bill_id,farmer_id=farmer_id, amount=float(amt),
                            card_no=card_no, cvv=cvv, dt=dt, time=tm, status='ok',remarks='ok')
        pm.save()
        pr_l = farmer_cart.objects.filter(farmer_id=int(farmer_id))
        for pr in pr_l:
            bd = bill_details(bill_id=bill_id, medicine_id=pr.medicine_id, quantity=pr.quantity, amount=pr.amount)
            bd.save()
            sc = farmer_cart.objects.filter(farmer_id=int(farmer_id))
            sc.delete()

                # amt += pm.price


        context = {'msg': 'Payment successfully done'}
        return render(request, 'myapp/farmer_medicine_purchase_add.html', context)

    else:
        farmer_id = request.session['user_id']
        cl = farmer_cart.objects.filter(farmer_id=farmer_id)
        med_l = shop_medicine_stock.objects.all()
        tot_amt = 0
        for amt in cl:
            tot_amt = tot_amt + amt.amount
        context = {'cart_list': cl, 'med_l': med_l, 'tot_amt': tot_amt}
        return render(request, './myapp/farmer_medicine_purchase_add.html',context)


def farmer_transaction_details_view(request):
    farmer_id = request.session['user_id']
    b_l = shop_farmer_sales.objects.filter(farmer_id=farmer_id)
    context = {'b_l':b_l}
    return render(request, './myapp/farmer_transaction_details_view.html',context)


def farmer_transaction_details_view1(request):
    farmer_id = request.session['user_id']
    bill_id = request.GET.get('id')
    b_l = bill_details.objects.filter(bill_id=bill_id)
    med_l = shop_medicine_stock.objects.all()
    context = {'b_l':b_l,'med_l':med_l}
    return render(request, './myapp/farmer_transaction_details_view1.html',context)


def farmer_company_details_view(request):
    cd = company_details.objects.all()
    context = {'company_list':cd}
    return render(request, './myapp/farmer_company_details_view.html',context)


def farmer_manager_details_view(request):
    company_id = request.GET.get('id')
    cd = company_details.objects.get(id=company_id)
    manager_list = manager_details.objects.filter(company_id=cd.user_id)
    context = {'manager_list':manager_list}
    return render(request, './myapp/farmer_manager_details_view.html',context)

from . models import farmer_manager_query
def farmer_manager_query_add(request):
    if request.method =='POST':
        query = request.POST.get('query')
        farmer_id = request.session['user_id']
        manager_id = request.POST.get('manager_id')
        q_dt = datetime.today().strftime('%Y-%m-%d')
        q_time = datetime.today().strftime('%H:%M:%S')
        reply = ''
        r_dt = ''
        r_time = ''
        status = 'No Reply'
        fm_q = farmer_manager_query(query=query, farmer_id=farmer_id, manager_id=manager_id,
                                    q_dt=q_dt, q_time=q_time,status=status)
        fm_q.save()
        context ={'manager_id':manager_id,'msg':'Message Sent..'}
        return render(request, './myapp/farmer_manager_query_add.html', context)
    else:
        manager_id = request.GET.get('id')
        context = {'manager_id':manager_id}
        return render(request, './myapp/farmer_manager_query_add.html',context)


def farmer_manager_query_view(request):
    farmer_id = request.session['user_id']
    fm_q = farmer_manager_query.objects.filter(farmer_id = farmer_id)
    md = manager_details.objects.all()
    cd_l = company_details.objects.all()
    cd = {}
    for c in cd_l:
        for m in md:
            if c.user_id == m.company_id:
                cd[m.user_id]=c.name
    print(cd)
    context = {'message_list':fm_q,'manager_list':md,'cd_l':cd}
    return render(request, './myapp/farmer_manager_query_view.html', context)



from . models import farmer_batch_sales
def farmer_batch_sales_add(request):
    if request.method == 'POST':
        farmer_id = request.session['user_id']
        company_id = request.POST.get('company_id')
        total_count = request.POST.get('total_count')
        total_weight = request.POST.get('total_weight')
        price = request.POST.get('price')
        total_price =float(total_weight)*float(price)
        dt = datetime.today().strftime('%Y-%m-%d')
        time = datetime.today().strftime('%H:%M:%S')
        status = 'Payment-Pending.'
        fb_s = farmer_batch_sales(farmer_id=farmer_id, company_id=company_id, total_count=total_count,total_weight=total_weight,
                                  price=price, total_price=total_price, dt=dt, time=time, status=status)
        fb_s.save()
        context = {'msg':'Sales Details Added..'}
        return render(request, './myapp/farmer_batch_sales_add.html', context)
    else:
        c_list = company_details.objects.all()
        context = {'company_list':c_list}
        return render(request, './myapp/farmer_batch_sales_add.html', context)



def farmer_batch_sales_view(request):
    farmer_id = request.session['user_id']
    fb_s = farmer_batch_sales.objects.filter(farmer_id = farmer_id)
    com_list = company_details.objects.all()
    context = {'fbs_list':fb_s,'company_list':com_list}
    return render(request, './myapp/farmer_batch_sales_view.html', context)



def company_farmer_batch_sales_view(request):
    company_id = request.session['user_id']
    fb_s = farmer_batch_sales.objects.filter(company_id = company_id)
    farmer_list = farmer_details.objects.all()
    context = {'fbs_list':fb_s,'farmer_list':farmer_list}
    return render(request, './myapp/company_farmer_batch_sales_view.html', context)


def company_farmer_payment_add(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        passwd = request.POST.get('passwd')
        company_id = request.session['user_id']
        ul = user_login.objects.get(id=company_id)
        if ul.passwd == passwd:
            fb_s = farmer_batch_sales.objects.get(id=id)
            fb_s.status = 'Payment-Done'
            fb_s.save()
            msg='Payment Success!'
        else:
            msg='Check Password and Try Again!'

        fb_s = farmer_batch_sales.objects.get(id=id)
        total_price = fb_s.total_price
        fr = farmer_details.objects.get(user_id=fb_s.farmer_id)
        farmer_name = f'{fr.f_name} {fr.l_name}'
        farmer_id = fb_s.farmer_id
        context = {'farmer_id': farmer_id, 'farmer_name': farmer_name, 'total_price': total_price, 'id': id,'msg':msg}
        return render(request, './myapp/company_farmer_payment_add.html', context)

    else:
        id = request.GET.get('id')
        fb_s = farmer_batch_sales.objects.get(id=id)
        total_price = fb_s.total_price
        fr = farmer_details.objects.get(user_id=fb_s.farmer_id)
        farmer_name = f'{fr.f_name} {fr.l_name}'
        farmer_id = fb_s.farmer_id
        context = {'farmer_id':farmer_id, 'farmer_name':farmer_name,'total_price':total_price, 'id':id}
        return render(request, './myapp/company_farmer_payment_add.html', context)

#todo:Farmer
############################***--MEDININESHOP--***################################

def medicineshop_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pwd = request.POST.get('pwd')
        #print(un,pwd)
        #query to select a record based on a condition
        ul = user_login.objects.filter(uname=un, passwd=pwd, u_type='medshop')

        if len(ul) == 1:
            request.session['user_name'] = ul[0].uname
            request.session['user_id'] = ul[0].id
            return render(request,'./myapp/medicineshop_home.html')
        else:
            msg = '<h1> Invalid Uname or Password !!!</h1>'
            context ={ 'msg1':msg }
            return render(request, './myapp/medicineshop_login.html',context)
    else:
        msg = ''
        context ={ 'msg1':msg }
        return render(request, './myapp/medicineshop_login.html',context)


def medicineshop_home(request):
    try:
        uname = request.session['user_name']
        print(uname)
    except:
        return medicineshop_login(request)
    else:
        return render(request,'./myapp/medicineshop_home.html')


def medicineshop_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/medicineshop_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/medicineshop_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/medicineshop_changepassword.html', context)
    else:
        return render(request, './myapp/medicineshop_changepassword.html')


def medicineshop_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return medicineshop_login(request)
    else:
        return medicineshop_login(request)


def medicineshop_medicine_add(request):
    if request.method == 'POST':

        name = request.POST.get('mname')
        cname = request.POST.get('cname')
        bcode = request.POST.get('bcode')
        mdes = request.POST.get('mdes')
        stock = request.POST.get('stock')
        amount = request.POST.get('amt')


        #status = "new"

        ud = shop_medicine_stock(medicine_name=name, medicine_company=cname,batch_code =bcode, medicine_description=mdes, stock=stock,amount=amount )
        ud.save()

        #print(user_id)
        context = {'msg': 'medicine added'}
        return render(request, 'myapp/medicineshop_medicine_add.html',context)

    else:
        return render(request, 'myapp/medicineshop_medicine_add.html')


def medicineshop_medicine_edit(request):
    if request.method == 'POST':
        id = request.POST.get('med_id')
        name = request.POST.get('mname')
        cname = request.POST.get('cname')
        bcode = request.POST.get('bcode')
        mdes = request.POST.get('mdes')
        stock = request.POST.get('stock')
        amt = request.POST.get('amt')

        m_obj = shop_medicine_stock.objects.get(id=int(id))
        m_obj.medicine_name = name
        m_obj.medicine_company= cname
        m_obj.batch_code = bcode
        m_obj.medicine_description=mdes
        m_obj.stock = stock
        m_obj.amount = amt
        m_obj.save()
        msg = 'Medicine Record Updated'
        context = {'msg': msg,'m_obj': m_obj, 'med_id': m_obj.id}
        return render(request, 'myapp/medicineshop_medicine_edit.html', context)
    else:
        id = request.GET.get('id')
        m_obj = shop_medicine_stock.objects.get(id=int(id))
        context = {'m_obj': m_obj, 'med_id': m_obj.id}
        return render(request, './myapp/medicineshop_medicine_edit.html', context)


def medicineshop_medicine_view(request):
    medicine_list = shop_medicine_stock.objects.all()
    context = {'medicine_list': medicine_list, 'msg': ''}
    return render(request, 'myapp/medicineshop_medicine_view.html', context)


def medicineshop_medicine_delete(request):
    # id = request.GET.get('id')
    # print('id = '+id)
    cg = shop_medicine_stock.objects.get(id=int(id))
    cg.delete()
    msg = "medicine deleted"

    medicine_list=shop_medicine_stock.objects.all()
    context = {'medicine list': medicine_list,'msg':msg}
    return render(request,'./myapp/medicineshop_medicine_view.html',context)


def medicineshop_transaction_details_view(request):
    farmer_id = request.session['user_id']
    b_l = shop_farmer_sales.objects.all()
    u_l = farmer_details.objects.all()
    context = {'b_l':b_l,'u_l':u_l}
    return render(request, './myapp/medicineshop_transaction_details_view.html',context)


def medicineshop_transaction_details_view1(request):
    farmer_id = request.session['user_id']
    bill_id = request.GET.get('id')
    b_l = bill_details.objects.filter(bill_id=bill_id)
    med_l = shop_medicine_stock.objects.all()
    context = {'b_l':b_l,'med_l':med_l}
    return render(request, './myapp/medicineshop_transaction_details_view1.html',context)
#####################################***--USER--***##########################################

# from .models import user_details

def user_login_check(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')

        ul = user_login.objects.filter(uname=uname, passwd=passwd, u_type='user')
        print(len(ul))
        if len(ul) == 1:
            request.session['user_id'] = ul[0].id
            request.session['user_name'] = ul[0].uname
            context = {'uname': request.session['user_name']}
            #send_mail('Login','welcome'+uname,uname)
            return render(request, 'myapp/user_home.html',context)
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request, 'myapp/user_login.html',context)
    else:
        return render(request, 'myapp/user_login.html')


def user_home(request):
    context = {'uname':request.session['user_name']}
    return render(request,'./myapp/user_home.html',context)
    #send_mail("heoo", "hai", 'snehadavisk@gmail.com')

    1

from . models import user_details
def user_details_add(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        addr = request.POST.get('addr')
        pin = request.POST.get('pin')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('pwd')
        uname=email
        #status = "new"

        ul = user_login(uname=uname, passwd=password, u_type='user')
        ul.save()

        user_id = user_login.objects.all().aggregate(Max('id'))['id__max']

        ud = user_details(user_id=user_id,fname=fname, lname=lname, gender=gender, age=age,address=addr, pin=pin, contact=contact, email=email )
        ud.save()

        print(user_id)
        context = {'msg': 'User Registered'}
        return render(request, 'myapp/user_login.html',context)

    else:
        return render(request, 'myapp/user_details_add.html')


def user_changepassword(request):
    if request.method == 'POST':
        uname = request.session['user_name']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print("username:::" + uname)
        print("current_password" + str(current_password))

        try:

            ul = user_login.objects.get(uname=uname, passwd=current_password)

            if ul is not None:
                ul.passwd = new_password  # change field
                ul.save()
                context = {'msg':'Password Changed Successfully'}
                return render(request, './myapp/user_changepassword.html',context)
            else:
                context = {'msg': 'Password Not Changed'}
                return render(request, './myapp/user_changepassword.html', context)
        except user_login.DoesNotExist:
            context = {'msg': 'Password Not Changed'}
            return render(request, './myapp/user_changepassword.html', context)
    else:
        return render(request, './myapp/user_changepassword.html')



def user_logout(request):
    try:
        del request.session['user_name']
        del request.session['user_id']
    except:
        return user_login_check(request)
    else:
        return user_login_check(request)


