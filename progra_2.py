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

    while contador_filas < alto:
        lista += [["▢"]*largo]
        contador_filas += 1
    return lista


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



def avanzar_tablero(tablero,posiciones,actual):
    """
    Avanza al jugador en el tablero
    """


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
            imprimir_tablero(tablero)
            posición_jugador = 0
            posición_enemigo = 0
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
            posiciones_finales = posiciones+proyectos
        else:
            print("Los proyectos fracasaron, no hay bonificaciones")
            posiciones_finales = posiciones

        última_fila = len(tablero)-1

        



iniciar(0)
