from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import uuid
from django.core.exceptions import ValidationError
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self,email,uuid_id,password=None):
        if not email:
            raise ValueError("Email is required")

        user=self.model(
            email=self.normalize_email(email),
            uuid_id=uuid_id,
            password=password
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,uuid_id,password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            uuid_id=uuid_id,
            password=password
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class ThisUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address",max_length=120,unique=True,null=True)
    uuid_id = models.CharField(max_length=200,default=uuid.uuid4,editable=True,unique=True,null=True)

    
    date_joined = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login",auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["uuid_id"]

    objects=MyUserManager()

    def __str__(self):
        return (f"{self.email}")

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True


