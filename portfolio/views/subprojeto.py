from rest_framework import generics
from portfolio.models import SubProjetoModel
from portfolio.serializers.subprojeto import SubProjetoSerializer


class SubProjetoListView(generics.ListCreateAPIView):
    queryset = SubProjetoModel.objects.all()
    serializer_class = SubProjetoSerializer


class SubProjetoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubProjetoModel.objects.all()
    serializer_class = SubProjetoSerializer
