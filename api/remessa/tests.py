import json
from requests import get, post, options
from http import HTTPStatus


transacoes_url = 'http://localhost:8000/transacoes'
importar_url = 'http://localhost:8000/importar-remessa'


def test_get_transacoes_url_returning_200():

    request = get(transacoes_url)

    assert request.status_code == HTTPStatus.OK

def test_post_transacoes_url_returning_405():
    
    request = post(transacoes_url)

    assert request.status_code == HTTPStatus.METHOD_NOT_ALLOWED

def test_get_importar_url_returning_405():
    
    request = get(importar_url)

    assert request.status_code == HTTPStatus.METHOD_NOT_ALLOWED

def test_post_importar_url_without_file_returning_400():
    
    request = post(importar_url)

    assert request.status_code == HTTPStatus.BAD_REQUEST