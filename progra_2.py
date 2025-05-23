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

    while contador_filas < largo:
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
    texto = elección
    while len(texto) > 0:

        if texto[0] != "0" and texto[0] != "1" and texto[0] != "2" and texto[0] != "3" and texto[0] != "4" and texto[0] != "5" and texto[0] != "6" and texto[0] != "7" and texto[0] != "8" and texto[0] != "9":
            return False
        else:
            texto = texto[1:]
    return True



def verificar_elecciones(elección):
    """
    verifica que las elecciones que hizo sean válidas
    """
    pass


def iniciar(turno):
    """
    Inicia el juego
    E: el turno
    S: inicia el juego
    R: ninguna
    """

    largo = input("¿Cuál será el largo del tablero? (Número entre 5 y 25):\n")
    alto = input("¿Cuál será el alto del tablero? (Número entre 5 y 25):\n")
    tablero = crear_matriz(largo, alto)
    imprimir_tablero(tablero)


iniciar(0)
