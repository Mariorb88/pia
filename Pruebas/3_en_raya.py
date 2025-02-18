import os
import random

NOMBRE_USU = os.getlogin()
NOMBRE_MAQUINA = 'Skynet'
CARACTER_USU = 'O'
CARACTER_MAQUINA = 'X'

v_jugador_actual = ' '
v_finalizado = False

v_tablero = [[' ' for i in range(3)] for j in range(3)]
v_inputs_validos = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3') # Tupla para verificar si es coord valida


def pinta_tablero():
    print('3 '+str(v_tablero[2]), end='\n')
    print('2 '+str(v_tablero[1]), end='\n')
    print('1 '+str(v_tablero[0]), end='\n')
    print('    a    b    c', end='\n')


def asigna_coordenada(p_fila, p_columna, p_usuario) -> bool:
    v_retorno = False
    if p_usuario == NOMBRE_USU:
        v_caracter = CARACTER_USU
        if v_tablero[p_fila][p_columna] == ' ':
            v_tablero[p_fila][p_columna] = v_caracter
            v_retorno = True
        else:
            print('La coordenada ya ha sido seleccionada. Introduzca otra.')
            v_retorno = False
    else:
        v_caracter = CARACTER_MAQUINA
        v_espacio_libre = False

        while not v_espacio_libre:
            v_fila = random.randint(0, 2)
            v_columna = random.randint(0, 2)
            if v_tablero[v_fila][v_columna] == ' ':
                v_tablero[v_fila][v_columna] = v_caracter
                v_espacio_libre = True
                v_retorno = True

    return v_retorno


def comprobar_fin(p_caracter) -> bool:
    if (v_tablero[0][0] == p_caracter and v_tablero[1][0] == p_caracter and v_tablero[2][0] == p_caracter) or (v_tablero[0][1] == p_caracter and v_tablero[1][1] == p_caracter and v_tablero[2][1] == p_caracter) or (v_tablero[0][2] == p_caracter and v_tablero[1][2] == p_caracter and v_tablero[2][2] == p_caracter) or (v_tablero[0][0] == p_caracter and v_tablero[0][1] == p_caracter and v_tablero[0][2] == p_caracter) or (v_tablero[1][0] == p_caracter and v_tablero[1][1] == p_caracter and v_tablero[1][2] == p_caracter) or (v_tablero[2][0] == p_caracter and v_tablero[2][1] == p_caracter and v_tablero[2][2] == p_caracter) or (v_tablero[0][2] == p_caracter and v_tablero[1][1] == p_caracter and v_tablero[2][0] == p_caracter) or (v_tablero[0][0] == p_caracter and v_tablero[1][1] == p_caracter and v_tablero[2][2] == p_caracter):
        return True
    else:
        return False


def tablero_lleno() -> bool:
    if v_tablero[0][0] != ' ' and v_tablero[0][1] != ' ' and v_tablero[0][2] != ' ' and v_tablero[1][0] != ' ' and v_tablero[1][1] != ' ' and v_tablero[1][2] != ' ' and v_tablero[2][0] != ' ' and v_tablero[2][1] != ' ' and v_tablero[2][2] != ' ':
        return True
    else:
        return False


def pide_coordenada() -> bool:
    v_coordenada_correcta = False
    while not v_coordenada_correcta:
        v_coordenada = input('Introduzca una coordenada: ').upper()

        if v_coordenada in v_inputs_validos:
            
            v_columna = ord(v_coordenada[:1]) - ord('A')
            v_fila = int(v_coordenada[1:])-1
            v_jugador_actual = NOMBRE_USU
            
            if asigna_coordenada(v_fila, v_columna, v_jugador_actual):
                v_coordenada_correcta = True
                v_fin = comprobar_fin(CARACTER_USU)
                if not v_fin:
                    v_jugador_actual = NOMBRE_MAQUINA
                    if asigna_coordenada('', '', v_jugador_actual):
                        v_coordenada_correcta = True
                        v_fin = comprobar_fin(CARACTER_MAQUINA)
                        
                    if v_fin:
                        print('Se acabó! Ha ganado ' + v_jugador_actual)
                        return v_fin
            if tablero_lleno() :
                print('todos completos')
                v_fin = True
                    
        else:
            print('Formato incorrecto, la coordenada debe ser del tipo a1, b2...')
    return v_fin




pinta_tablero()
while not v_finalizado:
    v_finalizado = pide_coordenada()
    pinta_tablero()