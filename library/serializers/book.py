from rest_framework.serializers import ModelSerializer

from rest_framework.serializers import ModelSerializer, SlugRelatedField

from uploader.models import Image
from uploader.serializers import ImageSerializer


from library.models import Author, Book, Category, Publisher

class BookSerializer(ModelSerializer):
    cover_attachment_key = SlugRelatedField(
        source="cover",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    cover = ImageSerializer(required=False, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

class BookDetailSerializer(ModelSerializer):
    cover = ImageSerializer(required=False)

    class Meta:
        model = Book
        fields = "__all__"
        depth = 1

class BookListSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "price"]
