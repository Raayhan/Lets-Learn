from rest_framework.permissions import AllowAny
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Category
from .serializers import CategorySerializer


class LatestCategoriesList(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        categories = Category.objects.all()[0:16]
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)