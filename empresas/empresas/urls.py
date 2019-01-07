from rest_framework_swagger.views import get_swagger_view
from django.urls import path, include

schema_view = get_swagger_view(title='API Empresa')

urlpatterns = [
    path('', schema_view),
    path('api/v1/', include('api.urls')),
    path('auth/', include('rest_framework.urls')),
]
