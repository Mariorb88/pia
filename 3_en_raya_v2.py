import os
import random

NOMBRE_USU = os.getlogin()  # obtengo el nombre de usuario del sistema operativo
NOMBRE_MAQUINA = 'Skynet'
CARACTER_USU = 'O'
CARACTER_MAQUINA = 'X'

v_jugador_actual = ' '
v_finalizado = False
v_tablero = [[' ' for i in range(3)] for j in range(3)]  # genero el tablero

# tupla para verificar si es coord válida
v_inputs_validos = ('A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3')


def pinta_tablero():  # procedimiento que pinta el tablero
    print('3 ' + str(v_tablero[2]), end='\n')
    print('2 ' + str(v_tablero[1]), end='\n')
    print('1 ' + str(v_tablero[0]), end='\n')
    print('    a    b    c', end='\n')
    print('-------------------------------------------')


# función que asigna posición en el tablero
def asigna_coordenada(p_fila, p_columna, p_usuario) -> bool:
    v_retorno = False
    if p_usuario == NOMBRE_USU:
        v_caracter = CARACTER_USU
        if v_tablero[p_fila][p_columna] == ' ':
            v_tablero[p_fila][p_columna] = v_caracter
            v_retorno = True
        else:
            print('La coordenada ya ha sido seleccionada. Introduzca otra.')
    else:
        v_caracter = CARACTER_MAQUINA
        v_espacio_libre = False
        # en el caso de la máquina, si me viene la coordenada, la asigno (primer movimiento), si no, la calculo de manera aleatoria
        if p_fila is not None and p_columna is not None:
            if v_tablero[p_fila][p_columna] == ' ':
                v_tablero[p_fila][p_columna] = v_caracter
                v_retorno = True
        else:
            while not v_espacio_libre:
                v_fila = random.randint(0, 2)
                v_columna = random.randint(0, 2)
                if v_tablero[v_fila][v_columna] == ' ':
                    v_tablero[v_fila][v_columna] = v_caracter
                    v_espacio_libre = True
                    v_retorno = True

    return v_retorno

# función que comprueba si la jugada es ganadora
def comprobar_ganador(p_caracter) -> bool:
    for i in range(3):
        if all([v_tablero[i][j] == p_caracter for j in range(3)]) or all([v_tablero[j][i] == p_caracter for j in range(3)]):
            return True
    if v_tablero[0][0] == p_caracter and v_tablero[1][1] == p_caracter and v_tablero[2][2] == p_caracter:
        return True
    if v_tablero[0][2] == p_caracter and v_tablero[1][1] == p_caracter and v_tablero[2][0] == p_caracter:
        return True
    return False

# función que comprueba si el tablero está lleno
def tablero_lleno() -> bool:
    return all(v_tablero[i][j] != ' ' for i in range(3) for j in range(3))

# función que realiza la jugada
def pide_coordenada() -> bool:
    v_coordenada_correcta = False
    v_fin = False
    while not v_coordenada_correcta:
        v_coordenada = input('Introduzca una coordenada: ').upper()

        if v_coordenada in v_inputs_validos:

            # obtengo la columna, pasando el primer caracter a números (a,b,c)->(0,1,2)
            v_columna = ord(v_coordenada[:1]) - ord('A')
            # obtengo la fila restando 1 al número de la posición 2 de la cadena
            v_fila = int(v_coordenada[1:])-1
            v_jugador_actual = NOMBRE_USU

            v_coordenada_correcta = asigna_coordenada(
                v_fila, v_columna, v_jugador_actual)  # juega humano

            if v_coordenada_correcta:
                v_fin = comprobar_ganador(CARACTER_USU)  # si gana se acabó

                if not v_fin and not tablero_lleno():
                    v_jugador_actual = NOMBRE_MAQUINA
                    v_coordenada_correcta = asigna_coordenada(
                        None, None, v_jugador_actual)
                    v_fin = comprobar_ganador(
                        CARACTER_MAQUINA)  # si gana se acabó

                if v_fin:
                    print('Se acabó! Ha ganado ' + v_jugador_actual)
                else:
                    if tablero_lleno():
                        print('Empate!!')
                        v_fin = True

        else:
            print('Formato incorrecto, la coordenada debe ser del tipo a1, b2...')
    return v_fin


# inicio del programa, lo primero es la jugada de la máquina en el centro y pintar el tablero, después generamos tiradas hasta que uno gane o no haya posiciones libres
v_dummy = asigna_coordenada(1, 1, NOMBRE_MAQUINA)
pinta_tablero()
while not v_finalizado:
    v_finalizado = pide_coordenada()
    pinta_tablero()
