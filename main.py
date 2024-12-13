from fastapi import FastAPI
import random

nombres = []

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application"}


@app.post("/agregar_nombre/")
def agregar_nombre(nombre: str):
    if nombre not in nombres:
        nombres.append(nombre)
        return {"message": f"Nombre {nombre} agregado exitosamente"}
    else:
        return {"message": f"El nombre {nombre} ya existe en la lista"}


@app.get("/sorteo/")
def sorteos():
    # Seleccionar un nombre al azar
    nombre_seleccionado = random.choice(nombres)
    # Eliminar el nombre seleccionado de la lista
    nombres.remove(nombre_seleccionado)
    return {"santa_secreto": nombre_seleccionado}
