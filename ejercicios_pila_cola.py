#Inicio ejercicios de pila

def factorial(número):
    """
    Calcula el factorial de un número
    E: Un número
    S: El factorial
    R: El número debe ser entero positivo
    """
    if type(número) != int or número < 0:
        return "Error01"
    elif número == 0:
     return 1
    else:
     return número*factorial(número-1)


def mcd(num1,num2):
    """
    E: 2 números
    S: el MCM entre ambos
    R: deben ser números
    """
    if type(num1) != int or type(num2) != int:
        return "Error 0"
    elif num1 < 0 or num2 < 0:
        return "Error 1"
    else:
        return mcd_aux(num1,num2)


def mcd_aux(num1,num2):
    """
    función auxiliar
    """
    if num1 % num2 == 0:
        return num2
    else:
        return mcd_aux(num2,num1%num2)



def eliminar_digito(dígito, número):
    """
    Elimina el dígito del número
    E: número y dígito
    S: número sin ese dígito
    R: número entero, dígito entero entre 0 y 9 inclusive
    """

    if type(número) !=int:
     return "Error01"
    elif type(dígito) !=int or dígito < 0 or dígito > 9:
     return "Error02"
    else:
     return eliminar_digito_aux(dígito, número)


def eliminar_digito_aux(dígito, número):
    """
    Función auxiliar
    """
    if número==0:
     return 0
    elif número%10==dígito:
     return eliminar_digito_aux(dígito, número//10)
    else:
     return número%10+eliminar_digito_aux(dígito,número//10)*10


def invertir_número(número):
    """
    Invierte un número
    E: Un número
    S: El número al revés
    R: debe ser entero positivo
    """
    if número == 0:
     return 0
    else:
     return(número%10)*10**(numero_digitos(número)-1)+invertir_número(número//10)


def numero_digitos(número):
    """
    Cuenta los dígitos de un número
    E: Un número
    S: número de dígitos
    R: Entero positivo
    """
    if número == 0:
     return 0
    else:
     return numero_digitos(número//10)+1


def contar_dígito(dígito, número):
    """
    cuenta cuántas veces hay un dígito en un número
    E: número y dígito
    S: veces que aparece el dígito en el número
    R: número entero, dígito entero entre 0 y 9 inclusive
    """

    if type(número) != int:
     return "Error01"
    elif type(dígito) != int or dígito < 0 or dígito > 9:
     return "Error02"
    else:
     return contar_dígito_aux(dígito, número)


def contar_dígito_aux(dígito, número):
    """
    Función auxiliar
    """
    if número==0:
     return 0
    elif número%10==dígito:
     return 1+contar_dígito_aux(dígito,número//10)
    else:
     return contar_dígito_aux(dígito,número//10)


def contar_vocales_pila(texto):
    """
    Cuenta las vocales de un texto
    E: Texto
    S: Número de vocales
    R: Tiene que ser un texto
    """
    if type(texto) != str:
        return "Error 1"
    else:
        return contar_vocales_pila_aux(texto)

def contar_vocales_pila_aux(texto):
    """
    Función auxiliar
    """
    if texto == "":
        return 0
    elif texto[0] == "a" or texto[0] == "e" or texto[0] == "i" or texto[0] == "u":
        return 1+contar_vocales_pila_aux(texto[1:])
    else:
        return contar_vocales_pila_aux(texto[1:])



def invertir_texto_pila(texto):
    """
    Invierte un texto
    E: Un texto
    S: El texto al revés
    R: Tiene que ser un str
    """
    if type(texto) != str:
        return "Error 1"
    else:
        return invertir_texto_pila_aux(texto)


def invertir_texto_pila_aux(texto):
    """
    Función auxiliar
    """
    if texto == "":
        return ""
    else:
        return invertir_texto_pila_aux(texto[1:])+texto[0]


def es_número_palindromo_pila(número):
    """
    E: número
    S: True si es palíndromo y False si no
    R: Debe ser un número
    """
    if type(número) != int:
        return "Error 0"
    elif invertir_número(número) == número:
        return True
    else:
        return False


def  es_texto_palindromo_pila(texto):
    """
    E: Texto
    S: True si es palíndromo y False si no
    R: Debe ser un texto
    """
    if type(texto) != str:
        return "Error 0"
    elif invertir_texto_pila(texto) == texto:
        return True
    else:
        return False



def contar_elementos_impares_pila(lista):
    """
    cuenta los elementos impares de una lista
    E: Una lista
    S: El número de impares
    R: Tiene que ser una lista
    """
    if type(lista) != list:
        return "Error01"
    else:
        return contar_elementos_impares_pila_aux(lista)

def contar_elementos_impares_pila_aux(lista):
    #Función auxiliar
    if lista == []:
        return 0
    elif lista[0] % 2 == 0:
        return 1 + contar_elementos_impares_pila_aux(lista[1:])
    else:
        return contar_elementos_impares_pila_aux(lista[1:])


def extraer_elementos_pares_pila(lista):
    """
    Extrae los elementos pares de una lista
    E: Una lista
    S: Lista con los pares de otra
    R: tipo list
    """
    if type(lista) != list:
        return "Error01"
    else:
        return extraer_elementos_pares_pila_aux(lista)

def extraer_elementos_pares_pila_aux(lista):
    #Función auxiliar
    if lista == []:
        return []
    elif lista[0] % 2 == 0:
        return [lista[0]]+extraer_elementos_pares_pila_aux(lista[1:])
    else:
        return extraer_elementos_pares_pila_aux(lista[1:])




def extraer_elementos_impares_pila(lista):
    """
    Extrae los elementos impares de una lista
    E: Una lista
    S: Lista con los impares de otra
    R: tipo list
    """
    if type(lista) != list:
        return "Error01"
    else:
        return extraer_elementos_impares_pila_aux(lista)

def extraer_elementos_impares_pila_aux(lista):
    #Función auxiliar
    if lista == []:
        return []
    elif lista[0] % 2 != 0:
        return [lista[0]]+extraer_elementos_impares_pila_aux(lista[1:])
    else:
        return extraer_elementos_impares_pila_aux(lista[1:])



def separar_elementos_pares_impares_pila(lista):
    """
    Crea una lista con 2 listas, una de pares y una de impares
    E: Una lista
    S: Una lista con 2 listas, una de pares y una de impares
    R: Debe ser lista
    """
    if type(lista)!=list:
        return "Error01"
    else:
        return [extraer_elementos_pares_pila(lista),extraer_elementos_impares_pila(lista)]


def multiplicar_escalar_vector_pila(escalar,vector):
    """
    Multiplica un escalar por un vector
    E: Un número escalar y una lista vector
    S: La lista escalada
    R: Número y lista
    """
    if type(escalar) != int or type(vector) != list:
        return "Error 0"
    else:
        return multiplicar_escalar_vector_pila_aux(escalar,vector)

def multiplicar_escalar_vector_pila_aux(escalar,vector):
    """
    Función auxiliar
    """
    if vector == []:
        return []
    else:
        return [escalar * vector[0]] + multiplicar_escalar_vector_pila_aux(escalar,vector[1:])


def verificar_todos_numéricos_pila(lista):
    """
    Verifica que todos los elementos de una lista sean numéricos
    E: Una lista
    S: True o False
    R: Tipo list
    """
    if type(lista) != list:
        return "Error 0"
    elif lista == []:
        return False
    else:
        return verificar_elementos_aux(lista)

def verificar_elementos_aux(lista):
    #Función auxiliar
    if lista == []:
        return True
    elif type(lista[0]) == int or type(lista[0]) == float:
        return verificar_elementos_aux(lista[1:])
    else:
        return False


def largo_texto(texto):
    #Función auxiliar
    if type(texto) != str:
        return "Error 0"
    elif texto == "":
        return 0
    else:
        return 1 + largo_texto(texto[1:])

def buscar_texto_pila(busca, texto):
    """
    Revisa si un texto está dentro de otro
    E: Texto largo y texto corto
    S: True o False
    R: deben ser textos y el texto largo debe ser más largo
    """
    if type(texto) != str or type(busca) != str:
        return "Error 0"
    elif largo_texto(texto) < largo_texto(busca):
        return "Error 1"
    else:
        return buscar_texto_pila_aux(busca,texto)

def buscar_texto_pila_aux(busca,texto):
    """
    Función auxiliar
    """

    if texto == "":
        return False
    elif busca == texto[0:largo_texto(busca)]:
        return True
    else:
        return buscar_texto_pila_aux(busca[1:],texto)


def dibujar_rectángulo_pila(largo,ancho):
    """
    E: Largo y ancho
    S: El rectángulo
    R: Números enteros positivos
    """
    if type(largo) != int or type(ancho) != int:
        return "Error 0"
    elif largo < 0 or ancho < 0:
        return "Error 1"
    else:
        return dibujar_rectángulo_pila_aux(largo,ancho)




def dibujar_rectángulo_pila_aux(largo,ancho):
    """
    Función auxiliar
    """
    if largo == 0 or ancho == 0:
        return ""
    elif ancho > 0:
        return "* " * largo + "\n" + dibujar_rectángulo_pila_aux(largo,ancho-1)
    else:
        return "* " * largo + dibujar_rectángulo_pila_aux(largo,ancho)