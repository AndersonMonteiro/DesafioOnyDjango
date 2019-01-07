import pytest
from .models import Empresa
from django.urls import reverse
from django.contrib.auth.models import User

pytestmark = pytest.mark.django_db

@pytest.fixture
def populate_db():
    User.objects.create_user('teste', 'teste@outlook.com', 'teste123')
    Empresa.objects.create(
        cnpj='00063960048721',
        nome='Supermercado Wallmart',
        cep='01050447',
        logradouro='Rua Teste Wallmart',
        numero='123',
        bairro='Caxangá',
        cidade='Recife',
        uf='PE'
    )
    Empresa.objects.create(
        cnpj='00013960044561',
        nome='Mercearia Arco Iris',
        cep='07808000',
        logradouro='Rua Arco Iris',
        numero='32145',
        bairro='Torre',
        cidade='Recife',
        uf='PE'
    )
    Empresa.objects.create(
        cnpj='98013960044123',
        nome='Supermercado Pão de Açucar',
        cep='65874000',
        logradouro='Rua José Bonifácio',
        numero='6545',
        bairro='Parnamirim',
        cidade='Recife',
        uf='PE'
    )

def test_empty_empresas(apiclient):
    response = apiclient.get(reverse('empresa-list'))
    assert response.status_code == 200
    assert len(response.json()) == 0

def test_empresas_get(apiclient, populate_db):
    response = apiclient.get(reverse('empresa-list'))
    json = response.json()
    assert response.status_code == 200
    assert len(json) == 3
    assert json[0]['cnpj'] == '00013960044561'

def test_empresas_post_unauthenticated(apiclient, populate_db):
    response = apiclient.post(reverse('empresa-list'), {
        'cnpj': '45543915006113',
        'nome': 'Supermercado Carrefour Paulista',
        'cep': '50710000',
        'logradouro': 'Rua José Bonifácio',
        'numero': '1315',
        'bairro': 'Torre',
        'cidade': 'Paulista',
        'uf': 'SP'
    })
    assert response.status_code == 403

def test_empresas_post_authenticated(apiclient, populate_db):
    apiclient.login(username='teste', password='teste123')
    response = apiclient.post(reverse('empresa-list'), {
        'cnpj': '34443915006113',
        'nome': 'Supermercado Carrefour Paulista',
        'cep': '50710000',
        'logradouro': 'Rua José Bonifácio',
        'numero': '1315',
        'bairro': 'Torre',
        'cidade': 'Paulista',
        'uf': 'SP'
    })
    assert response.status_code == 201
    assert reverse('empresa-detail', args=['34443915006113']) in response.json()['url']

def test_empresas_post_duplicated_cnpj (apiclient, populate_db):
    apiclient.login(username='teste', password='teste123')
    response = apiclient.post(reverse('empresa-list'), {
        'cnpj': '00063960048721',
        'nome': 'Supermercado Wallmart',
        'cep': '01050447',
        'logradouro': 'Rua Teste Wallmart',
        'numero': '123',
        'bairro': 'Caxangá',
        'cidade': 'Recife',
        'uf': 'PE'
    })
    assert response.status_code == 400

def test_empresas_detail_get(apiclient, populate_db):
    response = apiclient.get(reverse('empresa-detail', args=['00063960048721']))
    assert response.status_code == 200
    assert len(response.json()) == 11

def test_empresas_detail_get_inexistent_empresa(apiclient, populate_db):
    response = apiclient.get(reverse('empresa-detail', args=['99913960044123']))
    assert response.status_code == 404

def test_empresas_detail_patch_unauthenticated(apiclient, populate_db):
    response = apiclient.patch(reverse('empresa-detail', args=['00063960048721']), {
        'nome': 'Rede de Supermercados Wallmart'
    })
    assert response.status_code == 403

def test_empresas_detail_patch_authenticated(apiclient, populate_db):
    apiclient.login(username='teste', password='teste123')
    response = apiclient.patch(reverse('empresa-detail', args=['00063960048721']), {
        'logradouro': 'Rua Teste Wallmart Patched'
    })
    json = response.json()
    assert response.status_code == 200
    assert json['logradouro'] == 'Rua Teste Wallmart Patched'

"""test_ceps_detail_try_partial_update_with_put_authenticated"""
def test_empresas_detail_partial_put_authenticated(apiclient, populate_db):
    apiclient.login(username='teste', password='teste123')
    response = apiclient.put(reverse('empresa-list', args=['00063960048721']), {
        'nome': 'Supermercado Wallmart'
    })
    assert response.status_code == 404

def test_empresas_detail_delete(apiclient, populate_db):
    apiclient.login(username='teste', password='teste123')
    response = apiclient.delete(reverse('empresa-detail', args=['00063960048721']))
    assert response.status_code == 204


def test_api_root(apiclient):
    response = apiclient.get(reverse('api-root'))
    assert response.status_code == 200

def test_empresa_str(populate_db):
    empresa = Empresa.objects.get(pk='00063960048721')
    assert '00063960048721' in str(empresa)
