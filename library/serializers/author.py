from rest_framework.serializers import ModelSerializer

from library.models import Author, Book, Category, Publisher

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'