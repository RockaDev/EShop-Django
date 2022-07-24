from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from checkout.forms import CheckoutForm
from shop.models import Order,OrderItem,Customer,ShopItems
from checkout.models import ShippingAddress
import random,string
# Create your views here.

def create_unique_id():
    return ''.join(random.choices(string.digits, k=8))

def checkout(request):
    
    """
        Get generated device UUID.
    """

    if 'device' in request.COOKIES.keys():
        device = request.COOKIES['device']
    else:
        return HttpResponseRedirect('/loading/')

    customer = Customer.objects.get(device=device)
    order,created = Order.objects.get_or_create(customer=customer,complete=False)

    
    if request.method == 'POST':
        order = Order.objects.filter(customer=customer)


        form = CheckoutForm(request.POST)
        products = OrderItem.objects.all()
        shop_products = ShopItems.objects.all()
        order_id = Order.objects.all()

        if request.POST.get('payment'):
            if form.is_valid():

                transaction_gen_id = create_unique_id()

                unique_id = Order.objects.filter(transaction_id = transaction_gen_id).exists()

                for pk in order_id:
                    oid = Order.objects.get(customer=customer,complete=False)


                instance = form.save(commit=False)
                instance.order_id = oid

                instance.save()


                
                """
                    Generate unique transaction id if payment is completed
                """

                if unique_id:
                    transaction_gen_id = create_unique_id()
                    for id in order_id:
                        Order.objects.filter(id=id.id,customer=customer,complete=False).update(transaction_id=transaction_gen_id)
                        ShippingAddress.objects.filter(order_id=oid).update(transaction_id=transaction_gen_id)
                    for id in order:
                        OrderItem.objects.filter(order=oid).update(transaction_id=transaction_gen_id)
                else:
                    transaction_gen_id = create_unique_id()
                    for id in order_id:
                        Order.objects.filter(id=id.id,customer=customer,complete=False).update(transaction_id=transaction_gen_id)
                        ShippingAddress.objects.filter(order_id=oid).update(transaction_id=transaction_gen_id)
                    for id in order:
                        OrderItem.objects.filter(order=oid).update(transaction_id=transaction_gen_id)

                completed_order = Order.objects.filter(customer=customer).update(complete=True)

                return HttpResponseRedirect(request.META['HTTP_REFERER'])


    else:
        form = CheckoutForm()

    _data = {'form':form,'order':order}
    return render(request,'checkout/checkout.html',_data)

