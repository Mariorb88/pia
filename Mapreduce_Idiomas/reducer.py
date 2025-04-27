# reducer.py

def main():
    try:
        with open("entrada_reducer.txt", "r", encoding="utf-8") as entrada, open("salida_reducer.txt", "w", encoding="utf-8") as salida: # Abrimos el archivo de entrada y salida

            letra_actual = None  # Variable para almacenar la letra actual
            contador = 0  # Contador para sumar los valores de la misma letra

            for linea in entrada: # Iteramos sobre cada línea del archivo de entrada
                letra, valor = linea.strip().split('\t') # Separamos la letra y el valor
                valor = int(valor)

                if letra == letra_actual:
                    # Si es la misma letra que la anterior, sumamos
                    contador += valor
                else:
                    if letra_actual is not None:
                        # Guardamos la letra anterior y su contador
                        salida.write(f"{letra_actual}\t{contador}\n")
                    # Actualizamos la letra actual y su contador
                    letra_actual = letra
                    contador = valor

            # Guardamos la última letra después de terminar el bucle
            if letra_actual is not None:
                salida.write(f"{letra_actual}\t{contador}\n")

        print("Archivo 'salida_reducer.txt' creado correctamente.")

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'entrada_reducer.txt'. Asegúrate de ejecutar primero 'ordenar.py'.")

if __name__ == "__main__":
    main()
