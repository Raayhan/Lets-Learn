from rest_framework import serializers

from .models import Category,Course,Enrollment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']

class CourseBoxSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()
    author   = UserSerializer(read_only=True)
    class Meta:
        model = Course
        fields = (
            "title",
            "category",
            "get_image",
            "author",
            "get_absolute_url",          
            
        )
    def get_category(self, obj):
        return obj.category.name

class CourseDetailsSerializer(serializers.ModelSerializer):

    category = serializers.SerializerMethodField()
    author   = UserSerializer(read_only=True)
    class Meta:
        model = Course
        fields = (
            "title",
            "summary",
            "category",
            "get_image",
            "author",
            "description",
            "date_added" 
        )
    def get_category(self, obj):
        return obj.category.name


class CategorySerializer(serializers.ModelSerializer):

    courses = CourseBoxSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "name",
            "get_image",
            "get_absolute_url",
            "courses"
        )

class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseBoxSerializer(read_only=True)
    student = UserSerializer(read_only=True)
    student_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='student', write_only=True)
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), source='course', write_only=True)

    class Meta:
        model = Enrollment
        fields = (
            "course",
            "course_id",
            "student",
            "student_id",
            "enrollment_date",
            "completion_status"
        )

    def validate(self, data):
        student = data['student']
        course = data['course']
        
        # Check if the enrollment already exists
        if Enrollment.objects.filter(student=student, course=course).exists():
            raise serializers.ValidationError("You are already enrolled in this course.")
        
        return data