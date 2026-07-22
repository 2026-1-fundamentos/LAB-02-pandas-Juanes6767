"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_05():
    """
    Calcule el valor máximo de `c2` por cada letra en la columna `c1` del
    archivo `tbl0.tsv`.

    Rta/
    c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: c2, dtype: int64
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
    
    def max_cols(tabla):
        cols_seen = tabla[["c1", "c2"]]
        cols_seen = cols_seen.groupby("c1").max()
        return cols_seen["c2"]
    
    def measure_appearence(col):
        valores=tabla["c2"].values
        print(valores)
        max = col.max(axis=0)
        return max
    
    datos = load_data("files/input")
    tabla = clean_data(datos)

    col=tabla["c2"]
    max_appea = measure_appearence(col)
    cols_seen = max_cols(tabla)

    return cols_seen
print(pregunta_05())