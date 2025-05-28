#!/usr/bin/env python

import sys

contador = 0
palabra_anterior = None

for linea in sys.stdin:
    linea = linea.strip()
    lista = linea.split("\t")
    palabra = lista[0]
    #apariciones = lista[1]
    #palabra, apariciones = linea.split("\t")

    if palabra_anterior == None:
        palabra_anterior = palabra
    

    if palabra == palabra_anterior:
        contador += 1

    else:
        print(palabra_anterior, "\t", contador)
        palabra_anterior = palabra
        contador = 1

print(palabra_anterior, "\t", contador)