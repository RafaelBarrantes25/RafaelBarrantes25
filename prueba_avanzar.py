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
                fila += ["o"]
                j += 1
            else:
                fila += [tablero[i][j]]
                j += 1
        tablero_final += [fila]
        j = 0
        i += 1

        print(tablero_final)


tablero = [[57, 58, 59, 60, 61, 62, 63, 64], [49, 50, 51, 52, 53, 54, 55, 56], [41, 42, 43, 44, 45, 46, 47, 48], [33, 34, 35, 36, 37, 38, 39, 40], [
    25, 26, 27, 28, 29, 30, 31, 32], [17, 18, 19, 20, 21, 22, 23, 24], [9, 10, 11, 12, 13, 14, 15, 16], [1, 2, 3, 4, 5, 6, 7, 8]]
avanzar_tablero(tablero, 1, 0, [])
