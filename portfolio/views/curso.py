from rest_framework import generics
from portfolio.models import CursoModel
from portfolio.serializers.curso import CursoSerializer


class CursoListView(generics.ListCreateAPIView):
    queryset = CursoModel.objects.all()
    serializer_class = CursoSerializer


class CursoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CursoModel.objects.all()
    serializer_class = CursoSerializer
