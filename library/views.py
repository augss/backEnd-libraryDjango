from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from library.models import Author, Book, Category, Publisher
from library.serializers import AuthorSerializer, BookSerializer, CategorySerializer, PublisherSerializer

class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class PublisherViewSet(ModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
