"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_09():
    """
    Agregue el año como una columna al dataframe que contiene el archivo
    `tbl0.tsv`.

    Rta/
        c0 c1  c2          c3  year
    0    0  E   1  1999-02-28  1999
    1    1  A   2  1999-10-28  1999
    2    2  B   5  1998-05-02  1998
    ...
    36  36  B   8  1997-05-21  1997
    37  37  C   9  1997-07-22  1997
    38  38  E   1  1999-09-28  1999
    39  39  E   5  1998-01-26  1998

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
    def datar_cols(tabla,cols):
        fechas=cols[0] 
        años=[ str(row[:4])for row in fechas]
        print(len(años))
        tabla["year"] = años
      # for i in cols:
      #      tabla["year"]+=i
        tabla= tabla.reset_index(names=["c0"])
        return tabla
    
    def create_col(tabla):
     cols=[tabla["c3"]]
     tabla=datar_cols(tabla,cols)
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
print(pregunta_09())