from django.contrib import admin
from .models import User,Livestock,DepStock,FarmStock,LiveFarmStock
# Register your models here.
admin.site.register([User,Livestock,DepStock,FarmStock,LiveFarmStock])