def suma_conjuntos(lista1, lista2):
    if lista1 == []:
        return suma_conjuntos_2(lista1, lista2)
    elif lista1[0] == lista2[0]:
        return [lista2[0]]+suma_conjuntos(lista1[1:], lista2[1:])
    else:
        return [lista1[0]]+suma_conjuntos(lista1[1:], lista2)

def suma_conjuntos_2(lista1, lista2):
    if lista1 == []:
        return invertir_listas(lista1,lista2)
    elif lista1[0] == lista2[0]:
        return [lista1[0]]+suma_conjuntos(lista1[1:], lista2[1:])
    else:
        return [lista2[0]]+suma_conjuntos(lista1, lista2[1:])


def invertir_listas(lista1, lista2):
    return [invertir_lista_pila(lista1)]+[invertir_lista_pila(lista2)]

def invertir_lista_pila(lista):
    """
    Invierte una lista
    E: Lista
    S: Lista al revés
    R: Debe ser tipo list
    """
    if type(lista) != list:
        return "Error 0"
    else:
        return invertir_lista_pila_aux(lista)

def invertir_lista_pila_aux(lista):
    #Función auxiliar
    if lista == []:
        return []
    else:
        return invertir_lista_pila_aux(lista[1:])+[lista[0]]



print(suma_conjuntos([1,2,4,5,6],[4,5,6,1,8,9]))