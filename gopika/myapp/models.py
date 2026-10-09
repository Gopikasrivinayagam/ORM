

from django.db import models
from django.contrib import admin
class Items(models.Model):
    product_name=models.CharField(max_length=15)
    Name=models.CharField(max_length=10)
    Address=models.TextField()
    Mobile_No=models.IntegerField(primary_key=True)
    price=models.IntegerField()
    Dt=models.TimeField()
    DoD=models.DateField()
class ItemsAdmin(admin.ModelAdmin):

    list_display=["product_name","Name","Address","Mobile_No","price","Dt","DoD"]





