from rest_framework import serializers
from .models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Empresa
        fields = ('cnpj', 'nome_empresa', 'cep', 'logradouro', 'numero', 'bairro',
                    'cidade', 'uf', 'data_criacao', 'data_atualizacao', 'url')
