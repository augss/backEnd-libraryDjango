from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from library.serializers import ShoppingItemSerializer
from library.models import Shopping

class ShoppingSerializer(ModelSerializer):
    user = CharField(source="user.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    items = ShoppingItemSerializer(many=True, read_only=True)
    total = SerializerMethodField()

    class Meta:
        model = Shopping
        fields = ("id", "user", "status", "total", "items")

    def get_total(self, obj):
        return sum(item.book.price * item.amount for item in obj.items.all())
