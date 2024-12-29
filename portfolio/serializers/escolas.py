from rest_framework import serializers
from portfolio.models import EscolasModel


class EscolasSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscolasModel
        fields = "__all__"
