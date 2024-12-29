from rest_framework import serializers
from portfolio.models import PerfilModel


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilModel
        fields = "__all__"  # Inclui todos os campos do modelo
