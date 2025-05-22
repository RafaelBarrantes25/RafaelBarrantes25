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

def iniciar(turno):
    """
    Inicia el juego
    E: el turno
    S: inicia el juego
    R: ninguna
    """
    
    #Poner inputs para que el usuario escoja el tamaño del
    #tablero y validarlos
    tablero = crear_matriz(8,8)
    imprimir_tablero(tablero)

iniciar(0)