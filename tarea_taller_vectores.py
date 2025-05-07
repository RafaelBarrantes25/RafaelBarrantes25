def verificar_todos_numéricos_cola(lista):
    """
    Verifica que los elementos de una lista sean números
    E: lista
    S: True o False
    R: tipo list
    """
    if type(lista) != list:
        return "Error 0"
    else:
        return verificar_todos_numéricos_cola_aux(lista)


def verificar_todos_numéricos_cola_aux(lista):
    # Función auxiliar
    if lista == []:
        return True
    elif type(lista[0]) == int or type(lista[0]) == float:
        return verificar_todos_numéricos_cola_aux(lista[1:])
    else:
        return False

def vector_nulo(vector):
    """
    Comprueba si un vector es nulo
    E: lista
    S: True o False
    R: Vector lista
    """
    if vector == []:
        return True
    elif vector[0] == 0:
        return vector_nulo(vector[1:])
    else:
        return False

def vectores_iguales(vector1,vector2):
    """
    Revisa si dos vectores son iguales
    """
    if len(vector1) != len(vector2):
        return False
    elif vector1 == []:
        return True
    elif vector1[0] == vector2[0]:
        return vectores_iguales(vector1[1:],vector2[1:])
    else:
        return False

def suma(vector1,vector2):
    """
    Suma dos vectores
    E: dos vectores
    S: un vector con la suma
    R: números
    """
    if len(vector1) != len(vector2):
        return "Error 0"
    elif verificar_todos_numéricos_cola(vector1) == False:
        return "Error 1"
    elif verificar_todos_numéricos_cola(vector2) == False:
        return "Error 2"
    else:
        return suma_aux(vector1,vector2,[])


def suma_aux(vector1,vector2,resultado):
    #Función auxiliar
    if vector1 == []:
        return resultado
    else:
        return suma_aux(vector1[1:],vector2[1:],resultado+([vector1[0]+vector2[0]]))


def resta(vector1,vector2):
    """
    resta dos vectores
    E: dos vectores
    S: un vector con la resta
    R: números
    """
    if len(vector1) != len(vector2):
        return "Error 0"
    elif verificar_todos_numéricos_cola(vector1) == False:
        return "Error 1"
    elif verificar_todos_numéricos_cola(vector2) == False:
        return "Error 2"
    else:
        return resta_aux(vector1,vector2,[])
    
    
def producto_escalar(escalar, vector):
    """
    Multiplica un escalar por todos los elementos de la vector
    E: número y vector
    S: vector escalada
    R: debe ser tipo list y el número int o float
    """
    if type(vector) != list:
        return "Error 0"
    elif type(escalar) != int and type(escalar) != float:
        return "Error 1"
    else:
        return producto_escalar_aux(escalar, vector, [])


def producto_escalar_aux(número, vector, respuesta):
    # Función auxiliar
    if vector == []:
        return respuesta
    else:
        return producto_escalar_aux(número, vector[1:], respuesta + [vector[0] * número])



def resta_aux(vector1,vector2,resultado):
    #Función auxiliar
    if vector1 == []:
        return resultado
    else:
        return resta_aux(vector1[1:],vector2[1:],resultado+([vector1[0]-vector2[0]]))

