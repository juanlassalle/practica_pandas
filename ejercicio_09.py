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
#El índice identifica cada fila, es secuencial pero se puede personalizar
print(df.index)

#Nombre actúa como identificador de cada fila
df_personalizado = df.set_index("Nombre")
print()
print(df_personalizado)

df_reset = df_personalizado.reset_index()
print(df_reset.head())

df.rename(columns={"Nombre" : "Empleado","Ciudad" : "Localidad"}, inplace=True)
print()
print(df.head())