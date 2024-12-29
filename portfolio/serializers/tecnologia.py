from rest_framework import serializers
from portfolio.models import TecnologiaModel


class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TecnologiaModel
        fields = "__all__"
