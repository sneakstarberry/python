from django.contrib import admin
from .models import Item, ItemCategory
# Register your models here.
admin.site.register([Item, ItemCategory])