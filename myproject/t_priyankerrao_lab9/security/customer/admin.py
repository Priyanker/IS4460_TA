from .models import Customer
from django.contrib import admin

class CustomerAdmin(admin.ModelAdmin):
    pass  # Empty admin class for now

admin.site.register(Customer, CustomerAdmin)
