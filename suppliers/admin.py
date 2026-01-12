from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Supplier, Invoice, PQRDocument

admin.site.register(Supplier)
admin.site.register(Invoice)

from .models import DailyRevenue, Expense

admin.site.register(DailyRevenue)
admin.site.register(Expense)

