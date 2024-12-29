from rest_framework import generics
from portfolio.models import TecnologiaModel
from portfolio.serializers.tecnologia import TecnologiaSerializer


class TecnologiaListView(generics.ListCreateAPIView):
    queryset = TecnologiaModel.objects.all()
    serializer_class = TecnologiaSerializer
