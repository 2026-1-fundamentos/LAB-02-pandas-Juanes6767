"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""

import pandas as pd
def pregunta_10():
    """
    Construya una tabla que contenga `c1` y una lista separada por ':' de los
    rows de la columna `c2` para el archivo `tbl0.tsv`.

    Rta/
                                 c2
    c1
    A               1:1:2:3:6:7:8:9
    B                 1:3:4:5:6:8:9
    C                     0:5:6:7:9
    D                   1:2:3:5:5:7
    E   1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """

    def load_data(input_data):
        datos = pd.read_table(input_data + "/tbl0.tsv")
        return datos
    def filter_A(datos,letra):
        datos = datos[datos["c1"] == letra]
        return datos
    datos=load_data("files/input")
    letras= sorted(datos["c1"].unique())
    rows=[]
    for i in letras:
        datos2 = filter_A(datos,i)
        c2= datos2["c2"]
        rows.append(sorted(c2))
    rows = [":".join(str(val) for val in row) for row in rows]
    df= pd.DataFrame({'c1': letras,"c2":rows})
    return df.set_index("c1")
print(pregunta_10())