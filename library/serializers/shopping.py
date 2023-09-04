from rest_framework.serializers import ModelSerializer, CharField

from library.models import Shopping

class ShoppingSerializer(ModelSerializer):
    class Meta:
        model = Shopping
        fields = "__all__"