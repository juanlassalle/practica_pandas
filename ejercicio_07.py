#SQLAlchemy: biblioteca para trabajar con SQL en Python
#PyMySQL: conector específico para MySQL.
import pandas as pd
from sqlalchemy import create_engine

#Conexión a mysql y lectura de datos
usuario = "root"
contrasena = "monitorfeo1517/"
host = "localhost"
base_datos = "alumno"

#cadena de conexión
conexion = create_engine(f"mysql+pymysql://{usuario}:{contrasena}@{host}/{base_datos}")

#Leer datos desde una tabla
df_mysql = pd.read_sql("SELECT * FROM autor",conexion)
print(df_mysql.head())
