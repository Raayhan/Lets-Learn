from rest_framework.permissions import AllowAny
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category,Course
from .serializers import CategorySerializer
from .serializers import CourseSerializer


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
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)