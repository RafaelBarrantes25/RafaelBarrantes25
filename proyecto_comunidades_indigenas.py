import random

def solicitar_comunidades():
    """
    Genera un número aleatorio de comunidades
    """
    eleccion = input("¿Quiere comunidades?:\n1: Sí\n2. No\n")
    if eleccion != "1" and eleccion != "2":
        return "Error 0: Esa no es una opción"
    elif eleccion == "2":
        return "Está bien\nFin del juego"
    else:
        return generar_comunidades()



def crear_comunidad(numero, extra):
    """
    crea comunidad
    E: número
    S: comunidad
    R: ninguna
    """
    nombre = "Comunidad " + str(extra)
    acervo = random.randint(5, 10)
    autonomia = random.randint(5, 10)
    return [nombre, acervo, autonomia]


def generar_comunidades():
    numero = random.randint(5, 9)
    return generar_comunidades_aux(numero,extra=1)


def generar_comunidades_aux(numero, lista=[],extra=1):
    if extra == 0:
        extra = 0
    if numero == 0:
        return lista
    else:
        lista.append(crear_comunidad(numero,extra))
        return generar_comunidades_aux(numero-1,lista,extra+1)


print(generar_comunidades())
