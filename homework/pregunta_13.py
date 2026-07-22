"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
    def load_data(input_data,archivo):
        datos = pd.read_table(input_data + archivo)
        return datos
    
    def strip_index(datos):
        datos=datos.set_index(datos.columns[0]) #datos. 
        return datos
    def clean_data(datos):
        df=strip_index(datos)
        return df
    def len_filas(df):
        len = df.__len__()
        return len
    def sum_cols(tabla):
        cols_seen = tabla[["c1", "c5b"]]
        cols_seen = cols_seen.groupby("c1").sum()
        return cols_seen["c5b"]
    
    datos1 = load_data("files/input", "/tbl0.tsv")
    datos2 = load_data("files/input", "/tbl2.tsv")
    tabla=pd.merge(datos1, datos2)
    #df = clean_data(datos)
    #len = len_filas(df)
    suma = sum_cols(tabla)
    return suma
print(pregunta_13())
