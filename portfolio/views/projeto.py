from rest_framework import generics
from portfolio.models import ProjetoModel
from portfolio.serializers.projeto import ProjetoSerializer


class ProjetoListView(generics.ListCreateAPIView):
    queryset = ProjetoModel.objects.all()
    serializer_class = ProjetoSerializer


class ProjetoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProjetoModel.objects.all()
    serializer_class = ProjetoSerializer
