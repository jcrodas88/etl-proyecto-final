from extraccion import extraer_de_csv 
from transformacion import transformar_data
from carga import cargar_data
import os

if __name__ == "__main__":
    # Ruta del CSV (puede ser también una URL si el archivo está online)
    input_file = "data_input/netflix_titles.csv"   # asegúrate de que esté en el mismo directorio
    output_file = "data_output/netflix_transformado.csv"

    if not os.path.exists(input_file):
        print(f"Archivo no encontrado: {input_file}")
    else:
        raw_data = extraer_de_csv(input_file)
        transformed_data = transformar_data(raw_data)
        cargar_data(transformed_data, output_file)