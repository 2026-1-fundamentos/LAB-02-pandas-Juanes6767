"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_12():
    """
    Construya una tabla que contenga `c0` y una lista separada por ','
    de los valores de la columna `c5a`  y `c5b` (unidos por ':') de la
    tabla `tbl2.tsv`.

    Rta/
         c0                                   c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    
    def sum_cols(tabla):
            cols_seen = tabla[["c1", "c2"]]
            cols_seen = cols_seen.groupby("c1").sum()
            return cols_seen["c2"]
        
    def sum_appearence(row):
            valores=datos["c2"]
            row.sum()
            return valores
    
    def load_data(input_data):
        datos = pd.read_table(input_data + "/tbl2.tsv")
        return datos
    def filter_A(datos,letra):
        datos = datos[datos["c0"] == letra]
        return datos

    def create_col(tabla,cols):
         tabla["c5"] = ""
         for col in cols:
          if col != "c5b":
               tabla["c5"] += tabla[col].astype(str)
          else:
               tabla["c5"] += ":"+tabla[col].astype(str)
         return tabla
     
    datos = load_data("files/input")

    cols=["c5a","c5b"]
    datos = create_col(datos,cols)

    letras= sorted(datos["c0"].unique())
    rows=[]
    for i in letras:
        datos2 = filter_A(datos,i)
        c5= datos2["c5"]
        rows.append(sorted(c5))
    rows = [",".join(str(val) for val in row) for row in rows]
    df= pd.DataFrame({'c0': letras,"c5":rows})
    return df
print(pregunta_12())