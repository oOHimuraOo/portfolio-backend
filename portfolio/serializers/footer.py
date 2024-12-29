from rest_framework import serializers
from portfolio.models import FooterModel


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterModel
        fields = "__all__"
