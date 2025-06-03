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
            if type(matriz[i][j]) == str:
                print(matriz[i][j], end=" ")
            else:
                print("▢", end="  ")

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


def escaleras(alto, largo):
    """
    Crea la lista de escaleras
    E: tablero
    S: lista de escaleras
    R: no hay
    """
    número = abs(0.05*(largo*alto))
    lista = []
    while número > 0:
        lista += [random.randint(largo, (largo*alto)-largo*2)]
        número -= 1

    return lista


def escaleras_llegada(lista, largo):
    """
    Crea la lista de escaleras
    E: tablero
    S: lista de escaleras
    R: no hay
    """
    lista2 = []
    número = 0
    while len(lista2) < len(lista):
        lista2 += [lista[número]+random.randint(largo, largo*2)]
        número += 1

    return lista2


def añadir_escaleras(tablero, escal, escal_fin, número):
    tablero_final = []
    fila = []
    i = 0
    j = 0
    n = len(tablero)
    m = len(tablero)

    cuadritos = ["🟥", "🟧", "🟨", "🟩", "🟦", "🟪", "🟫", "⬛", "⬜", "🔳", "🔲", "🆗"]

    while i < n:
        fila = []
        while j < m:
            if type(tablero[i][j]) == str:
                fila += [tablero[i][j]]
                j += 1
            elif tablero[i][j] == escal[número]:
                fila += [cuadritos[número]]
                j += 1
            elif tablero[i][j] == escal_fin[número]:
                fila += [cuadritos[número]]
                j += 1
            else:
                fila += [tablero[i][j]]
                j += 1
        tablero_final += [fila]
        j = 0
        i += 1
    return tablero_final




def serpientes(alto, largo):
    """
    Crea la lista de serpientes
    E: tablero
    S: lista de serpientes
    R: no hay
    """
    número = abs(0.05*(largo*alto))
    lista = []
    while número > 0:
        lista += [random.randint(largo, (largo*alto)-largo*2)]
        número -= 1

    return lista


def serpientes_llegada(lista, largo):
    """
    Crea la lista de serpientes
    E: tablero
    S: lista de serpientes
    R: no hay
    """
    lista2 = []
    número = 0
    while len(lista2) < len(lista):
        lista2 += [lista[número]+random.randint(largo, largo*2)]
        número += 1

    return lista2


def añadir_serpientes(tablero, escal, escal_fin, número):
    tablero_final = []
    fila = []
    i = 0
    j = 0
    n = len(tablero)
    m = len(tablero)

    cuadritos = ["🔴", "🟠", "🟡", "🟢", "🔵", "🟣", "🟤", "⚫", "⚪", "⭕", "⛔", "🔘"]

    while i < n:
        fila = []
        while j < m:
            if type(tablero[i][j]) == str:
                fila += [tablero[i][j]]
                j += 1
            elif tablero[i][j] == escal[número]:
                fila += [cuadritos[número]]
                j += 1
            elif tablero[i][j] == escal_fin[número]:
                fila += [cuadritos[número]]
                j += 1
            else:
                fila += [tablero[i][j]]
                j += 1
        tablero_final += [fila]
        j = 0
        i += 1
    return tablero_final

def avanzar_tablero(tablero, posición_jugador, posición_enemigo, tablero_final,tablero_vacío):
    """
    Avanza al jugador en el tablero
    """
    i = 0
    j = 0
    filas = len(tablero)
    columnas = len(tablero[0])
    fila = []

    while i < filas:
        fila = []
        while j < columnas:

            if tablero_vacío[i][j] == posición_jugador:
                fila += ["ⒶⒶ"]
                j += 1
            elif tablero_vacío[i][j] == posición_enemigo:
                fila += ["XX"]
                j += 1

            else:
                fila += [tablero[i][j]]
                j += 1
        tablero_final += [fila]
        j = 0
        i += 1

    return tablero_final


def verificar_elecciones(elección):
    """
    verifica que las elecciones que hizo sean válidas
    """
    if elección < 10 or elección > 15:
        return False
    else:
        return True


