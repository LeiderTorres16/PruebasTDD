from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get("/")
def fibonacci(posicion:str):

    try:
        posicionEntero = int(posicion)
    except:
        return 0

    if posicionEntero <= 0:
        return 0

    posicionActual, posicionFutura = 1, 1
    count = 1
    while count <= posicionEntero:

        valorPosicion = posicionActual + posicionFutura
        posicionActual = posicionFutura
        posicionFutura = valorPosicion
        count += 1

    return posicionActual


