"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    def load_data(input_data):
        datos = pd.read_table(input_data + "/tbl1.tsv")
        return datos
    
    def strip_index(datos):
        datos=datos.set_index(datos.columns[0]) #datos. 
        return datos
    def clean_data(datos):
        df=strip_index(datos)
        return df
    
    def calc_unique_cols(df):
        unique_vals = df["c4"].unique()
        
        unique_vals = [word.upper() for word in unique_vals]
        unique_vals = sorted(unique_vals)
        return unique_vals
    
    def max_cols(tabla):
        cols_seen = tabla[["c1", "c2"]]
        cols_seen = cols_seen.groupby("c1").max()
        return cols_seen["c2"]
    
    def measure_appearence(col):
        valores=tabla["c2"].values
        #print(valores)
        max = col.max(axis=0)
        return max
    
    datos = load_data("files/input")
    tabla = clean_data(datos)

    col=tabla["c4"]
    #max_appea = measure_appearence(col)
    #cols_seen = max_cols(tabla)
    unique_vals=calc_unique_cols(tabla)

    return unique_vals
print(pregunta_06())