def es_vocal(caracter):
    vocales = "aeiouAEIOU"
    return caracter in vocales


v_palabra = str(input('Indique una palabra: ')).upper()


for letra in v_palabra:
    if not es_vocal(letra):
        print(letra)