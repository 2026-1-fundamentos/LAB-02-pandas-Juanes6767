"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_04():
    """
    Calcule el promedio de `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta
    c1
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: c2, dtype: float64
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
    
    def isolate_cols(tabla):
        cols_seen = tabla[["c1", "c2"]]
        cols_seen = cols_seen.groupby("c1").mean()
        return cols_seen["c2"]
    def count_appearences(col):
        count = col.value_counts()
        return count
    
    datos = load_data("files/input")
    tabla = clean_data(datos)

    col=tabla["c1"]
    group_count = count_appearences(col)
    cols_seen = isolate_cols(tabla)

    return cols_seen
print(pregunta_04())