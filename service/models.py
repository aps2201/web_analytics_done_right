from django.db import models
from django.contrib.auth import get_user_model

import uuid
# Create your models here.

class cart(models.Model):
    cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    items = models.ManyToManyField('service.product')
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    
    def __str__(self):
        return "{0} {1}".format(self.user.username,self.cart_id)
    
class product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 255)
    price = models.IntegerField()
    desc = models.TextField()

class orderItem(models.Model):
    product = models.OneToOneField('service.product', on_delete=models.SET_NULL,null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now = True)
    date_ordered = models.DateTimeField(null=True)
    
class order(models.Model):
    STATUS_ORDER = ((0,"received"),
                    (1,"processing"),
                    (2,"processed"),
                    (3,"completed"))
    STATUS_APPRV = ((0,"undecided"),
                    (1,"approved"),
                    (2,"rejected"))
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_status = models.CharField(max_length = 255,choices=STATUS_ORDER)
    order_approval = models.CharField(max_length = 255,choices=STATUS_APPRV)
    cart = models.ForeignKey('service.cart',null=True,on_delete=models.SET_NULL)
    items =  models.ManyToManyField('service.orderItem')
    date_ordered = models.DateTimeField(auto_now=True)
    ref_code = models.CharField(max_length=15)
    
    def get_cart_items(self):
        return self.items.all()
    def get_cart_total(self):
        return sum([item.product.product_price for item in self.items.all()])
    def __str__(self):
        return "{0},{1}".format(self.order_id)
    

