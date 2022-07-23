from django.db import models
# Create your models here.

class ShippingAddress(models.Model):
    address = models.CharField(max_length=9999,verbose_name="Adresa",unique=False)
    post_num = models.CharField(max_length=100,verbose_name="PSC",unique=False)
    country = models.CharField(max_length=9999,verbose_name="Krajina",unique=False)
    name = models.CharField(max_length=9999,verbose_name="Meno",unique=False)
    surname = models.CharField(max_length=9999,verbose_name="Priezvisko",unique=False)
    tel_number = models.IntegerField(verbose_name="Telefonne cislo",unique=False)
    dic = models.CharField(max_length=9999,verbose_name="DIC",unique=False)
    email = models.CharField(max_length=9999,verbose_name="Email",unique=False)
    date_of_order = models.DateTimeField(auto_now_add=True)

    mark_as_completed = models.BooleanField(default=False)

    order_id = models.CharField(max_length=9999,unique=False,null=True)
    transaction_id = models.CharField(max_length=9999,unique=False,null=True)

    def __str__(self):
        return (f"{self.country} | {self.name} {self.surname} | {self.email}")
