"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_11():
    """
    Construya una tabla que contenga `c0` y una lista separada por ',' de
    los valores de la columna `c4` del archivo `tbl1.tsv`.

    Rta/
         c0       c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    def load_data(input_data):
        datos = pd.read_table(input_data + "/tbl1.tsv")
        return datos
    def filter_A(datos,letra):
        datos = datos[datos["c0"] == letra]
        return datos
    datos=load_data("files/input")
    letras= sorted(datos["c0"].unique())
    rows=[]
    for i in letras:
        datos2 = filter_A(datos,i)
        c4= datos2["c4"]
        rows.append(sorted(c4))
    rows = [",".join(str(val) for val in row) for row in rows]
    df= pd.DataFrame({'c0': letras,"c4":rows})
    return df
print(pregunta_11())