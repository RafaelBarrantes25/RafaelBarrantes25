import random


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





def generar_comunidades_aux(numero, lista=[], extra=1):
    if extra == 0:
        extra = 0
    if numero == 0:
        return lista
    else:
        lista += [crear_comunidad(numero, extra)]
        return generar_comunidades_aux(numero-1, lista, extra+1)





def imprimir_valores_aux(lista, respuesta, lista2):
    # Imprime las comunidades y sus valores
    if len(lista) == 0:
        return respuesta
    else:
        return imprimir_valores_aux(lista[1:], respuesta+str(lista[0][0])+": "+"Acervo: "+str(lista[0][1])+" "+"Autonomía: "+str(lista[0][2])+"\n", lista2+[lista[0]])


def verificar_valores(lista2, lista3):
    if lista2 == [] and lista3 != []:
        return lista3
    elif lista2 == [] and lista3 == []:
        return False
    elif lista2[0][1] <= 0 or lista2[0][2] <= 0:
        return verificar_valores(lista2[1:], lista3)
    else:
        return verificar_valores(lista2[1:], lista3+[lista2[0]])


def restar_valores(lista1, restar, lista2):
    if len(lista1) == 0:
        return lista2
    elif lista1[0][0] == restar[0]:
        return restar_valores(lista1[1:], restar, lista2+[restar])
    else:
        return restar_valores(lista1[1:], restar, lista2+[lista1[0]])


def restar_valores_aux(lista,número3):
    número = random.randint(0, len(lista) - 1) #escoge una comunidad aleatoria
    número2 = random.randint(1, 3) #escoge en cuánto se va a disminuir el valor
    
    restar_autonomía =[lista[número][0], lista[número]
              [1], lista[número][2]-número2]
    if número3 == 1:
        restar_acervo = [lista[número][0], lista[número]
              [1] - número2, lista[número][2]]
        return restar_valores(lista, restar_acervo, [])
    elif número3 == 2:
        
        return restar_valores(lista,restar_autonomía,[])
    else:
        return "Error 6: No se puede restar el valor de la comunidad"


def verificar_elegir1(lista,elección):
    
    if lista == []:
        return False
    elif lista[0][0][10:11] == elección:
        return elección
    else:
        return verificar_elegir1(lista[1:],elección)




def verificar_elegir2(elección2):
    if elección2 != "1" and elección2 != "2":
        return False
    else:
        return elección2



def sumar_valores(lista, comunidad_elegida, elección2,lista_nueva=[]):
    valor = random.randint(1,3)
    if lista == []:
        return lista_nueva
    elif elección2 == "1" and lista[0][0][10:] == comunidad_elegida:
        suma = lista[0][1] + valor
        return sumar_valores(lista[1:], comunidad_elegida, elección2, lista_nueva+[[lista[0][0], suma, lista[0][2]]])
    elif elección2 == "2" and lista[0][0][10:] == comunidad_elegida:
        suma = lista[0][2] + valor
        return sumar_valores(lista[1:], comunidad_elegida, elección2, lista_nueva+[[lista[0][0], lista[0][1], suma]])
    elif lista[0][0][10:] != comunidad_elegida:
        return sumar_valores(lista[1:], comunidad_elegida, elección2, lista_nueva+[lista[0]])
    else:
        return "Error 4"




def finalizar():
    print("Fin")
    

def juego(turno, lista_nueva=[]):
    """
    Función principal del juego
    E: el turno del jugador
    S: el resultado de la función
    R: ninguna
    """
    numero = 0
    lista = []
    if lista == lista_nueva:
        numero = random.randint(3,5) #Número aleatorio, define el número de comunidades
        lista = generar_comunidades_aux(numero, extra=1) #devuelve una lista con las comunidades
        comunidades_ordenadas = imprimir_valores_aux(lista, "", []) #Ordena las comunidades en una string
        print(f"\n La lista de comunidades actual es:\n{comunidades_ordenadas}\n")
    else:
        lista = lista_nueva
        numero = 0
     

    if turno == 0:

        elección1 = input("Escoja la comunidad en la que quiere\nejecutar el proyecto (solo el número): ")
        if verificar_elegir1(lista,elección1) == False: #elige comunidad y revisa que exista
            print("Error 1: Esa no es una comunidad")
            return juego(0, lista)
        
        acervo_o_autonomia = input("¿Qué proyecto quiere ejecutar?\n1: Acervo\n2: Autonomía\n")
        if verificar_elegir2(acervo_o_autonomia) == False: #elige si sube el acervo o la autonomía
            print("Error 2: Esa no es una opción")
            return juego(0, lista)
        
        #Revisa si eligió acervo o autonomía e imprime un mensaje
        if acervo_o_autonomia == "1":
            print("\nEjecutó un proyecto que aumentó el acervo cultural de la comunidad "+elección1+"\n")
        elif acervo_o_autonomia == "2":
            print("\nEjecutó un proyecto que aumentó la autonomía de la comunidad "+elección1+"\n")
        else:
            return "Error 5: Esa no es una opción"
        
        #Imprime la lista con los valores sumados
        lista_nueva = sumar_valores(lista, elección1, acervo_o_autonomia, [])

        comunidades_tras_suma = imprimir_valores_aux(lista_nueva, "", []) #Ordena las comunidades en una string
        print(comunidades_tras_suma)
        turno = 1

    if turno == 1:
        misioneros_o_mineras = random.randint(1,2) #escoge qué valor bajar
        if misioneros_o_mineras == 1:
            print("\nLos misioneros bajaron el acervo cultural de una comunidad\n")
        else:
            print("\nLas mineras bajaron la autonomía de una comunidad\n")

        lista_bajada = restar_valores_aux(lista_nueva,misioneros_o_mineras) #baja el valor de una comunidad
        comunidades_tras_bajada = imprimir_valores_aux(lista_bajada, "", [])
        print(comunidades_tras_bajada)
        
        lista_final = verificar_valores(lista_bajada, [])
        if lista_final != False:
            return juego(0,lista_final)
        else:
            print("Fin del juego")
            return finalizar()



#Para iniciar el juego, se llama a juego(0)
juego(0)