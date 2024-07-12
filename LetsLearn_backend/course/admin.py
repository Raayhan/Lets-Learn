from django.contrib import admin
from .models import Category


class CategoryList(admin.ModelAdmin):
    list_display = ("name","slug")

admin.site.register(Category,CategoryList)