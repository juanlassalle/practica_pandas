import pandas as pd

#Crear una serie (columna de datos)
serie = pd.Series([10,20,30,40,50])
print("Serie: ")
print(serie)

# Crear un DataFrame (tabla)
datos = {
    "Nombre": ["Ana", "Luis", "Carla", "Pedro"],
    "Edad": [23, 35, 29, 42],
    "Ciudad": ["Córdoba", "Buenos Aires", "Rosario", "Mendoza"]
}
df = pd.DataFrame(datos)

print("\nDataFrame:")
print(df)

print("\n=== Diferencia entre Serie y DataFrame ===")
print("Tipo de serie:", type(serie))
print("Tipo de DataFrame:", type(df))
print("Columnas del DataFrame:", df.columns.tolist())