import pandas as pd

#Leer json en pandas
df_json = pd.read_json("datos.json")
print(df_json)

df = pd.read_csv("datos.csv")

#Guardar un dataframe en json
#El parámetro orient define la estructura de salida: "records" (lista de diccionarios), 
#"split", "index", entre otros.
df.to_json("salida.json",orient="records",indent=4)