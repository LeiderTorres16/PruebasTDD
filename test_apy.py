from fastapi.testclient import TestClient
from typing import Optional

from .main import app
from .main import fibonacci

client = TestClient(app)


def test_funcionExistente():
    assert fibonacci('5') == 8


def test_valorCorrecto():
    assert fibonacci('12') == 233

def test_posicionNegativa():
    assert fibonacci('-1') == 0


def test_valorNoEntero():
    assert fibonacci('5.9') == 0

def test_valorString():
    assert fibonacci('Alo') == 0