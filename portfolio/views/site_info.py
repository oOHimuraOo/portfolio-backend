from rest_framework.views import APIView
from rest_framework.response import Response
from portfolio.models import SiteInfoModel, CursoModel, ProjetoModel
from portfolio.serializers.site_info import SiteInfoSerializer


class SiteInfoView(APIView):
    def get(self, request):
        site_info = SiteInfoModel.objects.first()
        cursos = CursoModel.objects.all()
        projetos = ProjetoModel.objects.all()

        serializer = SiteInfoSerializer(site_info, context={"cursos": cursos, "projetos": projetos})
        return Response(serializer.data)
