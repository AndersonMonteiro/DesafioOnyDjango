from django.db import models

class Promocao(models.Model):
    descricao = models.CharField(max_length=200)
    produto = models.CharField(max_length=100)
    valor_unidade = models.DecimalField(max_digits=6, decimal_places=2)
    descricao_unidade = models.CharField(max_length=200)
    data_inicial = models.DateField()
    data_final = models.DateField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    cnpj = models.CharField(max_length=15)
    nome_empresa = models.CharField(max_length=200)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=80)
    uf = models.CharField(max_length=2)
    
    class Meta:
        ordering = ('descricao',)

    def __str__(self):
        return self.descricao