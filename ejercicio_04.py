#Los archivos CSV (Comma Separated Values) son el formato más extendido para intercambio de datos
#tabulares
import pandas as pd

#Leer un csv
df = pd.read_csv("datos.csv")
print(df.head())

print()
#Leer un archivo TSV (Tab Separated Values)
#Un archivo TSV (valores separados por tabulaciones) es un archivo de texto plano que almacena datos
#tabulares donde cada fila representa un registro y los valores de cada columna están separados por
#caracteres de tabulación en lugar de comas.
df_tsv = pd.read_csv("datos.tsv",sep="\t")
print(df_tsv.head())

print()
#Leer archivos de texto plano
df_txt = pd.read_csv("datos.txt",sep=";")
print(df_txt.head())

print()
#Guardar un DataFrame en CSV
df.to_csv("salida.csv",index= False)