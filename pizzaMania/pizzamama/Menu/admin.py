from django.contrib import admin
from .models import Pizza


# Register your models here.

class PizzaAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'price', 'ingredient', 'vegetarienne')
   

admin.site.register(Pizza, PizzaAdmin)
