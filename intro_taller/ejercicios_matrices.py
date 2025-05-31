def imprimir_matriz(matriz):
    """
    Imprime matriz
    E: la matriz lista
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


def transpuesta(matriz):
    """
    transpone una matriz
    E: matriz
    S: transpuesta
    R: lista, matriz
    """
    if type(matriz) != list:
        return False

    i = 0
    j = 0
    n = len(matriz)
    m = len(matriz[0])
    lista = []
    fila = []
    while j < m:
        fila = []
        while i < n:
            fila += [matriz[i][j]]
            i += 1
        lista += [fila]
        i = 0
        j += 1
    return lista


def multiplicar_matriz(matriz, matriz_t):
    """
    multiplica matriz
    E: la matriz normal y la transpuesta
    S: una matriz de las multiplicadas
    R: no deberían haber
    """
    if type(matriz) != list or type(matriz_t) != list:
        return False

    i = 0
    j = 0
    n = len(matriz)
    m = len(matriz[0])
    matriz_m = []
    fila = []
    while i < n:
        fila = []
        while j < m:
            fila += [matriz[i][j]*matriz_t[i][j]]
            j += 1
        matriz_m += [fila]
        j = 0
        i += 1
    return matriz_m


matriz_t = transpuesta([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
transp = transpuesta(multiplicar_matriz(
    [[1, 2, 3], [1, 2, 3], [1, 2, 3]], matriz_t))

imprimir_matriz(transp)
