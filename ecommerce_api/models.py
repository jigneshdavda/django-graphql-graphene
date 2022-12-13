from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shop(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255)
    email_id = models.CharField(max_length = 255)
    contact_number = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = False, blank = True)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updated_at = models.DateTimeField(auto_now = True, blank = True) 

    def __str__(self):
        return self.name
    
class Products(models.Model):
    shop = models.ForeignKey(Shop, on_delete = models.CASCADE, blank = True, null = True)
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    price = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = False, blank = True)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updated_at = models.DateTimeField(auto_now = True, blank = True) 

    def __str__(self):
        return self.name