from rest_framework import generics
from portfolio.models import FooterModel
from portfolio.serializers import FooterSerializer


class FooterView(generics.RetrieveUpdateAPIView):
    queryset = FooterModel.objects.all()
    serializer_class = FooterSerializer

    def get_object(self):
        return FooterModel.objects.first()
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.views += 1
        instance.save()
        return super().retrieve(request, *args, **kwargs)
