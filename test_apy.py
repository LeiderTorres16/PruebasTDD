from fastapi.testclient import TestClient
from typing import Optional
from .main import app
from .main import isPrime
from .main import fibonacci
from fastapi import FastAPI
from http import client
from urllib import response

client = TestClient(app)


# caso peticion hello fastapi
def test_get_helloFastAPI():
    response = client.get('/helloFastAPI')
    assert response.status_code == 200
    assert response.json() == "Hello FastAPI"


# caso peticion la funcion existe
def test_funcionExistente():
    response =client.get('/fibonacci/5')
    assert response.status_code == 200
    assert response.json() == {"Numero":8}

# caso peticion Posicion y numero correcto
def test_valorCorrecto():
    response = client.get('/fibonacci/12')
    assert response.status_code == 200
    assert response.json() == {"Numero": 233}

# caso peticion Posicion Negativa
def test_posicionNegativa():
    response = client.get('/fibonacci/-1')
    assert response.status_code == 200
    assert response.json() == {"Numero":0}

# caso peticion Posicion con numero no Entero
def test_valorNoEntero():
    response = client.get('/fibonacci/5.9')
    assert response.status_code == 200

# caso peticion Posicion con letra
def test_valorString():
    response = client.get('/fibonacci/Alo')
    assert response.status_code == 200


# caso peticion Numero primo
def test_get_isPrimeCasoNumeroPrimo():
    response = client.get('/numeroPrimo/53')
    assert response.status_code == 200
    assert response.json() == True


# caso peticion Numero no primo
def test_get_isPrimeCasoNumeroNoPrimo():
    response = client.get('/numeroPrimo/28')
    assert response.status_code == 200
    assert response.json() == False


# caso peticion numero negativo
def test_get_isPrime_CasoNegativo():
    response = client.get('/numeroPrimo/-5')
    assert response.status_code == 200
    assert response.json() == False


# caso peticion caracter letra
def test_get_isPrime_CasoLetra():
    response = client.get('/numeroPrimo/a')
    assert response.status_code == 200


# caso peticion caracter especial
def test_get_isPrime_CasoCaracterEspecial():
    response = client.get('/numeroPrimo/.')
    assert response.status_code == 200


# caso peticion numero flotante
def test_get_isPrime_CasoFlotante():
    response = client.get('/numeroPrimo/2.4')
    assert response.status_code == 200


# caso numero primo
def test_function_isPrimeCasoNumeroPrimo():
    assert isPrime(53) == True


# caso numero no primo
def test_function_isPrimeCasoNumeroNoPrimo():
    assert isPrime(9) == False


# parametro letra
def test_function_isPrime_casoLetra():
    assert isPrime('a')


# parametro caracter especial
def test_function_isPrime_casoCaracterEspecial():
    assert isPrime('.')


# parametro numero decimal
def test_function_isPrime_casoDatoFlotante():
    assert isPrime(1.5) == False


# parametro numero negativo
def test_function_isPrime_casoNumeroNegativo():
    assert isPrime(-1) == False