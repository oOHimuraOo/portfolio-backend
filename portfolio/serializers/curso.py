from rest_framework import serializers
from portfolio.models import CursoModel


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoModel
        fields = "__all__"
