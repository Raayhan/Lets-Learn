from rest_framework.permissions import AllowAny
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category,Course
from .serializers import CategorySerializer
from .serializers import CourseBoxSerializer
from .serializers import CourseDetailsSerializer


class LatestCategoriesList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        categories = Category.objects.all()[0:16]
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CategoryDetail(APIView):
    permission_classes = [AllowAny]

    def get_object(self,category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class CourseList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        courses = Course.objects.all()[0:16]
        serializer = CourseBoxSerializer(courses, many=True)
        return Response(serializer.data)

class CourseDetail(APIView):
    permission_classes = [AllowAny]

    def get_object(self,category_slug,course_slug):
        try:
            return Course.objects.filter(category__slug=category_slug).get(slug=course_slug)
        except Course.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, course_slug, format=None):
        course = self.get_object(category_slug, course_slug)
        serializer = CourseDetailsSerializer(course)
        return Response(serializer.data)