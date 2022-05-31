from django.contrib import admin
from .models import Contact

# Register your models here.
from shop.models import Cart, Cook, Dish
admin.site.register(Dish)
admin.site.register(Cook)
admin.site.register(Cart)
admin.site.register(Contact)
