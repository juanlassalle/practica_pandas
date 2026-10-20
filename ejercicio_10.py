'''En Pandas podemos seleccionar filas, columnas o subconjuntos de diversas maneras dentro de un DataFrame. 
Las herramientas principales son loc (por etiquetas), iloc (por posición numérica), condiciones lógicas y 
máscaras booleanas. Dominar estas técnicas permite analizar datasets con mayor precisión en Python'''
import pandas as pd

datos = {
    "Nombre": ["Ana", "Luis", "Carla", "Pedro", "María"],
    "Edad": [23, 35, 29, 42, 31],
    "Ciudad": ["Córdoba", "Buenos Aires", "Rosario", "Mendoza", "Salta"],
    "Salario": [55000, 72000, 61000, 83000, 59000]
}

df = pd.DataFrame(datos)
df = df.set_index("Nombre") #usamos Nombre como índice
print(df)
print()
#seleccionar una fila por etiqueta
print(df.loc["Carla"])
print()
#seleccionar varias filas
print(df.loc[["Ana","Pedro"]])
print()
#seleccionar filas y columnas específicas
print(df.loc["Luis","Ciudad"]) #valor único
print()
print(df.loc[["Ana","María"],["Edad","Salario"]])