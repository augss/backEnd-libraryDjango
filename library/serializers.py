from rest_framework.serializers import ModelSerializer

from library.models import Author, Book, Category, Publisher

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'