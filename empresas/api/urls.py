from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('empresas/', views.EmpresaLista.as_view(), name='empresa-list'),
    path('empresas/<str:pk>/', views.EmpresaDetalhe.as_view(), name='empresa-detail'),
    path('', views.api_root, name='api-root'),
]

urlpatterns = format_suffix_patterns(urlpatterns)