def verificar_eventos_inicio(eventos_inicio, eventos_final,serpientes_inicio,serpientes_final):
    """
    Verifica que los eventos generados no tengan duplicados
    E: la lista de eventos
    S: nueva lista eliminando duplicados
    R: no
    """
    número = 0
    número2 = 1

    while número < len(eventos_inicio)-1:

        while número2 < len(eventos_inicio)-1:
            if eventos_inicio[número] == eventos_inicio[número2]:
                eventos_inicio[número] += 2
                número2 += 1
            else:
                número2 += 1
        número += 1

    número = 0
    número2 = 0

    while número < len(eventos_inicio)-1:

        while número2 < len(eventos_inicio)-1:
            if eventos_inicio[número] == eventos_final[número2]:
                eventos_inicio[número] += 2
                número2 += 1
            else:
                número2 += 1
        número += 1


    número = 0
    número2 = 0

    while número < len(eventos_inicio)-1:

        while número2 < len(eventos_inicio)-1:
            if eventos_inicio[número] == serpientes_inicio[número2]:
                eventos_inicio[número] += 2
                número2 += 1
            else:
                número2 += 1
        número += 1


    número = 0
    número2 = 0

    while número < len(eventos_inicio)-1:

        while número2 < len(eventos_inicio)-1:
            if eventos_inicio[número] == serpientes_final[número2]:
                eventos_inicio[número] += 2
                número2 += 1
            else:
                número2 += 1
        número += 1

    return eventos_inicio


def menú():
    """
    El menú al inicio del juego
    E: ninguna
    S: la opción que escoge
    R: debe escoger la opción correcta
    """

    print("Anarquistas VS Fascistas")

    time.sleep(3)
    print("")
    print("Opciones:\n1. Iniciar juego\n2. Instrucciones\n3. Fuentes consultadas")
    print("")
    time.sleep(1)
    while True:
        elección = input("Escoja una opción: ")
        if elección == "1":
            return True
        if elección == "2":
            print("El juego es una recreación del juego de" \
            "mesa serpientes y escaleras.")
            time.sleep(3)
            print("FALTA ESCRIBIR LAS" \
            "OPCUEOSNWF" \
            "R" \
            "TF4" \
            "ER4G}FERG" \
            "" \
            "YRU" \
            "R6U" \
            "6TFF" \
            "U" \
            "6TI" \
            "6TD" \
            "8R" \
            "7" \
            "6" \
            "F7" \
            "R5" \
            "U" \
            "6TPO" \
            "U" \
            "YTR" \
            "XYH" \
            "" \
            "C57U" \
            "T6" \
            "UJ" \
            "XR" \
            "6" \
            "RXU" \
            "")


def ganar_anarquistas():
    print("Ganaron los anarquistas")

def ganar_fascistas():
    print("Ganaron los fascistas")



