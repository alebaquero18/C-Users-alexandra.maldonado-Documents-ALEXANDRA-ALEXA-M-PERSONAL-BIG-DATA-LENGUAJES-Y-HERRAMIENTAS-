import numpy as np
import argparse
import pandas as pd

def calcular_min_max(lista_numeros, verbose=True):
    """
    retorna los valores minimo y maximo d euna lista de numeros 
    args:
        lista_numeros:Type list
    """
    min_value=min(lista_numeros)
    max_value=max(lista_numeros)

    if verbose == True:
        print("valor minimo:", min_value)
        print("valor maximo:", max_value)
    else:
        pass
    return min_value, max_value

def calcular_valores_centrales(lista_numeros, verbose=True):
    """calcula la media y la desviacion estandar de numeros

    Args:
        lista_numeros (list): lista con valores numéricos
        verbose (bool, optional): para decidir si imprimir mensajes en pantalla. Defaults to True.

    Returns:
        Tuple: (media, desviacion estandar)
    """

    media   = np.mean(lista_numeros)
    dev_std = np.std(lista_numeros)

    if verbose == True:
        print("Media:", media)
        print("Desviacion Estandar:", dev_std)
    else:
        pass
    return media, dev_std

def calcular_valores(lista_numeros, verbose=True):   #del pseudo codigo esta es la funcion main
    suma=np.sum=(lista_numeros)
    min_val, max_val = calcular_min_max(lista_numeros)
    media, dev_std=calcular_valores_centrales(lista_numeros)

    return suma, min_val, max_val, media, dev_std

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--verbose", type=bool, default=True, help="para imprimir en pantalla informacion")
    args=parser.parse_args()

    
    lista_valores=[5, 4, 8, 9, 21]
    calcular_valores(lista_numeros=lista_valores, verbose=args.verbose)

if __name__ == "__main__":
   main()
