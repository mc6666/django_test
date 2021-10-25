from django.db import models
from django.utils import timezone
import datetime

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=20, blank=True, null=True)
    updated_by = models.CharField(max_length=20, blank=True, null=True)
    
    class Meta:
        abstract = True

class Customer(BaseModel):
    customer_id = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)

class Order(BaseModel):
    order_id = models.CharField(max_length=20)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.CharField(max_length=8)
    required_date = models.CharField(max_length=8)

class Product(BaseModel):
    product_id = models.CharField(max_length=20)
    product_name = models.CharField(max_length=60, blank=True, null=True)

class Order_Detail(BaseModel):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.IntegerField()
    quantity = models.IntegerField()
    discount = models.DecimalField(max_digits=3, decimal_places=2)


    
