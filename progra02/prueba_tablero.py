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
    fila = []
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


lista = crear_matriz(7, 7)
lista_inv = invertir_tablero(lista)
imprimir_tablero(lista_inv)
