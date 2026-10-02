#El DataFrame es la estructura estrella de Pandas: se asemeja a una tabla de Excel o SQL, 
#con filas identificadas por un índice y columnas con nombres. Puede crearse a partir de 
#múltiples fuentes de datos.
import pandas as pd

#Desde un diccionario de listas
datos = {
    "Nombre" : ["Ana","Luis","Carla","Pedro"],
    "Edad" : [23,35,29,42],
    "Ciudad" : ["Córdoba","Buenos Aires","Rosario","Mendoza"]
}

df = pd.DataFrame(datos)
print(df)

#Desde una lista de diccionarios
datos2 = [
    {"Nombre": "Ana", "Edad": 23, "Ciudad": "Córdoba"},
    {"Nombre": "Luis", "Edad": 35, "Ciudad": "Buenos Aires"},
    {"Nombre": "Carla", "Edad": 29, "Ciudad": "Rosario"}
]

df2 = pd.DataFrame(datos2)
print(df2)