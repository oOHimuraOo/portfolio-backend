from rest_framework import serializers
from portfolio.models import SubProjetoModel

class SubProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubProjetoModel
        fields = "__all__"
