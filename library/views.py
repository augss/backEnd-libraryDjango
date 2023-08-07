from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet

from library.models import Author, Book, Category, Publisher
from library.serializers import AuthorSerializer, BookSerializer, BookDetailSerializer, BookListSerializer, CategorySerializer, PublisherSerializer

class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsAuthenticated]


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return BookListSerializer
        elif self.action == "retrieve":
            return BookDetailSerializer
        return BookSerializer
    
    permission_classes = [IsAuthenticated]



class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

class PublisherViewSet(ModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    permission_classes = [IsAuthenticated]

