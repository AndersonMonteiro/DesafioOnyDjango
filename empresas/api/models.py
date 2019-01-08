from django.db import models

class Empresa(models.Model):
    """Classe que representa a model Empresa"""
    cnpj = models.CharField(max_length=15, primary_key=True)
    nome_empresa = models.CharField(max_length=200)
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=80)
    uf = models.CharField(max_length=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('cnpj', )

    def __str__(self):
        return self.cnpj
        