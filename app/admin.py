from django.contrib import admin
from .models import Menu, CustomerRegisteration,Hotels

# Register your models here.
admin.site.register(Hotels)
admin.site.register(Menu)
admin.site.register(CustomerRegisteration) 