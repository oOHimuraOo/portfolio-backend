from rest_framework import serializers
from portfolio.models import SiteInfoModel
from portfolio.serializers.perfil import PerfilSerializer
from portfolio.serializers.footer import FooterSerializer
from portfolio.serializers.curso import CursoSerializer
from portfolio.serializers.projeto import ProjetoSerializer


class SiteInfoSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer()
    footer = FooterSerializer()
    cursos = CursoSerializer(many=True)
    projetos = ProjetoSerializer(many=True)

    class Meta:
        model = SiteInfoModel
        fields = ["perfil", "footer", "cursos", "projetos"]
