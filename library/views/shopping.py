from rest_framework.viewsets import ModelViewSet

from library.models import Shopping
from library.serializers import ShoppingSerializer


class ShoppingViewSet(ModelViewSet):
    queryset = Shopping.objects.all()
    serializer_class = ShoppingSerializer