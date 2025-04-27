# mapper.py
import unicodedata
import sys
import os

def normalizar_letra(letra): # Normaliza la letra a mayúscula y elimina acentos
    letra = letra.upper() # Convertir a mayúscula
    if letra == 'Ñ': # Verifica si la letra es Ñ
        return 'Ñ' # No modificar la Ñ
    letra = unicodedata.normalize('NFD', letra) # Descomponer caracteres acentuados
    letra = ''.join([c for c in letra if unicodedata.category(c) != 'Mn']) # Eliminar acentos
    return letra

def es_letra(c):
    return c.isalpha() # Verifica si el carácter es una letra

def main():
    if len(sys.argv) != 2: # Verifica que se haya pasado el nombre del archivo como argumento
        print("Uso: python mapper.py <archivo_entrada.txt>")
        sys.exit(1)

    archivo_entrada = sys.argv[1] # Nombre del archivo de entrada

    if not os.path.isfile(archivo_entrada): # Verifica si el archivo existe
        print(f"Error: El archivo '{archivo_entrada}' no existe.")
        sys.exit(1)

    with open(archivo_entrada, "r", encoding="utf-8") as entrada, open("salida_mapper.txt", "w", encoding="utf-8") as salida: # Abre el archivo de entrada y crea el archivo de salida
        for linea in entrada:
            for caracter in linea:
                if es_letra(caracter): # Verifica si el carácter es una letra
                    letra_normalizada = normalizar_letra(caracter) # Normaliza la letra
                    salida.write(f"{letra_normalizada}\t1\n") # Escribe la letra normalizada y el conteo (1) en el archivo de salida

if __name__ == "__main__":
    main()
