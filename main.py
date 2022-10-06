from fastapi import FastAPI
from typing import Optional
from typing import Union


app = FastAPI()

def isPrime(numero:int):
    if numero <= 0:
        return False
    elif numero == 1:
        return True
    else:
        for i in range(2,numero+1):
            if numero%i == 0 and i<numero:
                return False
            elif i==numero:
                return True

@app.get('/fibonacci/{posicion}')
def fibonacci(posicion:int):

    if posicion <= 0:
        return {"Numero":0}

    posicionActual, posicionFutura = 0, 1
    count = 1
    while count <= posicion:

        valorPosicion = posicionActual + posicionFutura
        posicionActual = posicionFutura
        posicionFutura = valorPosicion
        count += 1

    return {"Numero":posicionActual}


@app.get('/helloFastAPI')
async def leer_helloFastAPI():
    return "Hello FastAPI"



@app.get('/numeroPrimo/{numero}')
async def numeroPrimo(numero:int):
    return isPrime(numero)


