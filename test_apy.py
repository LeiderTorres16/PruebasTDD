from fastapi.testclient import TestClient
from typing import Optional

from .main import app
from .main import fibonacci

client = TestClient(app)


def test_funcionExistente():
    response =client.get('/fibonacci/5')
    assert response.json() == {"Numero":8}


def test_valorCorrecto():
    response = client.get('/fibonacci/12')
    assert response.json() == {"Numero": 233}

def test_posicionNegativa():
    response = client.get('/fibonacci/-1')
    assert response.json() == {"Numero":0}


def test_valorNoEntero():
    response = client.get('/fibonacci/5.9')
    assert response.json() == {"Numero":0}

def test_valorString():
    response = client.get('/fibonacci/Alo')
    assert response.json() == {"Numero":0}