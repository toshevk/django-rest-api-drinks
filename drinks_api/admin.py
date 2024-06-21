from django.contrib import admin
from .models import Drink


class DrinkAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price")
    search_fields = ("name", "description")


admin.site.register(Drink, DrinkAdmin)
