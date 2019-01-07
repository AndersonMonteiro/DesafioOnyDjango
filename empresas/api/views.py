from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Empresa
from .serializers import EmpresaSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'empresas': reverse('empresa-list', request=request, format=format),
    })

class EmpresaLista(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EmpresaDetalhe(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
