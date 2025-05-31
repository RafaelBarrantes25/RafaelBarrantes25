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
    return generar_comunidades_aux(numero, extra=1)


def generar_comunidades_aux(numero, lista=[], extra=1):
    if extra == 0:
        extra = 0
    if numero == 0:
        return lista
    else:
        lista += [crear_comunidad(numero, extra)]
        return generar_comunidades_aux(numero-1, lista, extra+1)


def imprimir_valores():
    # Obtiene la lista de valores y la pasa
    return imprimir_valores_aux(generar_comunidades(), "", [])


def imprimir_valores_aux(lista, respuesta, lista2):
    # Imprime las comunidades y sus valores
    if len(lista) == 0:
        print(respuesta)
        return elegir(lista2,"")  #Esto es lo que tiene la lista con las comunidades IMPORTANTE
    else:
        return imprimir_valores_aux(lista[1:], respuesta+str(lista[0][0])+": "+"Acervo: "+str(lista[0][1])+" "+"Autonomía: "+str(lista[0][2])+"\n", lista2+[lista[0]])


def verificar_valores(lista2, lista3):
    if lista2 == [] and lista3 != []:
        print(imprimir_valores_aux(lista3, "", []))
    elif lista2 == [] and lista3 == []:
        return finalizar()
    elif lista2[0][1] <= 0 or lista2[0][2] <= 0:
        return verificar_valores(lista2[1:], lista3)
    else:
        return verificar_valores(lista2[1:], [lista2[0]]+lista3)


def restar_valores(lista1, restar, lista2):
    if len(lista1) == 0:
        return verificar_valores(lista2, [])
    elif lista1[0][0] == restar[0]:
        return restar_valores(lista1[1:], restar, [restar]+lista2)
    else:
        return restar_valores(lista1[1:], restar, [lista1[0]]+lista2)


def restar_valores_aux(lista):
    número = random.randint(0, len(lista) - 1) #escoge una comunidad aleatoria
    número2 = random.randint(1, 3) #escoge en cuánto se va a disminuir el valor
    número3 = random.randint(1,2) #para decidir si se resta el acervo o la autonomía
    restar_acervo = [lista[número][0], lista[número]
              [1] - número2, lista[número][2]]
    restar_autonomía =[lista[número][0], lista[número]
              [1], lista[número][2]-número2]
    if número3 == 1:
        return restar_valores(lista, restar_acervo, [])
    else:
        return restar_valores(lista,restar_autonomía,[])



def verificar_numéricos(string, string2=""):
    """
    Verifica si el input es un número
    E: un string
    S: si es un número, lo pasa a la función verificar_elegir
    si no, dice eso
    R: nada
    """
    if string == "":
        return True
    elif string[0] == "0" or string[0] == "1" or string[0] == "2" or string[0] == "3" or string[0] == "4" or string[0] == "5" or string[0] == "6" or string[0] == "7" or string[0] == "8" or string[0] == "9":
        return verificar_numéricos(string[1:], string2+string[0])
    else:
        return "Error 2: Eso no es un número"



def elegir(lista, respuesta):
    """
    Le pregunta al usuario a cuál comunidad le quiere subir los valores
    E: El input del usuario, un número
    S: envía el resultado a verificar_elegir para ver si existe la comunidad
    R: debe ser un número de una comunidad existente
    """
    elección = input("Escoja la comunidad en la que quiere\nejecutar el proyecto (solo el número): ")
    elección2 = input("¿Qué proyecto quiere ejecutar?\n1: Acervo\n2: Autonomía\n")
    if elección != "" and elección2 != "":
        return verificar_elegir(lista, elección,elección2,[])
    else:
        return "Error 1"
    
def verificar_elegir(lista,elección,elección2,lista2):
    """
    Verifica que la comunidad que eligió existe
    E: la lista de comunidades
    S: si existe, envía la lista para que se le sume el valor
    R: la comunidad debe existir
    """
    valor = random.randint(1,3)

    if elección2 != "1" and elección2 != "2":
        return "Error 5: Esa no es una opción"
    if lista == []:
        return turno_cpu(lista2)

    elif lista[0][0][10:] == elección and elección2 == "1":
        suma = lista[0][1] + valor
        return verificar_elegir(lista[1:], elección, elección2, lista2+[[lista[0][0], suma, lista[0][2]]])
    elif lista[0][0][10:] == elección and elección2 == "2":
        suma = lista[0][2] + valor
        return verificar_elegir(lista[1:], elección, elección2, lista2+[[lista[0][0], lista[0][1], suma]])
    elif lista[0][0][10:] != elección:
        return verificar_elegir(lista[1:], elección, elección2, lista2+[lista[0]])
    else:
        return "Error 4"




def turno_cpu(lista):
    """
    Después del turno del jugador, vienen los misioneros o las
    mineras y le restan valores de acervo cultural o autonomía a una comunidad
    E: lista de comunidades
    S: lista con valores restados
    R: ninguna
    """
    print("Bajan valores")
    lista2 = restar_valores_aux(lista)
    imprimir_valores_aux(lista2, "", [])
    return elegir(lista2,"")

def finalizar():
    print("Fin")
    
imprimir_valores()
