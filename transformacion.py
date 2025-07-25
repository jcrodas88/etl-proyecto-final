import pandas as pd

def transformar_data(df):
    print("Transformando datos...")

    # Eliminar columnas que no nos interesan
    df = df.drop(columns=['show_id', 'description'])

    # Eliminar duplicados
    df = df.drop_duplicates()

    # Llenar valores nulos con texto
    df['director'] = df['director'].fillna('Desconocido')
    df['cast'] = df['cast'].fillna('Sin reparto')

    # Formatear fechas
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    # Crear nueva columna con año de incorporación
    df['año_agregado'] = df['date_added'].dt.year

    return df