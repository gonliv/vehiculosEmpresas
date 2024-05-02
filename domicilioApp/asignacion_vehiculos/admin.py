from django.contrib import admin
from .models import Driver, Vehicle, AccountingRegistry

# Register your models here.
admin.site.register(Driver)
admin.site.register(Vehicle)
admin.site.register(AccountingRegistry)
