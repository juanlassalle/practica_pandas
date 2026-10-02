#Pandas también puede trabajar con archivos excel (.xlsx,.xls), aunque requier instalar openpycl o xlrd
#para manejar los formatos modernos.
import pandas as pd

#Leer un archivo excel
#Leer hoja por defecto
df_excel = pd.read_excel("Libro1.xlsx")
print(df_excel.head())

#Leer una hoja específica
df_hoja = pd.read_excel("Libro1.xlsx",sheet_name="Hoja1")