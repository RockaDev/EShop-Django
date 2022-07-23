
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test
from shop.models import Order,OrderItem,Customer,ShopItems
from checkout.models import ShippingAddress


@user_passes_test(lambda u: u.is_superuser,login_url=('/error404/'))
def placed_order(request):
    
    if 'device' in request.COOKIES.keys():
        device = request.COOKIES['device']
    else:
        return redirect('/loading/')
    
    _order_list = OrderItem.objects.all()
    _order_id = Order.objects.filter(complete=True)
    _orders = ShippingAddress.objects.all().order_by('id')
    customer = Customer.objects.get(device=device)

    
    _data = {'shipping':_orders,'list':_order_list,'orderid':_order_id}

    return render(request,'orders/placed_orders.html',_data)


def no_permissions(request):
    _data = {}
    return render(request,'orders/permission_not_granted.html',_data)

@user_passes_test(lambda u: u.is_superuser,login_url=('/error404/'))
def orderdetail(request,pk):
    order = OrderItem.objects.filter(order = pk)
    shipping = ShippingAddress.objects.filter(order_id=pk)
    product = ShopItems.objects.filter(pk = pk)
    order_model = Order.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST.get('save_checkbox_db'):
            checklist = request.POST.get('mark_as_completed','') == 'on'


            checkmark = ShippingAddress.objects.get(order_id=pk)
            checkmark.mark_as_completed = checklist
            checkmark.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])

        elif request.POST.get('delete_order'):
            del_order = shipping.delete()
            return HttpResponseRedirect('/orders/')


    _data = {'order':order,'shipping':shipping,'products':product,'order_model':order_model}

    return render(request,'orders/orderdetail.html',_data)