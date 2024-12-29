from django.urls import path
from portfolio.views.site_info import SiteInfoView
from portfolio.views.escolas import EscolasListView
from portfolio.views.tecnologia import TecnologiaListView
from portfolio.views.curso import CursoListView, CursoDetailView
from portfolio.views.projeto import ProjetoListView, ProjetoDetailView
from portfolio.views.perfil import PerfilView
from portfolio.views.footer import FooterView
from portfolio.views.subprojeto import SubProjetoDetailView, SubProjetoListView

urlpatterns = [
    path('site-info/', SiteInfoView.as_view(), name='site-info'),
    path('escolas/', EscolasListView.as_view(), name='escolas'),
    path('tecnologias/', TecnologiaListView.as_view(), name='tecnologia'),
    path('site-info/cursos/', CursoListView.as_view(), name='curso-list'),
    path('site-info/cursos/<int:pk>/', CursoDetailView.as_view(), name='curso-detail'),
    path('site-info/projetos/', ProjetoListView.as_view(), name='projeto-list'),
    path('site-info/projetos/<int:pk>/', ProjetoDetailView.as_view(), name='projeto-detail'),
    path('site-info/subprojetos', SubProjetoListView.as_view(), name='subprojeto-list'),
    path('site-info/subprojetos/<int:pk>/', SubProjetoDetailView.as_view(), name='subprojeto-datail'),
    path('site-info/perfil/', PerfilView.as_view(), name='perfil'),
    path('site-info/footer/', FooterView.as_view(), name='footer'),
]
