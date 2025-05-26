import random
import time

def crear_matriz(largo, alto):
    """
    Crea una matriz vacía según el largo y alto
    E: largo y alto, números int
    S: matriz 
    R: int
    """
    if type(largo) != int or type(alto) != int:
        return False
    contador_filas = 0
    lista = []
    tablero = []
    número = 1
    contador_columnas = 0
    while contador_filas < alto:
        lista = []
        while contador_columnas < largo:
            lista += [número]
            número += 1
            contador_columnas += 1
        tablero += [lista]
        contador_columnas = 0
        contador_filas += 1
    return tablero


def invertir_tablero(tablero):
    """
    invierte el orden de las listas, así se ve como debería
    E: el tablero
    S: el tablero con las listas invertidas
    R: no
    """
    tablero_nuevo = []
    número = len(tablero)-1
    while len(tablero_nuevo) != len(tablero):
        while número > -1:
            tablero_nuevo += [tablero[número]]
            número -= 1
    return tablero_nuevo


def imprimir_tablero(matriz):
    """
    Imprime el tablero
    E: la matriz del tablero
    S: la matriz pero en forma de str para imprimir
    R: no deberían haber...
    """
    if type(matriz) != list:
        return False

    i = 0
    j = 0
    n = len(matriz)
    m = len(matriz[0])

    while i < n:
        while j < m:
            if matriz[i][j] < 10:
                print(matriz[i][j], end="  ")
            else:
                print(matriz[i][j], end=" ")

            j += 1
        j = 0
        i += 1
        print()

    while i < n:
        while j < m:
            print(matriz[i][j], end=" ")
            j += 1
        j = 0
        i += 1
        print("")


def verificar_numéricos(elección):
    """
    verifica que un string contenga únicamente números
    E: string
    S: True o False
    R: no deberían haber
    """
    if elección == "":
        return False
    texto = elección
    while len(texto) > 0:

        if texto[0] != "0" and texto[0] != "1" and texto[0] != "2" and texto[0] != "3" and texto[0] != "4" and texto[0] != "5" and texto[0] != "6" and texto[0] != "7" and texto[0] != "8" and texto[0] != "9":
            return False
        else:
            texto = texto[1:]
    return True



def avanzar_tablero(tablero,posición_jugador,posición_enemigo,tablero_final):
    """
    Avanza al jugador en el tablero
    """
    i = 0
    j = 0
    filas = len(tablero)
    columnas = len(tablero[0])
    fila = []

    while i < filas:
        while j < columnas:
            if tablero[i][j] == posición_jugador:
                fila += [tablero[i][0:j] + "o" + tablero[i][j:]]
    print(fila)
       



def verificar_elecciones(elección):
    """
    verifica que las elecciones que hizo sean válidas
    """
    if elección < 5 or elección > 25:
        return False
    else:
        return True


def iniciar(turno,tablero_nuevo=[]):
    """
    Inicia el juego
    E: el turno
    S: inicia el juego
    R: ninguna
    """
    turno = 0
    tablero = tablero_nuevo

    if tablero == tablero_nuevo:
        largo = input("¿Cuál será el largo del tablero? (Número entre 5 y 25):\n")
        alto = input("¿Cuál será el alto del tablero? (Número entre 5 y 25):\n")

        if verificar_numéricos(largo) and verificar_numéricos(alto):
            largo = int(largo)
            alto = int(alto)
        else:
            print("Eso no es un número")
            return iniciar(0)
        
        if verificar_elecciones(largo) == False or verificar_elecciones(alto) == False:
            print("El número debe estar entre 5 y 25")
            return iniciar(0)
        else:
            tablero = crear_matriz(largo,alto)
            imprimir_tablero(invertir_tablero(tablero))
            posición_jugador = -1
            posición_enemigo = -1
    if turno == 0:
        input("Presione enter para lanzar los dados")
        posiciones = random.randint(1,4)
        proyectos = random.randint(1,4)
        eficacia = random.randint(1,4)
        posiciones_finales = 0
        time.sleep(1.5)
        print("Va a avanzar "+str(posiciones)+ " casillas")
        time.sleep(1.5)
        if proyectos == 1:
            print("Está intentando ejecutar "+str(proyectos)+" proyecto")
        else:
            print("Está intentando ejecutar "+str(proyectos)+" proyectos")
        time.sleep(1.5)
        if eficacia %2 == 0:
            print("Los proyectos fueron exitosos, se va a mover "+str(eficacia)+" casillas extra y los fascistas van a retroceder")
            posición_jugador += posiciones+proyectos
        else:
            print("Los proyectos fracasaron, no hay bonificaciones")
            posición_jugador += posiciones
        
        tablero_2 = avanzar_tablero(tablero,posición_jugador,posición_enemigo,tablero_final=[])
        print(tablero_2)
        



iniciar(0)
