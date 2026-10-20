#Con iloc seleccionamos datos según su posición numérica, al estilo de un array de NumPy.

import pandas as pd

datos = {
    "Nombre": ["Ana", "Luis", "Carla", "Pedro", "María"],
    "Edad": [23, 35, 29, 42, 31],
    "Ciudad": ["Córdoba", "Buenos Aires", "Rosario", "Mendoza", "Salta"],
    "Salario": [55000, 72000, 61000, 83000, 59000]
}

df = pd.DataFrame(datos)
df = df.set_index("Nombre")  # usamos Nombre como índice
print()
# Seleccionar la primera fila
print(df.iloc[0])
print()
# Seleccionar la tercera fila y segunda columna
print(df.iloc[2, 1])
print()
# Seleccionar un rango de filas
print(df.iloc[1:4])  # filas 1 a 3
print()
# Seleccionar rango de filas y columnas
print(df.iloc[0:2, 0:2])  # primeras 2 filas y 2 columnas
print()

#Filtrado con condiciones lógicas

# Filtrar empleados con Edad mayor a 30
print(df[df["Edad"] > 30])
print()
# Filtrar con varias condiciones (AND y OR)
print(df[(df["Edad"] > 30) & (df["Salario"] > 60000)])  # AND
print()
print(df[(df["Ciudad"] == "Rosario") | (df["Ciudad"] == "Salta")])  # OR
print()
#Uso de máscaras booleanas
#Una máscara booleana es un arreglo de true/false que pandas usa para filtrar filas
#de forma reutilizable

# Crear una máscara booleana
mask = df["Edad"] > 30
print(mask)

# Aplicar la máscara al DataFrame
print(df[mask])