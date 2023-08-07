from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ModelViewSet

from library.models import Author, Book, Category, Publisher
from library.serializers import AuthorSerializer, BookSerializer, BookDetailSerializer, BookListSerializer, CategorySerializer, PublisherSerializer


class PublisherViewSet(ModelViewSet):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
    permission_classes = [IsAuthenticated]