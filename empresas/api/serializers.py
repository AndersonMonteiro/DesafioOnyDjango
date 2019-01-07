from rest_framework import serializers
from .models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    """Serializer para mapeamento do Model no formato Json"""
    
    class Meta:
        model = Empresa
        fields = ('cnpj', 'nome', 'cep', 'logradouro', 'numero', 'bairro', 
                    'cidade', 'uf', 'data_criacao', 'data_atualizacao', 'url')
