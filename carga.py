def cargar_data(df, output_path):
    print("Cargando datos transformados...")
    df.to_csv(output_path, index=False)
    print(f"Datos cargados en: {output_path}")