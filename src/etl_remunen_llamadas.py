#Pseudo codigo
#1. ller archivo.csv
#2. Extraer el resumen 
#3. guardar el resumen del formato .csv

#from fileinput import filename
import pandas as pd
import os
from pathlib import Path


def main(): # esta es la funcion principal, a penas yo entre va a entrar ahí 

    # leer archivo
    data=get_data(filename="llamadas123_julio_2022.csv")

    # Extraer resumen 
    df_resumen =  get_summary(data)
    
    # Guarde el resumen
    save_data(df_resumen, filename)

def save_data(df, filename):
    out_name="resumen_"+filename
    root_dir = Path(".").resolve()
    out_path=os.path.join(root_dir,"data", "processed", out_name)

    #print(out_path)
    df.to_csv(out_path)
    

def get_summary(data):
    #crear un diccionario vacio 
    dict_resumen=dict()

    for col in data.columns:
        valores_unicos=data[col].unique()
        n_valores=len(valores_unicos)

        dict_resumen[col]=n_valores

    df_resumen=pd.DataFrame.from_dict(dict_resumen, orient="index")
    df_resumen.rename({0: "count"}, axis=1, inplace=True)

    return df_resumen

def get_data(filename):
    data_dir="raw"
    root_dir=Path(".").resolve()
    file_path=os.path.join(root_dir, "data", data_dir, filename)

    data=pd.read_csv(file_path, enconding="latin-1", sep=";")
    return data

if name == "_main_":
    main()


