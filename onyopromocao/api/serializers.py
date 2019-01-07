from rest_framework import serializers
from .models import Promocao

class PromocaoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Promocao
        fields = ('cnpj', 'descricao', 'produto', 'valor_unidade', 'descricao_unidade',
         'data_inicial', 'data_final', 'data_criacao', 'data_atualizacao', 'cnpj_empresa',)
