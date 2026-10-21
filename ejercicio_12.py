#Detección de valores nulos (isnull,notnull)
#En pandas los valores faltantes se representan con NaN. Podemos identificarlos rápidamente
#usando los métodos isnull() y notnull()
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
print(df.isnull()) #detecta valores nulos
print()
print(df.notnull()) #detecta valores no nulos
print()
print(df.isnull().sum()) #contar valores nulos por columna
