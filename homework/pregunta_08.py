"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd
def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de `c0` y `c2` al
    data frame que contiene el archivo `tbl0.tsv`.

    Rta/
         c0  c1   c2          c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

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
        cols_seen = cols_seen.groupby("c1").sum()
        return cols_seen["c2"]
    
    def sum_appearence(row):
        valores=tabla["c2"]
        row.sum()
        return valores
    
    def create_col(tabla):
     tabla["suma"] = tabla.index + tabla["c2"]
     tabla= tabla.reset_index(names=["c0"])
     return tabla
    
    datos = load_data("files/input")
    tabla = clean_data(datos)

    axis=tabla["c1"].unique()
    """t([ sum_appearence(row
                           ) for row 
           in axis])"""
    #um_appea = sum_appearence(col)
    cols_seen = max_cols(tabla)
    tabla = create_col(tabla)
    return tabla
print(pregunta_08())