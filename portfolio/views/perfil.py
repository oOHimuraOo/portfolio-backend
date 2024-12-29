from rest_framework import generics
from portfolio.models import PerfilModel
from portfolio.serializers.perfil import PerfilSerializer


class PerfilView(generics.RetrieveUpdateAPIView):
    queryset = PerfilModel.objects.all()
    serializer_class = PerfilSerializer

    def get_object(self):
        return PerfilModel.objects.first()
