from rest_framework.serializers import ModelSerializer

from library.models import Author, Book, Category, Publisher

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BookDetailSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        depth = 1

class BookListSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "price"]
