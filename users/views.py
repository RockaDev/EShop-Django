from django.shortcuts import render,redirect
from users.forms import AdminForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import get_user_model,authenticate
from django.contrib import auth
from shop.models import Customer,Order,ShopItems
from django.http import HttpResponseRedirect
import random,uuid
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

User = get_user_model()

def home(request):
    print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])

    if 'device' in request.COOKIES.keys():
        device = request.COOKIES['device']
    else:
        return HttpResponseRedirect('/loading/')

    customer,created = Customer.objects.get_or_create(device=device)
    order,created = Order.objects.get_or_create(customer=customer,complete=False)

    queryset = ShopItems.objects.filter(product_item="non_existent_name")
    upper_content_random = list(ShopItems.objects.all())
    count_shopitems = ShopItems.objects.count()


    try:
        random_items = random.sample(upper_content_random, 2)

    except: 
        random_items = random.sample(upper_content_random, 0)

    data = {'random_shopitem':random_items,'order':order}
    return render(request,'base/home.html',data)

def adminlogin(request):
    if request.method == 'POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        usr = authenticate(request,email=email,password=password)
        adminForm = AdminForm(request.POST)
        if usr is not None:
            auth_login(request,usr)
            return HttpResponseRedirect('/')

    else:
        adminForm = AdminForm()
            
    data = {'adminForm':adminForm}
    return render(request,'admin/admin_login.html',data)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')



def loading_data(request):
    _data = {}
    return render(request,'base/loading.html',_data)
