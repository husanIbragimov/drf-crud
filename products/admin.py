from django.contrib import admin
from .models import Product


class ProductAmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    filter_vertical = ('title', )


admin.site.register(Product)
