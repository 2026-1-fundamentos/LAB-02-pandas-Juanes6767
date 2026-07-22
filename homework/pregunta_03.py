"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
    def load_data(input_data):
        datos = pd.read_table(input_data + "/tbl0.tsv")
        return datos
    
    def strip_index(datos):
        datos=datos.set_index(datos.columns[0]) #datos. 
        return datos
    def clean_data(datos):
        df=strip_index(datos)
        return df
    def calc_len_cols(df):
        len = df.columns.__len__()
        return len
    def count_appearences(tabla):
        c1 = tabla["c1"]
        count = c1.value_counts()
        return count
    datos = load_data("files/input")
    tabla = clean_data(datos)
    len = calc_len_cols(tabla)
    group_count = count_appearences(tabla)

    return group_count.sort_index()
print(pregunta_03())