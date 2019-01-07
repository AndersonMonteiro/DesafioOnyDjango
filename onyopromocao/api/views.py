from django.shortcuts import render

import json
from requests import get
#from django.conf import settings
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Promocao
from .serializers import PromocaoSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'promocoes': reverse('promocao-list', request=request, format=format),
    })


def _on_create_or_update(serializer):
    data = serializer.validated_data
#    response = get('{}{}/'.format(settings.CEP_URL, data['cep']))
    response = get('http://127.0.0.1:8000/api/v1/empresas/45543915006122.json')
    if response.status_code != 200:
        data = json.loads(response.content)
        data['detail'] = 'CNPJ: ' + data['detail']
        raise serializers.ValidationError(data)
    url_adress = json.loads(response.content)
    url_adress.pop('url')
    data.update(url_adress)
    serializer.save() 
    return

class PromocaoList(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Promocao.objects.all()
    serializer_class = PromocaoSerializer

    def on_create(self, serializer):
        _on_create_or_update(serializer)
        return
    
class PromocaoDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Promocao.objects.all()
    serializer_class = PromocaoSerializer

    def perform_create(self, serializer):
        _on_create_or_update(serializer)
        return
        