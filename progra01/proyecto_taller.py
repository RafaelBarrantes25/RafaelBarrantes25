import random
import time #para un time.sleep(3) cuando se imprimen las comunidades con valores restados

def crear_comunidad(extra):
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
    """
    Mete en una lista las comunidades generadas
    E: número de comunidades
    S: lista de comunidades
    R: ninguna
    """
    if extra == 0:
        extra = 0
    if numero == 0:
        return lista
    else:
        lista += [crear_comunidad(extra)]
        return generar_comunidades_aux(numero-1, lista, extra+1)





def imprimir_valores_aux(lista, respuesta, lista2):
    """
    Acomoda los valores de la lista para imprimirlos
    E: lista de comunidades
    S: string con los valores acomodados
    R: ninguna
    """
    if type(lista) != list:
        return False
    elif len(lista) == 0:
        return respuesta
    else:
        return imprimir_valores_aux(lista[1:], respuesta+str(lista[0][0])+": "+"Acervo: "+str(lista[0][1])+" "+"Autonomía: "+str(lista[0][2])+"\n", lista2+[lista[0]])


def verificar_valores(lista2, lista3):
    """
    Verifica si algún valor de una comunidad llega a 0, la elimina e imprime
    un mensaje si sí
    E: lista de comunidades
    S: lista de comunidades con una eliminada si llega a 0, y
    un mensaje avisando que fue eliminada
    R: ninguna
    """
    if lista2 == [] and lista3 != []:
        return lista3
    elif lista2 == [] and lista3 == []:
        return False
    elif lista2[0][1] <= 0 or lista2[0][2] <= 0:
        print("La comunidad "+lista2[0][0][10]+" ha sido eliminada")
        return verificar_valores(lista2[1:], lista3)
    else:
        return verificar_valores(lista2[1:], lista3+[lista2[0]])


def restar_valores(lista1, restar, lista2):
    """
    le resta valor de acervo o autonomía a una comunidad
    E: la lista de comunidades y la comunidad que se le va a restar
    S: la lista de comunidades con el valor restado
    R: ninguna
    """
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
        return "Error 3: No se puede restar el valor de la comunidad"



def verificar_elegir1(lista,elección):
    """
    verifica que exista la comunidad elegida
    E: lista de comunidades y la que eligió
    S: la eleccción
    R: ninguna
    """
    if lista == []:
        return False
    elif lista[0][0][10:] == elección:
        return elección
    else:
        return verificar_elegir1(lista[1:],elección)




def verificar_elegir2(elección2):
    """
    Verifica que elija 1 o 2 cuando le pregunte si quiere
    aumentar el acervo o autonomía
    E: la elección
    S: la elección si existe, sino False
    R: ninguna
    """
    if elección2 != "1" and elección2 != "2":
        return False
    else:
        return elección2



def sumar_valores(lista, comunidad_elegida, elección2,lista_nueva=[]):
    """
    Le suma el valor de acervo o autonomía a la comunidad elegida, 
    aleatorio en rango de 1 a 3
    E: lista de comunidades, comunidad elegida, elección de acervo o autonomía
    S: lista de comunidades con el valor sumado
    R: ninguna
    """
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
        return "Error 4, no se puede sumar el valor de la comunidad"


def finalizar():
    #Imprime mensajes cuando acaba el juego
    print("Todas las comunidades indígenas han sido eliminadas.")   
    print("Las empresas mineras y los misioneros han ganado.")
    print("Fin del juego.")
    

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
        print(f"\nLa lista de comunidades actual es:\n{comunidades_ordenadas}\n")
    else:
        lista = lista_nueva
        numero = 0
     

    if turno == 0:
        #Turno del jugador
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
        turno = 1 #Al cambiar el turno, sigue las mineras y misioneros

    if turno == 1:
        misioneros_o_mineras = random.randint(1,2) #escoge qué valor bajar
        time.sleep(2)
        if misioneros_o_mineras == 1:
            print("\nLos misioneros bajaron el acervo cultural de una comunidad\n")
        else:
            print("\nLas mineras bajaron la autonomía de una comunidad\n")

        lista_bajada = restar_valores_aux(lista_nueva,misioneros_o_mineras) #baja el valor de una comunidad
        
        lista_final = verificar_valores(lista_bajada, [])
        comunidades_tras_bajada = imprimir_valores_aux(lista_final, "", [])


        if lista_final != False:
            print(comunidades_tras_bajada)
            return juego(0,lista_final) #Vuelve al turno del jugador si alguna comunidad sigue existiendo
        else:
            return finalizar()  #Si no quedan comunidades, se acaba



#Para iniciar el juego, se llama a juego(0)
juego(0)