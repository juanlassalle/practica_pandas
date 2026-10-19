#Exploración de datos en Pandas
import pandas as pd

#Ejemplo de DataFrame
datos = {
    "Nombre" : ["Ana","Luis","Carla","Pedro","María"],
    "Edad" : [23,35,29,42,31],
    "Ciudad" : ["Córdoba","Buenos Aires","Rosario","Mendoza","Salta"],
    "Salario" : [55000,72000,61000,83000,59000]
}

df = pd.DataFrame(datos)

print(df.head(3)) #muestra las 3 primeras filas
print()
print(df.tail(2)) #muestra las 2 últimas filas
print()
print(df.info()) #informa tipo de datos y valores no nulos
print()
print(df.describe()) #genera estadísticas descriptiva

print()
print(df.dtypes)

#Convertir Edad a float
df["Edad"] = df["Edad"].astype(float)
#Convertir Salario a string
df["Salario"] = df["Salario"].astype(str)
print()
print(df.dtypes)

df_fechas = pd.DataFrame(
    {
        "Fecha" : ["2025-01-01","2025-02-15","2025-03-20"]
    }
)
df_fechas["Fecha"] = pd.to_datetime(df_fechas["Fecha"])
print()
print(df_fechas)
print(df_fechas.dtypes)