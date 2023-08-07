from rest_framework.serializers import ModelSerializer

from library.models import Author, Book, Category, Publisher

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'