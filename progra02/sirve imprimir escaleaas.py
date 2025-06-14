import random


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
    
    while i < n:
        fila = []
        while j < m:
            if type(tablero[i][j]) == str:
                fila += [tablero[i][j]]
                j += 1
            elif tablero[i][j] == escal[número]:
                fila += [str(número)+"/"]
                j += 1
            elif tablero[i][j] == escal_fin[número]:
                fila += [str(número)+"|"]
                j += 1
            else:
                fila += [tablero[i][j]]
                j += 1
        tablero_final += [fila]
        j = 0
        i += 1
    return tablero_final


def avanzar_tablero(tablero, posición_jugador, posición_enemigo, tablero_final):
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

            if tablero[i][j] == posición_jugador:
                fila += ["ⒶⒶ"]
                j += 1
            elif tablero[i][j] == posición_enemigo:
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
    if elección < 5 or elección > 15:
        return False
    else:
        return True


def iniciar(turno, tablero_nuevo=[], posición_jugador=0, posición_enemigo=0, tablero=[],escaleras_inicio=[],escaleras_final=[]):
    """
    Inicia el juego
    E: el turno
    S: inicia el juego
    R: ninguna
    """
    if turno == 0:
        turno = 0
        tablero = tablero_nuevo

        if tablero == tablero_nuevo:
            largo = input(
                "¿Cuál será el largo del tablero? (Número entre 5 y 15):\n")
            alto = input(
                "¿Cuál será el alto del tablero? (Número entre 5 y 15):\n")

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
                tablero = crear_matriz(largo, alto)
                
                posición_jugador = 0
                posición_enemigo = 0

        escaleras_inicio = escaleras(largo, alto)
        escaleras_final = escaleras_llegada(escaleras_inicio, largo)
                #Pone las escaleras
        número = 0
        tablero4 = []
        while número < len(escaleras_inicio):
            tablero4 = añadir_escaleras(
                tablero, escaleras_inicio, escaleras_final, número)
            número += 1
            tablero = tablero4

        imprimir_tablero(invertir_tablero(tablero))
            






    turno = 1

    while turno == 1:
        input("Presione enter para lanzar los dados")
        posiciones = random.randint(1, 4)
        proyectos = random.randint(1, 4)
        eficacia = random.randint(1, 4)

        #Calcula lo que va a avanzar


        print("Va a avanzar "+str(posiciones) + " casillas")

        if proyectos == 1:
            print("Está intentando ejecutar "+str(proyectos)+" proyecto")
        else:
            print("Está intentando ejecutar "+str(proyectos)+" proyectos")

        #Comprueba si los proyectos fracasan o no
        if eficacia % 2 == 0:
            print("Los proyectos fueron exitosos, se va a mover " +
                  str(proyectos)+" casillas extra y los fascistas van a retroceder")
            posición_jugador += posiciones+proyectos
            posición_enemigo -= proyectos

        else:
            print("Los proyectos fracasaron, no hay bonificaciones")
            posición_jugador += posiciones

        #Para que la posición no se vaya a números negativos
        if posición_jugador < 0:
            posición_jugador = 0
        if posición_enemigo < 0:
            posición_enemigo = 0
        if posición_jugador == posición_enemigo:
            print("Qué mala suerte, cayó en una casilla fascista.")
            print("Retrocede un espacio.")
            posición_jugador -= 1






        #comprueba si cayó en una casilla de escaleras o no y lo avanza si sí

        revisión = 0

        while revisión < len(escaleras_inicio)-1:
            
            if posición_jugador == escaleras_inicio[revisión]:
                posición_jugador = escaleras_final[revisión]
            else:
                revisión += 1



        tablero_2 = avanzar_tablero(
            tablero, posición_jugador, posición_enemigo, tablero_final=[])
        imprimir_tablero(invertir_tablero(tablero_2))

        turno = 2










    while turno == 2:
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

        tablero_3 = avanzar_tablero(
            tablero, posición_jugador, posición_enemigo, tablero_final=[])
        imprimir_tablero(invertir_tablero(tablero_3))

        return iniciar(1, tablero_3, posición_jugador, posición_enemigo, tablero,escaleras_inicio,escaleras_final)


iniciar(0)
