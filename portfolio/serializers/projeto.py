from rest_framework import serializers
from portfolio.models import ProjetoModel
from portfolio.serializers.subprojeto import SubProjetoSerializer

class ProjetoSerializer(serializers.ModelSerializer):
    subprojetos = SubProjetoSerializer(many=True, read_only=True)  # Subprojetos aninhados

    class Meta:
        model = ProjetoModel
        fields = "__all__"
