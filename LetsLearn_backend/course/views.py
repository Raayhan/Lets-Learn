from rest_framework.permissions import AllowAny, IsAuthenticated
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category,Course
from .serializers import CategorySerializer
from .serializers import CourseBoxSerializer
from .serializers import CourseDetailsSerializer
from .serializers import EnrollmentSerializer


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

class GetEnrollment(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, category_slug, course_slug):
        try:
            course = Course.objects.get(slug=course_slug, category__slug=category_slug)
        except Course.DoesNotExist:
            
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        
        if not request.user.is_authenticated:
           
            return Response({"error": "User not authenticated"}, status=status.HTTP_401_UNAUTHORIZED)
        
        data = request.data.copy()
        data['student_id'] = request.user.id
        data['course_id'] = course.id
        data['completion_status'] = False

        serializer = EnrollmentSerializer(data=data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)