from rest_framework.serializers import ModelSerializer

from library.models import Author, Book, Category, Publisher

class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'