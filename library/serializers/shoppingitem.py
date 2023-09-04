from rest_framework.serializers import ModelSerializer, CharField

from library.models import Shopping, ShoppingItem

class ShoppingItemSerializer(ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = "__all__"