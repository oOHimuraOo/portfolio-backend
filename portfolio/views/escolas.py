from rest_framework import generics
from portfolio.models import EscolasModel
from portfolio.serializers.escolas import EscolasSerializer


class EscolasListView(generics.ListCreateAPIView):
    queryset = EscolasModel.objects.all()
    serializer_class = EscolasSerializer
