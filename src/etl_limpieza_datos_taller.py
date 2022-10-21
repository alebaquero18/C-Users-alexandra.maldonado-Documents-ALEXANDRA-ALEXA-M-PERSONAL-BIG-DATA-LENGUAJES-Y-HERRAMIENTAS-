# TALLER LIMPIEZA DE DATOS

import numpy as np
import pandas as pd
import os
from pathlib import Path

bucket = "gs://amaldonado_bucket_llamadas123"

def get_data(filename):
    
#filename="llamadas123_julio_2022.csv"
    data_dir="raw"
    file_path=os.path.join(bucket,"data", data_dir, filename)
    data=pd.read_csv(file_path, encoding="latin-1", sep=";")
    data.head()

    print('get_data')
    print('La tabla contiene', data.shape[0], 'filas', data.shape[1], 'columnas')
    return data

def generate_report(data):
    # Crear un diccionario vacio
    dict_resumen = dict()

    # loop para llenar el diccionario de columnas con valores unicos
    for col in data.columns:
        valores_unicos = data[col].unique()
        n_valores = len(valores_unicos)
        dict_resumen[col] = n_valores

    reporte = pd.DataFrame.from_dict(dict_resumen, orient='index')
    reporte.rename({0: 'Count'}, axis=1, inplace=True)

    print('generate_report')
    print(reporte.head())
    return reporte

def save_data(reporte, filename):
    # Guardar la tabla:

    out_name = 'resumen_' + filename
    out_path = os.path.join(bucket, 'data', 'processed', out_name)
    reporte.to_csv(out_path)
    
    print("Guardado en BQ")
    # Guardar la tabla en BigQuery
    reporte.to_gbq(destination_table="linen-synthesis-364223.llamadas_123",)

def main():

    filename = "llamadas123_julio_2022.csv"
    data = get_data(filename)
    reporte = generate_report(data)
    save_data(reporte, filename)

    print('DONE!!!')

if __name__ == '__main__':
    main()
    
# Registros duplicados

    bucket = "gs://amaldonado_bucket_llamadas123"

def get_data(filename):
    data_dir="raw"
    file_path=os.path.join(bucket,"data", data_dir, filename)
    data=pd.read_csv(file_path, encoding="latin-1", sep=";")
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