def turno_jugador(turno,posición_jugador=0, posición_enemigo=0, tablero=[], escaleras_inicio_finales=[], escaleras_final=[],serpientes_inicio=[],serpientes_final=[],tamaño=0,tablero_vacío=[]):
    """
    Ejecuta el turno del jugador
    E: la posición del jugador y el enemigo, el tablero editado,
    las casillas de serpientes y escaleras, el tamaño del tablero
    y el tablero vacío, solo los números
    S: ejecuta el turno del jugador, entonces lo avanza
    R: no hay
    """
    input("Presione enter para lanzar los dados")
    posiciones = random.randint(1, 4)
    proyectos = random.randint(1, 4)
    eficacia = random.randint(1, 4)

    # Calcula lo que va a avanzar

    print("Va a avanzar "+str(posiciones) + " casillas")

    if proyectos == 1:
        print("Está intentando ejecutar "+str(proyectos)+" proyecto")
    else:
        print("Está intentando ejecutar "+str(proyectos)+" proyectos")

    # Comprueba si los proyectos fracasan o no
    if eficacia % 2 == 0:
        print("Los proyectos fueron exitosos, se va a mover " +
                str(proyectos)+" casillas extra y los fascistas van a retroceder")
        posición_jugador += posiciones+proyectos
        posición_enemigo -= proyectos

    else:
        print("Los proyectos fracasaron, no hay bonificaciones")
        posición_jugador += posiciones

    # Para que la posición no se vaya a números negativos
    if posición_jugador < 0:
        posición_jugador = 0
    if posición_enemigo < 0:
        posición_enemigo = 0
    if posición_jugador == posición_enemigo:
        print("Qué mala suerte, cayó en una casilla fascista.")
        print("Retrocede un espacio.")
        posición_jugador -= 1

    # comprueba si cayó en una casilla de escaleras o no y lo avanza si sí

    revisión = 0

    while revisión < len(escaleras_inicio_finales)-1:

        if posición_jugador == escaleras_inicio_finales[revisión]:
            print("")
            print("")
            print("Cayó en una escalera")
            print("Va a subir a la parte de arriba")
            time.sleep(1)
            tablero_3 = avanzar_tablero(
            tablero, posición_jugador, posición_enemigo, tablero_final=[],tablero_vacío=tablero_vacío)
            imprimir_tablero(invertir_tablero(tablero_3))
            print("")
            print("")
            posición_jugador = escaleras_final[revisión]
            time.sleep(1)
        else:
            revisión += 1



    revisión = 0

    while revisión < len(serpientes_final)-1:

        if posición_jugador == serpientes_final[revisión]:
            print("")
            print("")
            print("Cayó en una serpiente")
            print("Va a bajar a la cola")
            time.sleep(1)
            tablero_3 = avanzar_tablero(tablero, posición_jugador, posición_enemigo, tablero_final=[],tablero_vacío=tablero_vacío)
            imprimir_tablero(invertir_tablero(tablero_3))
            print("")
            print("")
            posición_jugador = serpientes_inicio[revisión]
            time.sleep(1)
        else:
            revisión += 1


    if posición_jugador >= tamaño:
        posición_jugador = tamaño
        tablero_2 = avanzar_tablero(
        tablero, posición_jugador, posición_enemigo, tablero_final=[],tablero_vacío=tablero_vacío)
        imprimir_tablero(invertir_tablero(tablero_2))
        return ganar_anarquistas()


    tablero_2 = avanzar_tablero(
        tablero, posición_jugador, posición_enemigo, tablero_final=[],tablero_vacío=tablero_vacío)
    imprimir_tablero(invertir_tablero(tablero_2))

    turno += 1
    return juego(turno,tablero_nuevo=[], posición_jugador=0, posición_enemigo=0, tablero=[], escaleras_inicio_finales=[], escaleras_final=[],serpientes_inicio=[],serpientes_final=[],tamaño=0,tablero_vacío=[])






def turno_enemigo(turno,tablero_nuevo=[], posición_jugador=0, posición_enemigo=0, tablero=[], escaleras_inicio_finales=[], escaleras_final=[],serpientes_inicio=[],serpientes_final=[],tamaño=0,tablero_vacío=[]):

    input("Presione enter para el turno de los fascistas")
    posiciones_f = random.randint(1, 4)
    proyectos_f = random.randint(1, 4)
    eficacia_f = random.randint(1, 4)

    print("Va a avanzar "+str(posiciones_f) + " casillas")

    if proyectos_f == 1:
        print("Está intentando ejecutar "+str(proyectos_f)+" proyecto")
    else:
        print("Está intentando ejecutar "+str(proyectos_f)+" proyectos")

    if eficacia_f % 2 == 0:
        print("Los proyectos fueron exitosos, se va a mover " +
                str(proyectos_f)+" casillas extra y los anarquistas van a retroceder")
        posición_enemigo += posiciones_f+proyectos_f
        posición_jugador -= proyectos_f
    else:
        print("Los proyectos fracasaron, no hay bonificaciones")
        posición_enemigo += posiciones_f

    if posición_jugador < 0:
        posición_jugador = 0
    if posición_enemigo < 0:
        posición_enemigo = 0
    if posición_jugador == posición_enemigo:
        print("Buena suerte, los fascistas cayeron en una casilla anarquista.")
        print("Retroceden un espacio.")
        posición_enemigo -= 1

    revisión = 0
    while revisión < len(escaleras_inicio_finales)-1:

        if posición_enemigo == escaleras_inicio_finales[revisión]:
            print("")
            print("")
            print("Cayó en una escalera")
            print("Va a subir a la parte de arriba")
            time.sleep(1)
            tablero_3 = avanzar_tablero(
            tablero, posición_jugador, posición_enemigo, tablero_final=[],tablero_vacío=tablero_vacío)
            imprimir_tablero(invertir_tablero(tablero_3))
            print("")
            print("")
            posición_enemigo = escaleras_final[revisión]
            time.sleep(1)
        else:
            revisión += 1



    revisión = 0

    while revisión < len(serpientes_final)-1:

        if posición_enemigo == serpientes_final[revisión]:
            print("")
            print("")
            print("Cayó en una serpiente")
            print("Va a bajar a la cola")
            time.sleep(1)
            tablero_3 = avanzar_tablero(
            tablero, posición_jugador, posición_enemigo, tablero_final=[],tablero_vacío=tablero_vacío)
            imprimir_tablero(invertir_tablero(tablero_3))
            print("")
            print("")
            posición_enemigo = serpientes_inicio[revisión]-1
            time.sleep(1)
        else:
            revisión += 1

    if posición_enemigo >= tamaño:
        posición_enemigo = tamaño
        tablero_3 = avanzar_tablero(
        tablero, posición_jugador, posición_enemigo, tablero_final=[],tablero_vacío=tablero_vacío)
        imprimir_tablero(invertir_tablero(tablero_3))
        return ganar_fascistas()

    tablero_3 = avanzar_tablero(
        tablero, posición_jugador, posición_enemigo, tablero_final=[],tablero_vacío=tablero_vacío)
    imprimir_tablero(invertir_tablero(tablero_3))


    turno += 1
    return juego(turno, tablero_3, posición_jugador, posición_enemigo, tablero, escaleras_inicio_finales, escaleras_final,serpientes_inicio,serpientes_final,tamaño,tablero_vacío)











