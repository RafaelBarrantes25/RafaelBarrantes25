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

def imprimir_valores():
    #Obtiene la lista de valores y la pasa
    return imprimir_valores_aux(generar_comunidades(),"",[])



def imprimir_valores_aux(lista, respuesta,lista2):
    #Imprime las comunidades y sus valores
    if len(lista) == 0:
        print(respuesta)
        return verificar_valores(lista2,[])
    else:
        return imprimir_valores_aux(lista[1:],respuesta+str(lista[0][0])+": "+"Acervo: "+str(lista[0][1])+" "+"Autonomía: "+str(lista[0][2])+"\n",lista2+[lista[0]])


def verificar_valores(lista2,lista3):
    if len(lista2) == 0:
        número = random.randint(0,len(lista3)-1)
        número2 = random.randint(0,3)
        restar = [lista3[número][0],lista3[número][1]-número2,lista3[número][2]-número2]
        return restar_valores(lista3,restar,[])
    elif lista2[0][1] == 0 or lista2[0][2] == 0:
        return False
    else:
        return verificar_valores(lista2[1:],lista3+[lista2[0]])

def restar_valores(lista1,restar,lista2):
    if len(lista1) == 0:
        return imprimir_valores_aux(lista2,"",[])
    elif lista1[0][0] == restar[0]:
        return restar_valores(lista1[1:],restar,[restar]+lista2)
    else:
        return restar_valores(lista1[1:],restar,[lista1[0]]+lista2)

imprimir_valores()
