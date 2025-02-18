from collections import deque

# Representación de los estados como (jarra3, jarra5)
estado_inicial = (0, 0)
meta = 4

def movimientos_validos(estado):
    jarra3, jarra5 = estado
    capacidad_3, capacidad_5 = 3, 5
    return [
        (capacidad_3, jarra5),  # Llenar la jarra de 3
        (jarra3, capacidad_5),  # Llenar la jarra de 5
        (0, jarra5),            # Vaciar la jarra de 3
        (jarra3, 0),            # Vaciar la jarra de 5
        (max(0, jarra3 - (capacidad_5 - jarra5)), min(capacidad_5, jarra5 + jarra3)),  # Verter de 3 a 5
        (min(capacidad_3, jarra3 + jarra5), max(0, jarra5 - (capacidad_3 - jarra3)))   # Verter de 5 a 3
    ]

def resolver():
    visitados = set()
    cola = deque([(estado_inicial, [])])
    
    while cola:
        (estado_actual, pasos) = cola.popleft()
        if meta in estado_actual:
            return pasos + [estado_actual]
        if estado_actual in visitados:
            continue
        visitados.add(estado_actual)
        for nuevo_estado in movimientos_validos(estado_actual):
            if nuevo_estado not in visitados:
                cola.append((nuevo_estado, pasos + [estado_actual]))
    return None

# Ejecutar
solucion = resolver()
for paso in solucion:
    print(paso)
