from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model
from checkout.models import ShippingAddress
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

User=get_user_model()


class ShopItems(models.Model):
    product_item = models.CharField(max_length=200,verbose_name="product name",unique=False)
    product_item_ascii = models.CharField(max_length=200,verbose_name="only ascii",unique=False,default='none')
    price = models.IntegerField(verbose_name="item price",unique=False)
    about_item = models.CharField(max_length=9999,verbose_name="popis",unique=False)
    image = models.ImageField(upload_to='products/',null=True,blank=True)
    on_stock = models.IntegerField(default=0,verbose_name="on stock",unique=False)
    created_date = models.DateTimeField('date created',auto_now_add=True)

    class Meta:
        ordering = ["product_item","price","about_item","on_stock"]

    objects = models.Manager()

    def __str__(self):
        return self.product_item

    def get_fields(self):
        return [(field.name, getattr(self,field.name)) for field in ShopItems._meta.fields]


class Customer(models.Model):
    device = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.device:
            name = self.device
        else:
            name = self.device
        return str(name)
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)
        
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total 

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total 

class OrderItem(models.Model):
    product = models.ForeignKey(ShopItems, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=999,default="Caka sa na platbu",unique=False)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return (f"produkt: {self.product} || pocet: {self.quantity} || id: {self.order} || transakcia: {self.transaction_id}")

