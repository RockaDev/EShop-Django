from .models import ShopItems,Order,OrderItem,Customer
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect

class Process:

    """
        return 0 -> FAIL
        return 1 -> SUCCESS
    """
    
    def add_to_cart_function(request):
        for product in ShopItems.objects.all():
            if request.POST.get(f"add-to-cart-{product.id}"):
                ItemQuantity = request.POST.get('quantity')
                if not ItemQuantity or int(ItemQuantity) < 1:
                    return 0
                elif int(ItemQuantity) > int(product.on_stock):
                    return 0
                else:
                    product = ShopItems.objects.get(pk = product.id)
                    device = request.COOKIES['device']
                    customer,created = Customer.objects.get_or_create(device=device)

                    order, created = Order.objects.get_or_create(customer=customer, complete=False)
                    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
                    orderItem.quantity=request.POST['quantity']
                    orderItem.save()
                    return 1


    def edit_quantity_and_remove_items_function(request):
        device = request.COOKIES['device']
        customer,created = Customer.objects.get_or_create(device=device)

        order,created = Order.objects.get_or_create(customer=customer,complete=False)

        for product in ShopItems.objects.all():
            if request.POST.get(f'remove-{product.id}'):
                removeOrderItem = OrderItem.objects.filter(order=order, product=product.id)
                removeOrderItem.delete()

                return 1

        
            if request.POST.get(f'apply-add-{product.id}'):
                editedQuantity = request.POST.get(f'edit-quantity-{product.id}')
                updateQuantity = OrderItem.objects.get(order=order, product=product.id)
                if not editedQuantity or int(editedQuantity) < 1:
                    return 0
                elif int(editedQuantity) > int(product.on_stock):
                    return 0
                else:
                    updateQuantity.quantity = int(editedQuantity)
                    updateQuantity.save()
                    return 1


