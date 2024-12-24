from collections import deque

# Movimientos posibles del caballero
movimientos_caballero = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

def movimientos_validos(x, y, n):
    # Genera movimientos válidos dentro de los límites del tablero
    return [(x+dx, y+dy) for dx, dy in movimientos_caballero if 0 <= x+dx < n and 0 <= y+dy < n]

def caballero_tablero(pos_inicio, pos_meta, n):
    visitados = set()
    cola = deque([(pos_inicio, 0)])  # (posición, pasos)
    
    while cola:
        (x, y), pasos = cola.popleft()
        if (x, y) == pos_meta:
            return pasos
        if (x, y) in visitados:
            continue
        visitados.add((x, y))
        for nuevo_x, nuevo_y in movimientos_validos(x, y, n):
            cola.append(((nuevo_x, nuevo_y), pasos + 1))
    return -1  # No se puede llegar

# Ejecutar
inicio = (0, 0)
meta = (7, 7)
tamaño_tablero = 8
pasos = caballero_tablero(inicio, meta, tamaño_tablero)
print(f"El caballero llega en {pasos} movimientos.")
