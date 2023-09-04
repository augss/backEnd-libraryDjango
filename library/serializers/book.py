from rest_framework.serializers import ModelSerializer, SlugRelatedField

from library.models import Book

from uploader.models import Image
from uploader.serializers import ImageSerializer

class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    cover_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    cover = ImageSerializer(required=False, read_only=True)


class BookDetailSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        depth = 1
    cover = ImageSerializer(required=False)


class BookListSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "price"]
