from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from library.models import Shopping, ShoppingItem

class ShoppingItemSerializer(ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = ["book", "amount", "total"]
        depth = 2

    total = SerializerMethodField()

    def get_total(self, instance):
        return instance.amount * instance.book.price