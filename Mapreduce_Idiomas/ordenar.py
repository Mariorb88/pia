# ordenar.py
import sys
import locale

def clave_ordenacion(linea):
    letra = linea.split('\t')[0]
    # Reglas de ordenamiento: la Ñ debe ir justo después de la N
    # Truco: para comparar, cambiamos "Ñ" por "N~", así se ordena bien
    if letra == 'Ñ':
        return 'N~'
    return letra

def main():
    try:
        with open("salida_mapper.txt", "r", encoding="utf-8") as entrada:
            lineas = entrada.readlines()
        
        # Ordenamos usando la clave personalizada
        lineas.sort(key=clave_ordenacion)

        with open("entrada_reducer.txt", "w", encoding="utf-8") as salida:
            salida.writelines(lineas)

        print("Archivo 'entrada_reducer.txt' creado correctamente.")

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'salida_mapper.txt'. Asegúrate de ejecutar primero 'mapper.py'.")

if __name__ == "__main__":
    main()
