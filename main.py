from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get('/fibonacci/{posicion}')
def fibonacci(posicion:int):

    if posicion <= 0:
        return {"Numero":0}

    posicionActual, posicionFutura = 1, 1
    count = 1
    while count <= posicion:

        valorPosicion = posicionActual + posicionFutura
        posicionActual = posicionFutura
        posicionFutura = valorPosicion
        count += 1

    return {"Numero":posicionActual}


