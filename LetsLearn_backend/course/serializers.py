from rest_framework import serializers

from .models import Category,Course
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class CourseSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()
    author   = UserSerializer(read_only=True)
    class Meta:
        model = Course
        fields = (
            "id",
            "title",
            "summary",
            "category",
            "author",
            "description",
            "get_absolute_url",
            "date_added",
           
            
        )
    def get_category(self, obj):
        return obj.category.name

class CategorySerializer(serializers.ModelSerializer):

    courses = CourseSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_image",
            "get_absolute_url",
            "courses"
        )