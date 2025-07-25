import pandas as pd

#Crear una función para extraer los datos de los archivos csv
def extraer_de_csv(ruta_archivo_csv):
    print("Extrayendo datos...")
    df = pd.read_csv(ruta_archivo_csv)
    return df