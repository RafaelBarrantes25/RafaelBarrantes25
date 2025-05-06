import random

def solicitar_comunidades():
    """
    Función que inicia el proyecto, un chiste tonto
    """
    eleccion = input("¿Quiere comunidades?:\n1: Sí\n2. No\n")
    if eleccion != "1" and eleccion != "2":
        return "Error 0: Esa no es una opción"
    elif eleccion == "2":
        return "Está bien\nFin del juego"
    else:
        pass
#########Debe crearse una función que imprima las comunidadeds imprimir_valores() y sea llamada por esta


def crear_comunidad(numero, extra):
    """
    crea comunidad, llamada por generar comunidades aux
    E: número
    S: comunidad
    R: ninguna
    """
    nombre = "Comunidad " + str(extra)
    acervo = random.randint(5, 10)
    autonomia = random.randint(5, 10)
    return [nombre, acervo, autonomia]


def generar_comunidades():
    """
    Llamada por ################# genera un número aleatorio y lo pasa
    a generar_comunidades
    """
    numero = random.randint(5, 9)
    return generar_comunidades_aux(numero,extra=1)


def generar_comunidades_aux(numero, lista=[],extra=1):
    """
    Llamada por generar_comunidades, crea una lista con cada comunidad
    dentro de una lista, el número de veces generado en generar_comunidades
    """
    if extra == 0:
        extra = 0
    if numero == 0:
        return lista
    else:
        lista.append(crear_comunidad(numero,extra))
        return generar_comunidades_aux(numero-1,lista,extra+1)



def contar_elementos_cola(lista):
    """
    Cuenta los elementos de una lista
    E: una lista
    S: el número de elementos
    R: la lista debe ser tipo list
    """
    if type(lista) != list:
        return "Error 0"
    else:
        return contar_elementos_cola_aux(lista, 0)


def contar_elementos_cola_aux(lista, respuesta):
    # Función auxiliar
    if lista == []:
        return respuesta
    else:
        return contar_elementos_cola_aux(lista[1:], respuesta + 1)



def imprimir_valores():
    #Obtiene la lista de valores y la pasa
    return imprimir_valores_aux(generar_comunidades(),"")


def imprimir_valores_aux(lista, respuesta):
    #Imprime las comunidades y sus valores
    if contar_elementos_cola(lista) == 0:
        print(respuesta)
        return verificar_valores(lista,[])
    else:
        return imprimir_valores_aux(lista[1:],respuesta+str(lista[0][0])+": "+"Acervo: "+str(lista[0][1])+" "+"Autonomía: "+str(lista[0][2])+"\n")



def verificar_valores(lista1,lista2):
    if len(lista1) == 0:
        return restar_valores(lista2)
    elif lista1[0][1] <= 0 or lista1[0][2] <= 0:
        return finalizar(lista1)
    else:
        return verificar_valores(lista1[1:],lista2+[lista1[0]])


def finalizar(lista):
    return "Fin del juego"

def restar_valores(lista):
    lista2 = lista[random.randint(0,len(lista))][random.randint(1,2)]-1
    print(imprimir_valores_aux(lista2,[]))

imprimir_valores()
#Se inicia llamando a solicitar_comunidades()



