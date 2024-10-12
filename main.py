def convertir_palabras_a_coma(input_file, output_file):
    try:
        # Leer todas las palabras del archivo de entrada
        with open(input_file, 'r') as infile:
            palabras = [line.strip() for line in infile]

        # Escribir las palabras separadas por comas en el archivo de salida
        with open(output_file, 'w') as outfile:
            outfile.write(','.join(palabras))

        print(f"Archivo '{output_file}' generado con éxito.")
    except FileNotFoundError:
        print(f"Error: El archivo '{input_file}' no existe.")

# Nombre de los archivos de entrada y salida
archivo_entrada = 'palabras.txt'  # Cambia por el nombre de tu archivo de entrada
archivo_salida = 'palabras_comas.txt'  # Nombre del archivo de salida

# Llamar a la función para realizar la conversión
convertir_palabras_a_coma(archivo_entrada, archivo_salida)
