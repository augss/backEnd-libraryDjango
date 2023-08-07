from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import User


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
