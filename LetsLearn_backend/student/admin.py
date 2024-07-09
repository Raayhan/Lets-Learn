from django.contrib import admin

from .models import Information

class StudentInformation(admin.ModelAdmin):
  list_display = ("user","phone", "gender","division","district")
admin.site.register(Information,StudentInformation)
