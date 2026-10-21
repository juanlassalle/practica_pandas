#Eliminación de datos (dropna)
#A veces lo más simple es eliminar o columnas que contienen valores faltantes. dropna()
#ofrece varios parámetros para controlar la limpieza
# Eliminar filas con cualquier valor nulo
import pandas as pd
import numpy as np

datos = {
    "Nombre": ["Ana", "Luis", "Carla", "Pedro", "María"],
    "Edad": [23, np.nan, 29, 42, None],
    "Ciudad": ["Córdoba", "Buenos Aires", None, "Mendoza", "Salta"],
    "Salario": [55000, 72000, None, 83000, 59000]
}

df = pd.DataFrame(datos)
print(df)
print()
# Eliminar filas con cualquier valor nulo
df_sin_nulos = df.dropna()
print(df_sin_nulos)
print()
# Eliminar columnas con cualquier valor nulo
df_sin_columnas = df.dropna(axis=1)
print(df_sin_columnas)
print()
# Eliminar filas solo si todos los valores son nulos
df_sin_todos = df.dropna(how="all")
print(df_sin_todos)
print()
# Eliminar filas si tienen menos de un mínimo de valores no nulos
df_min = df.dropna(thresh=3)  # conserva filas con al menos 3 valores válidos
print(df_min)