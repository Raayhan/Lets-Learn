from django.contrib import admin
from .models import Category,Course,Enrollment
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms


class CategoryList(admin.ModelAdmin):
    list_display = ("name","slug")


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditor5Widget())

    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
              "text": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="comment"
              )
          }

class CourseAdmin(admin.ModelAdmin):
    form = CourseForm
    

class CourseList(admin.ModelAdmin):
    list_display = ("title","category","author","slug","date_added")

class EnrollmentList(admin.ModelAdmin):
    list_display = ("course","student","completion_status","enrollment_date")

admin.site.register(Category,CategoryList)
admin.site.register(Course,CourseList)
admin.site.register(Enrollment,EnrollmentList)