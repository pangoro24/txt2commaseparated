def verificar_palabras(input_comas, input_lineas):
    try:
        # Leer las palabras del archivo separado por comas
        with open(input_comas, 'r') as file_comas:
            palabras_comas = set(file_comas.read().strip().split(','))

        # Leer las palabras del archivo con palabras por línea
        with open(input_lineas, 'r') as file_lineas:
            palabras_lineas = set(line.strip() for line in file_lineas)

        # Encontrar las palabras que están en el archivo de comas pero faltan en el de líneas
        palabras_faltantes = palabras_comas - palabras_lineas

        if palabras_faltantes:
            print("Las siguientes palabras faltan en el archivo de líneas:")
            for palabra in palabras_faltantes:
                print(palabra)
        else:
            print("Todas las palabras están presentes en el archivo de líneas.")

    except FileNotFoundError as e:
        print(f"Error: {e.filename} no existe.")

# Nombres de los archivos
archivo_comas = 'palabras_comas.txt'  # Archivo con palabras separadas por comas
archivo_lineas = 'palabras.txt'  # Archivo con palabras separadas por líneas

# Llamar a la función para verificar las palabras
verificar_palabras(archivo_comas, archivo_lineas)
