"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_07():
    """
    Calcule la suma de la `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: c2, dtype: int64
    """
    import pandas as pd
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
    
    datos = load_data("files/input")
    tabla = clean_data(datos)

    axis=tabla["c1"].unique()
    """t([ sum_appearence(row
                           ) for row 
           in axis])"""
    #um_appea = sum_appearence(col)
    cols_seen = max_cols(tabla)

    return cols_seen
print(pregunta_07())