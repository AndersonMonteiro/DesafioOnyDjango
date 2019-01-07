from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('promocoes/', views.PromocaoList.as_view(), name='promocao-list'),
    path('promocoes/<pk>/', views.PromocaoDetail.as_view(), name='promocao-detail'),
    path('', views.api_root, name='api-root'),    
]

urlpatterns = format_suffix_patterns(urlpatterns)