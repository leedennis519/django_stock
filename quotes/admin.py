from django.contrib import admin
#import the stock class
from .models import Stock

# Register your models here.
admin.site.register(Stock)