def iniciar():
    """
    Inicia el juego
    E: el turno
    S: inicia el juego
    R: ninguna
    """
   
    largo = input(
        "¿Cuál será el largo del tablero? (Número entre 10 y 15):\n")
    alto = input(
        "¿Cuál será el alto del tablero? (Número entre 10 y 15):\n")

    if verificar_numéricos(largo) and verificar_numéricos(alto):
        largo = int(largo)
        alto = int(alto)
    else:
        print("Eso no es un número")
        return iniciar()

    if verificar_elecciones(largo) == False or verificar_elecciones(alto) == False:
        print("El número debe estar entre 10 y 15")
        return iniciar()
    else:
        tablero = crear_matriz(largo, alto)

    tablero_vacío = tablero


    escaleras_inicio = escaleras(largo, alto)
    escaleras_final = escaleras_llegada(escaleras_inicio, largo)

    serpientes_inicio = serpientes(largo, alto)
    serpientes_final = serpientes_llegada(serpientes_inicio, largo)

    cinco_verificaciones = 0
    while cinco_verificaciones != 5:

        escaleras_inicio_finales = verificar_eventos_inicio(
            escaleras_inicio, escaleras_final,serpientes_inicio,serpientes_final)
        cinco_verificaciones += 1

        # Pone las escaleras
    número = 0
    tablero4 = []
    while número < len(escaleras_inicio_finales):
        tablero4 = añadir_escaleras(
            tablero, escaleras_inicio_finales, escaleras_final, número)
        número += 1
        tablero = tablero4

    #pone las serpientes
    número = 0
    tablero4 = []
    while número < len(serpientes_inicio):
        tablero4 = añadir_serpientes(
            tablero, serpientes_inicio, serpientes_final, número)
        número += 1
        tablero = tablero4

    imprimir_tablero(invertir_tablero(tablero))

    return tablero


def juego(turno, tablero_nuevo=[], posición_jugador=0, posición_enemigo=0, escaleras_inicio_finales=[], escaleras_final=[],serpientes_inicio=[],serpientes_final=[],largo=0,alto=0,tablero_vacío=[]):
    """
    Ejecuta el juego
    """
    if turno == 0:
        posición_jugador = 0
        posición_enemigo = 0

        tamaño = largo*alto

        tablero = iniciar()
        tablero_vacío = crear_matriz(largo,alto)
        tablero_vacío = invertir_tablero(tablero_vacío)
        turno = 1

    if turno > 0:
        while posición_jugador < 100 and posición_enemigo < 100:
            
            turno_jugador(turno,posición_jugador, posición_enemigo,tablero, escaleras_inicio_finales, escaleras_final,serpientes_inicio,serpientes_final,tamaño,tablero_vacío)
            

juego(0)