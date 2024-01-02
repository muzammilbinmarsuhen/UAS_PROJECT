from django.db import models
from datetime import datetime,date
# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    email=models.EmailField()
    date_create=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
    
class Tags(models.Model):
    name=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.name
    
class Produk(models.Model):
    KATEGORI=(
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door'),
    )

    name=models.CharField(max_length=50,null=True)
    price=models.FloatField()
    kategori=models.CharField(max_length=50,null=True,choices=KATEGORI)
    deskripsi=models.CharField(max_length=200,null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    tags=models.ManyToManyField(Tags)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS=(
        ('Pending','Pending' ),
        ('Our for delivery','Our for delivery' ),
        ('Delivered','Delivered' ),
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    produk=models.ForeignKey(Produk,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)

