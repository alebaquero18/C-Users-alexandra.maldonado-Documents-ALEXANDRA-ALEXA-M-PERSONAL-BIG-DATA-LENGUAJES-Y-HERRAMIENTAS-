# TALLER LIMPIEZA DE DATOS

import numpy as np
import pandas as pd
import os
from pathlib import Path

filename="llamadas123_julio_2022.csv"
data_dir="raw"
file_path=os.path.join(root_dir,"data", data_dir, filename)
data=pd.read_csv(file_path, encoding="latin-1", sep=";")

data.head()

# Registros duplicados

print("forma incial", data.shape)
data=data.drop_duplicates() 
print("forma final", data.shape)
data.info()

# cuente los diferentes valores
data["UNIDAD"].value_counts(dropna=False)

# reemplace en la columna unidad los nulos por SIN_DATO
data["UNIDAD"].fillna("SIN_DATO").value_counts(dropna=False, normalize=False)
data["UNIDAD"]=data["UNIDAD"].fillna("SIN_DATO")
data.info()

# Manipule las fechas 
col="FECHA_INICIO_DESPLAZAMIENTO_MOVIL"
data[col].max()

# Aplique filtros
val_min=data[col].min()
data[data[col] != val_min]

# Datetime
data[col]=pd.to_datetime(data[col], errors="coerce")
data.info()

data["RECEPCION"]
val_min=data[col].min()
data[data[col] == val_min]

from dateutil.parser import parse
parse("08/02/2021")
def convertir_formato_fecha(str_fecha):
    val_datetime=parse(str_fecha, dayfirst=False)
    return val_datetime


data=data.reset_index()


lista_fechas=list()
n_filas=data.shape[0] #len(data[RECEPCION])
#n_filas=len(data["RECEPCION"])
for i in range(0, n_filas):

    str_fecha=data["RECEPCION"][i]
    
    try: #tráte de hacerlo o sino haga algo
        val_datetime=convertir_formato_fecha(str_fecha=str_fecha)
        lista_fechas.append(val_datetime)
    except Exception as e:
        #print(i, e)
        lista_fechas.append(str_fecha)
        continue

lista_fechas

data["RECEPCION_CORREGIDA"]=lista_fechas
data

data["RECEPCION_CORREGIDA"]=pd.to_datetime(data["RECEPCION_CORREGIDA"], errors="coerce")
data

# CONSISTENCIA DE DATOS

data["EDAD"].value_counts(dropna=False)

data["EDAD"].replace({"SIN_DATO":np.nan}).value_counts(dropna=False)
data["EDAD"]=data["EDAD"].replace({"SIN_DATO":np.nan})

x=np.nan
f=lambda x: x if pd.isna(x) == True else int(x)
f(x)

data ["EDAD"]=data["EDAD"].apply(f)

data.info()

word="BigData   "
print(word, word.lower(), word.upper(), word.lstrip() )
data["LOCALIDAD"].apply(lambda x: x.strip()).value_counts()


