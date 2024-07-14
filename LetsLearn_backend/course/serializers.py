from rest_framework import serializers

from .models import Category

class CategorySerializer(serializers.ModelSerializer):

   #jobs = JobSerializer(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_image",
            "get_absolute_url",
        )
