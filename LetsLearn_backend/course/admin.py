from django.contrib import admin
from .models import Category,Course
from ckeditor.widgets import CKEditorWidget
from django import forms


class CategoryList(admin.ModelAdmin):
    list_display = ("name","slug")


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Course
        fields = '__all__'

class CourseAdmin(admin.ModelAdmin):
    form = CourseForm
    

class CourseList(admin.ModelAdmin):
    list_display = ("title","category","author","slug","date_added")

admin.site.register(Category,CategoryList)
admin.site.register(Course,CourseList)