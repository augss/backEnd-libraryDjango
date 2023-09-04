from rest_framework.serializers import ModelSerializer, CharField

from library.serializers import ShoppingItemSerializer

from library.models import Shopping

class ShoppingSerializer(ModelSerializer):
    class Meta:
        model = Shopping
        fields = "__all__"

    user = CharField(source="user.email", read_only=True)
    status = CharField(source="get_status_display", read_only=True)
    items = ShoppingItemSerializer(many=True, read_only=True)

