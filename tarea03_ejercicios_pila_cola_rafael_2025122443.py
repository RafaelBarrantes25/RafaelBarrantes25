# Inicio ejercicios de pila


def factorial_pila(número):
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
        return número * factorial_pila(número - 1)


def mcd_pila(num1, num2):
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
        return mcd_pila_aux(num1, num2)


def mcd_pila_aux(num1, num2):
    """
    función auxiliar
    """
    if num1 % num2 == 0:
        return num2
    else:
        return mcd_pila_aux(num2, num1 % num2)


def eliminar_digito_pila(dígito, número):
    """
    Elimina el dígito del número
    E: número y dígito
    S: número sin ese dígito
    R: número entero, dígito entero entre 0 y 9 inclusive
    """

    if type(número) != int:
        return "Error01"
    elif type(dígito) != int or dígito < 0 or dígito > 9:
        return "Error02"
    else:
        return eliminar_digito_pila_aux(dígito, número)


def eliminar_digito_pila_aux(dígito, número):
    """
    Función auxiliar
    """
    if número == 0:
        return 0
    elif número % 10 == dígito:
        return eliminar_digito_pila_aux(dígito, número // 10)
    else:
        return número % 10 + eliminar_digito_pila_aux(dígito, número // 10) * 10


def invertir_número_pila(número):
    """
    Invierte un número
    E: Un número
    S: El número al revés
    R: debe ser entero positivo
    """
    if número == 0:
        return 0
    else:
        return (número % 10) * 10 ** (numero_digitos(número) - 1) + invertir_número_pila(número // 10)


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
        return numero_digitos(número // 10) + 1


def contar_digito_pila(digito, número):
    """
    cuenta cuántas veces hay un digito en un número
    E: número y digito
    S: veces que aparece el digito en el número
    R: número entero, digito entero entre 0 y 9 inclusive
    """

    if type(número) != int:
        return "Error01"
    elif type(digito) != int or digito < 0 or digito > 9:
        return "Error02"
    else:
        return contar_digito_pila_aux(digito, número)


def contar_digito_pila_aux(digito, número):
    """
    Función auxiliar
    """
    if número == 0:
        return 0
    elif número % 10 == digito:
        return 1 + contar_digito_pila_aux(digito, número // 10)
    else:
        return contar_digito_pila_aux(digito, número // 10)


def contar_caracter_pila(caracter, texto):
    """
    Cuenta las veces que un caracter aparece en un texto
    E: caracter y texto
    S: número de veces que aparece el caracter en el texto
    R: Caracter longitud 1, ambos tipo str
    """
    if type(texto) != str or type(caracter) != str:
        return "Error 0"
    elif len(caracter) != 1:
        return "Error 1"
    else:
        return contar_caracter_pila_aux(caracter, texto)


def contar_caracter_pila_aux(caracter, texto):
    # Función auxiliar
    if texto == "":
        return 0
    elif texto[0] == caracter:
        return 1 + contar_caracter_pila(caracter, texto[1:])
    else:
        return contar_caracter_pila(caracter, texto[1:])


def eliminar_sección_pila(inicio, final, texto):
    """
    Elimina una sección de un texto
    E: El texto, el inicio y el final
    S: Texto sin el inicio y el final
    R: Inicio debe ser menor, tipo int, texto tipo str
    """
    if type(texto) != str:
        return "Error 0"
    elif inicio > final:
        return "Error 1"
    elif type(inicio) != int or type(final) != int:
        return "Error 2"
    else:
        return eliminar_sección_pila_aux(inicio, final, texto)


def eliminar_sección_pila_aux(inicio, final, texto):
    # Función auxiliar
    if final == 0:
        return texto[1:]
    elif inicio <= 0:
        return eliminar_sección_pila_aux(inicio, final - 1, texto[1:])
    else:
        return texto[0] + eliminar_sección_pila_aux(inicio - 1, final - 1, texto[1:])


def eliminar_final_pila(índice, texto):
    """
    Elimina una final de un texto
    E: índice y texto
    S: texto sin el final
    R: índice debe ser int, texto str
    """
    if type(texto) != str:
        return "Error 0"
    elif type(índice) != int:
        return "Error 1"
    else:
        return eliminar_final_pila_aux(índice, texto)


def eliminar_final_pila_aux(índice, texto):
    # Función auxiliar
    if índice == 0 or texto == "":
        return ""
    else:
        return texto[0] + eliminar_final_pila_aux(índice - 1, texto[1:])


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
        return 1 + contar_vocales_pila_aux(texto[1:])
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
        return invertir_texto_pila_aux(texto[1:]) + texto[0]


def es_número_palindromo_pila(número):
    """
    E: número
    S: True si es palíndromo y False si no
    R: Debe ser un número
    """
    if type(número) != int:
        return "Error 0"
    elif invertir_número_pila(número) == número:
        return True
    else:
        return False


def es_texto_palindromo_pila(texto):
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


def eliminar_espacios_cola(texto):
    """
    Elimina espacios de un texto
    E: Un texto
    S: el texto sin espacios
    R: debe ser str
    """
    if type(texto) != str:
        return "Error 0"
    else:
        return eliminar_espacios_cola_aux(texto, "")


def eliminar_espacios_cola_aux(texto, respuesta):
    # Función auxiliar
    if texto == "":
        return respuesta
    elif texto[0] == " ":
        return eliminar_espacios_cola_aux(texto[1:], respuesta)
    else:
        return eliminar_espacios_cola_aux(texto[1:], respuesta + texto[0])


def eliminar_espacios_pila(texto):
    """
    elimina los espacios de un texto
    E: Texto
    S: texto sin espacios
    R: Tiene que ser un texto
    """
    if type(texto) != str:
        return "Error 1"
    else:
        return eliminar_espacios_pila_aux(texto)


def eliminar_espacios_pila_aux(texto):
    """
    Función auxiliar
    """
    if texto == "":
        return ""
    elif texto[0] == " ":
        return eliminar_espacios_pila_aux(texto[1:])
    else:
        return texto[0] + eliminar_espacios_pila_aux(texto[1:])


def separar_palabras_pila(caracter, texto):
    """
    Cuenta las veces que un caracter aparece en un texto
    E: caracter y texto
    S: número de veces que aparece el caracter en el texto
    R: Caracter longitud 1, ambos tipo str
    """
    if type(texto) != str or type(caracter) != str:
        return "Error 0"
    elif len(caracter) != 1:
        return "Error 1"
    else:
        return separar_palabras_pila_aux(caracter, texto)


def separar_palabras_pila_aux(caracter, texto):
    # Función auxiliar
    if texto == "":
        return ""
    elif texto[0] == caracter:
        return ", " + separar_palabras_pila(caracter, texto[1:])
    else:
        return texto[0] + separar_palabras_pila(caracter, texto[1:])


def contar_elementos_pila(lista):
    """
    Cuenta el número de elementos de una lista
    E: Lista
    S: Número de elementos
    R: Tipo list
    """
    if type(lista) != list:
        return "Error 0"
    else:
        return contar_elementos_pila_aux(lista)


def contar_elementos_pila_aux(lista):
    # Función auxiliar
    if lista == []:
        return 0
    else:
        return 1 + contar_elementos_pila_aux(lista[1:])


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
    # Función auxiliar
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
    # Función auxiliar
    if lista == []:
        return []
    elif lista[0] % 2 == 0:
        return [lista[0]] + extraer_elementos_pares_pila_aux(lista[1:])
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
    # Función auxiliar
    if lista == []:
        return []
    elif lista[0] % 2 != 0:
        return [lista[0]] + extraer_elementos_impares_pila_aux(lista[1:])
    else:
        return extraer_elementos_impares_pila_aux(lista[1:])


def separar_elementos_pares_impares_pila(lista):
    """
    Crea una lista con 2 listas, una de pares y una de impares
    E: Una lista
    S: Una lista con 2 listas, una de pares y una de impares
    R: Debe ser lista
    """
    if type(lista) != list:
        return "Error01"
    else:
        return [extraer_elementos_pares_pila(lista), extraer_elementos_impares_pila(lista)]


def multiplicar_escalar_vector_pila(escalar, vector):
    """
    Multiplica un escalar por un vector
    E: Un número escalar y una lista vector
    S: La lista escalada
    R: Número y lista
    """
    if type(escalar) != int or type(vector) != list:
        return "Error 0"
    else:
        return multiplicar_escalar_vector_pila_aux(escalar, vector)


def multiplicar_escalar_vector_pila_aux(escalar, vector):
    """
    Función auxiliar
    """
    if vector == []:
        return []
    else:
        return [escalar * vector[0]] + multiplicar_escalar_vector_pila_aux(escalar, vector[1:])


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
        return verificar_todos_numéricos_aux(lista)


def verificar_todos_numéricos_aux(lista):
    # Función auxiliar
    if lista == []:
        return True
    elif type(lista[0]) == int or type(lista[0]) == float:
        return verificar_todos_numéricos_aux(lista[1:])
    else:
        return False


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
    # Función auxiliar
    if lista == []:
        return []
    else:
        return invertir_lista_pila_aux(lista[1:]) + [lista[0]]


def largo_texto(texto):
    # Función auxiliar
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
        return buscar_texto_pila_aux(busca, texto)


def buscar_texto_pila_aux(busca, texto):
    """
    Función auxiliar
    """

    if texto == "":
        return False
    elif busca == texto[0:largo_texto(busca)]:
        return True
    else:
        return buscar_texto_pila_aux(busca[1:], texto)


def juntar_asteriscos_pila(número):
    """
    Imprime asteriscos según el número
    E: Un número
    S: Un texto
    R: El número debe ser entero positivo
    """
    if número == 0:
        return ""
    else:
        return "* " + juntar_asteriscos_pila(número - 1)


def dibujar_triángulo_pila(número):
    """
    Dibuja un triángulo de asteriscos
    E: El número de capas
    S: Un triángulo de asteriscos
    R: Entero positivo impar
    """
    if type(número) != int or número < 0 or número % 2 == 0:
        return "Error 0"
    else:
        return (triángulo_derecho_pila(número) + "\n" + "\n" + triángulo_revés_pila(número))


def triángulo_derecho_pila(número, x=-1):
    '''Función auxiliar de dibujar_triángulo_pila.'''
    if número == 0:
        return ""

    else:
        return (triángulo_derecho_pila(número - 1, x + 1) +
                "\n" + " " * (x + 1) + juntar_asteriscos_pila(número))


def triángulo_revés_pila(número, n=0):
    '''Función auxiliar de dibujar_triángulo_pila.'''
    if número == 0:
        return ""
    else:
        return (juntar_asteriscos_pila(número) +
                "\n" + " " * (n + 1) + triángulo_revés_pila(número - 1, n + 1))


def dibujar_rectángulo_pila(largo, ancho):
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
        return dibujar_rectángulo_pila_aux(largo, ancho)


def dibujar_rectángulo_pila_aux(largo, ancho):
    """
    Función auxiliar
    """
    if largo == 0 or ancho == 0:
        return ""
    elif ancho > 0:
        return "* " * largo + "\n" + dibujar_rectángulo_pila_aux(largo, ancho - 1)
    else:
        return "* " * largo + dibujar_rectángulo_pila_aux(largo, ancho)


def permutaciones_pila(lista1, lista2):
    """
    Crea la permutación de 2 listas
    E: Dos listas
    S: Una lista con las listas permutadas
    R: Deben ser tipo list
    """
    if type(lista1) != list:
        return "Error 0"
    elif type(lista2) != list:
        return "Error 1"
    else:
        return permutaciones_lista_pila_aux(lista1, lista2)


def permutaciones_lista_pila_aux(lista1, lista2):
    # Función auxiliar
    if lista1 == []:
        return []
    else:
        return (unir_elementos_pila(lista2, lista1[0]) + permutaciones_lista_pila_aux(lista1[1:], lista2))


def unir_elementos_pila(lista, elemento):
    """
    Función auxiliar
    E: Lista y elemento
    S: Lista
    R: Tipo list
    """
    if lista == []:
        return []
    else:
        return [[elemento] + [lista[0]]] + unir_elementos_pila(lista[1:], elemento)


# Fin ejercicios pila


# Inicio ejercicios cola


def contar_digito_cola(num):
    """
    cuenta cuántos dígitos hay en un número
    E: número
    S: número de dígitos
    R: número
    """
    if type(num) != int:
        return "Error 1"
    elif num == 0:
        return 0
    else:
        return contar_digito_cola_aux(num, 0)


def contar_digito_cola_aux(num, cant):
    # Función auxiliar
    if num == 0:
        return cant
    else:
        return contar_digito_cola_aux(num // 10, cant + 1)


def factorial_cola(número):
    """
    Calcula el factorial de un número
    E: número entero positivo
    S: el factorial
    R: debe ser un número, entero y positivo
    """
    if type(número) != int:
        return "Error 1"
    elif número < 0:
        return "Error 2"
    else:
        return factorial_cola_aux(número, 1)


def factorial_cola_aux(número, resultado):
    # Función auxiliar
    if número == 0:
        return resultado
    else:
        return factorial_cola_aux(número - 1, número * resultado)


def mcd_cola(número1, número2):
    """
    E: 2 números
    S: el MCM entre ambos
    R: deben ser números
    """
    if type(número1) != int or type(número2) != int:
        return "Error 0"
    elif número1 < 0 or número2 < 0:
        return "Error 1"
    else:
        return mcd_cola_aux(número1, número2)


def mcd_cola_aux(número1, número2):
    """
    función auxiliar
    """
    if número1 % número2 == 0:
        return número2
    else:
        return mcd_cola_aux(número2, número1 % número2)


def eliminar_digito_cola(digito, número):
    """
    Elimina un dígito de un número más largo
    E: El número y el dígito, enteros positivos
    S: El número sin el dígito
    R: tienen que ser enteros positivos, dígito debe ser más corto
    """
    if type(número) != int or type(digito) != int:
        return "Error 0"
    elif digito >= 10 or digito < 0:
        return "Error 1"
    elif número < 0:
        return "Error 2"
    else:
        return eliminar_digito_cola_aux(digito, número, 1, 0)


def eliminar_digito_cola_aux(digito, número, número_nuevo, extra):
    """
    función auxiliar
    """
    if número == 0:
        return extra
    elif número % 10 == digito:
        return eliminar_digito_cola_aux(digito, número // 10, número_nuevo, extra)
    else:
        return eliminar_digito_cola_aux(digito, número // 10, número_nuevo * 10, extra + (número % 10) * número_nuevo)

def cuenta_digito_cola(número):
    """
    Cuenta los dígitos de un número
    E: Número
    S: dígitos
    R: int
    """
    if type(número) != int:
        return "Error 0"
    else:
        return cuenta_digito_aux(número,0)

def cuenta_digito_aux(número,resultado):
    #Función auxiliar
    if número == 0:
        return resultado
    else:
        return cuenta_digito_aux(número//10, resultado+1)

def invertir_número_cola(número):
    """
    invierte número entero positivo
    E: número
    S: número invertido
    R: entero positivo número
    """
    if type(número) != int:
        return "Error 0"
    elif número < 0:
        return "Error 1"
    else:
        return invertir_número_cola_aux(número, 10 ** (cuenta_digito_cola(número) - 1), 0)


def invertir_número_cola_aux(número, potencia, result):
    """
    función auxiliar
    """
    if número == 0:
        return result
    else:
        return invertir_número_cola_aux(número // 10, potencia // 10, result + (número % 10) * potencia)



def contar_vocales_cola(texto):
    """
    Cuenta las vocales de un texto
    E: texto
    S: número de vocales
    R: texto debe ser tipo string
    """
    if type(texto) != str:
        return "Error 0"
    else:
        return contar_vocales_cola_aux(texto, ["a", "e", "i", "o", "u"], 0)


def comparar_cola(texto, lista):
    # verifica si un str pertenece a una lista
    if lista == []:
        return False
    elif texto == lista[0]:
        return True
    else:
        return comparar_cola(texto, lista[1:])


def contar_vocales_cola_aux(texto, vocales, respuesta):
    # función auxiliar
    if texto == "":
        return respuesta
    elif comparar_cola(texto[0], vocales) == True:
        return contar_vocales_cola_aux(texto[1:], vocales, respuesta + 1)
    else:
        return contar_vocales_cola_aux(texto[1:], vocales, respuesta)


def invertir_texto_cola(texto):
    """
    Invierte un texto
    E: texto
    S: el texto al revés
    R: debe ser tipo str
    """
    if type(texto) != str:
        return "Error 0"
    else:
        return invertir_texto_cola_aux(texto, "")


def invertir_texto_cola_aux(texto, respuesta):
    if texto == "":
        return respuesta
    else:
        return invertir_texto_cola_aux(texto[1:], texto[0] + respuesta)


def es_número_palindromo_cola(número):
    """
    Revisa si un número es palíndromo
    E: número
    S: True o False, dependiendo si es palíndromo o no
    R: debe ser número entero positivo
    """
    if type(número) != int:
        return "Error 0"
    elif número < 0:
        return "Error 1"
    else:
        return es_número_palindromo_cola_aux(número)


def es_número_palindromo_cola_aux(número):
    # Función auxiliar
    if número == invertir_número_cola(número):
        return True
    else:
        return False


def es_texto_palindromo_cola(texto):
    """
    Revisa si un texto es palíndromo o no
    E: texto
    S: True o False
    R: debe ser tipo str
    """
    if type(texto) != str:
        return "Error 0"
    elif texto == invertir_texto_cola(texto):
        return True
    else:
        return False


def separa_palabras_cola(caracter, texto):
    """
    Separa un texto según un caracter
    E: texto y caracter
    S: texto separado
    R: tipo str, solo un caracter
    """
    if type(texto) != str or type(caracter) != str:
        return "Error 0"
    elif caracter[1:] != "":
        return "Error 1"
    else:
        return separa_palabras_cola(caracter, texto, [], "")


def separa_palabras_cola_aux(caracter, texto, lista, respuesta):
    # Función auxiliar
    if texto == "":
        return lista + [respuesta]
    elif texto[0] == caracter:
        return separa_palabras_cola_aux(caracter, texto[1:],
                                        lista + [respuesta], "")
    else:
        return separa_palabras_cola_aux(caracter, texto[1:], lista,
                                        respuesta + texto[0])


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


def contar_elementos_impares_cola(lista):
    """
    Cuenta la cantidad de números impares
    E: lista
    S: número de impares
    R: tipo list
    """
    if type(lista) != list:
        return "Error 0"
    elif verificar_todos_numéricos_pila(lista) == False:
        return "Error 1"
    else:
        return contar_elementos_impares_cola_aux(lista, 0)


def contar_elementos_impares_cola_aux(lista, respuesta):
    # Función auxiliar
    if lista == []:
        return respuesta
    elif lista[0] % 2 != 0:
        return contar_elementos_impares_cola_aux(lista[1:], respuesta + 1)
    else:
        return contar_elementos_impares_cola_aux(lista[1:], respuesta)


def extraer_elementos_pares_cola(lista):
    """
    Cuenta los elementos pares de una lista
    E: lista
    S: lista de pares
    R: lista debe ser tipo list
    """
    if type(lista) != list:
        return "Error 0"
    else:
        return extraer_elementos_pares_cola_aux(lista, [])


def extraer_elementos_pares_cola_aux(lista, respuesta):
    # Función auxiliar
    if lista == []:
        return respuesta
    elif type(lista[0]) != int:
        return extraer_elementos_pares_cola_aux(lista[1:], respuesta)
    elif lista[0] % 2 == 0:
        return extraer_elementos_pares_cola_aux(lista[1:], respuesta + [lista[0]])
    else:
        return extraer_elementos_pares_cola_aux(lista[1:], respuesta)


def extraer_elementos_impares_cola(lista):
    """
    Cuenta los elementos impares de una lista
    E: lista
    S: lista de impares
    R: lista debe ser tipo list
    """
    if type(lista) != list:
        return "Error 0"
    else:
        return extraer_elementos_impares_cola_aux(lista, [])


def extraer_elementos_impares_cola_aux(lista, respuesta):
    # Función auxiliar
    if lista == []:
        return respuesta
    elif type(lista[0]) != int:
        return extraer_elementos_impares_cola_aux(lista[1:], respuesta)
    elif lista[0] % 2 != 0:
        return extraer_elementos_impares_cola_aux(lista[1:], respuesta + [lista[0]])
    else:
        return extraer_elementos_impares_cola_aux(lista[1:], respuesta)


def separar_elementos_pares_impares_cola(lista):
    """
    Crea una lista con 2 listas, una de pares y una de impares
    E: lista
    S: lista con listas
    R: tipo list
    """
    if type(lista) != list:
        return "Error 0"
    else:
        return [extraer_elementos_impares_cola(lista)] + [extraer_elementos_pares_cola(lista)]


def pertenece(lista, elemento):
    """
    Verifica si un elemento pertenece a una lista
    E: elemento y lista
    S: true o false
    R: tipo list
    """
    if type(lista) != list:
        return "Error 0"
    else:
        return pertenece_aux(lista, elemento)


def pertenece_aux(lista, elemento):
    # Función auxiliar
    if lista == []:
        return False
    elif lista[0] == elemento:
        return True
    else:
        return pertenece_aux(lista[1:], elemento)


def suma_conjuntos_cola(conjunto1, conjunto2):
    """
    Une 2 conjuntos
    E: dos conjuntos
    S: una conjunto
    R: deben ser tipo list
    """
    if type(conjunto1) != list or type(conjunto2) != list:
        return "Error 0"
    else:
        return suma_conjuntos_cola_aux(conjunto1, conjunto2)


def suma_conjuntos_cola_aux(conjunto1, conjunto2):
    # Función auxiliar
    if conjunto2 == []:
        return conjunto1
    elif pertenece(conjunto1, conjunto2[0]):
        return suma_conjuntos_cola_aux(conjunto1, conjunto2[1:])
    else:
        return suma_conjuntos_cola_aux(conjunto1 + [conjunto2[0]], conjunto2[1:])


def multiplicar_escalar_vector_cola(escalar, vector):
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
        return multiplicar_escalar_vector_cola_aux(escalar, vector, [])


def multiplicar_escalar_vector_cola_aux(número, vector, respuesta):
    # Función auxiliar
    if vector == []:
        return respuesta
    else:
        return multiplicar_escalar_vector_cola_aux(número, vector[1:], respuesta + [vector[0] * número])


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


def invertir_lista_cola(lista):
    """
    Invierte una lista
    E: lista
    S: lista invertida
    R: debe ser tipo list
    """
    if type(lista) != list:
        return "Error 0"
    else:
        return invertir_lista_cola_aux(lista, [])


def invertir_lista_cola_aux(lista, respuesta):
    # Función auxiliar
    if lista == []:
        return respuesta
    else:
        return invertir_lista_cola_aux(lista[1:], [lista[0]] + respuesta)


def buscar_texto_cola(busca, texto):
    """
    Buca un texto en otro
    E: texto a buscar y texto donde se busca
    S: True o False
    R: tipo str
    """
    if type(texto) != str:
        return 'Error02'
    elif type(busca) != str:
        return 'Error01'
    else:
        return buscar_texto_cola_aux(texto, busca)


def buscar_texto_cola_aux(texto, busca):
    # Función auxiliar
    if texto == "":
        return False
    elif eliminar_final_cola(texto, len(busca)) == busca:
        return True
    else:
        return buscar_texto_cola_aux(texto[1:], busca)


def eliminar_final_cola_triangulo(indice,texto):
    """
    Elimina el final de un texto según un índice
    E: Un texto y un número.
    S: Un texto sin el final
    R: Texto tipo str, índice entero positivo.
    """
    if type(texto) != str:
        return "Error 01"
    elif type(indice) != int or indice < 0:
        return "Error 02"
    else:
        return eliminar_final_cola_triangulo_aux(indice, texto, "")

def eliminar_final_cola_triangulo_aux(indice, texto, respuesta):
  #Función auxiliar
    if indice == 0:
        return respuesta
    else:
        return eliminar_final_cola_triangulo_aux(indice-1,texto[1:],respuesta+texto[0])


def dibujar_triángulo_cola(número):
    """
    Dibuja un triángulo
    E: Número de capas
    S: Triángulo hecho de asteriscos
    R: Entero positivo
    """
    if type(número) != int:
        return "Error 0"

    elif número % 2 != 0:
        return dibujar_triángulo_derecho_cola(0, "", número - 1, número) + "\n" + "\n" + dibujar_triángulo_revés_cola(
            número, "", 0)
    else:
        return dibujar_triángulo_derecho_cola(0, "", número - 1, número) + "\n" + "\n" + dibujar_triángulo_revés_cola(
            número, "", 0)


def dibujar_triángulo_derecho_cola(número, triángulo, espacios, fin):
    # Función auxiliar
    if número == fin:
        return eliminar_final_cola_triangulo(len(triángulo) - 1, triángulo)
    else:
        return dibujar_triángulo_derecho_cola(número + 1,triángulo + " " * espacios + juntar_asteriscos_cola(número + 1,"") + "\n",espacios - 1, fin)


def dibujar_triángulo_revés_cola(número, triángulo, espacios):
    # Función auxiliar
    if número == 0:
        return triángulo
    else:
        return dibujar_triángulo_revés_cola(número - 1,triángulo + " " * espacios + juntar_asteriscos_cola(número, "") + "\n",espacios + 1)


def juntar_asteriscos_cola(número, respuesta):
    # Función auxiliar
    if número == 0:
        return respuesta
    else:
        return juntar_asteriscos_cola(número - 1, respuesta + "* ")


def contar_caracter_cola(caracter, texto):
    """
    Cuenta cuántas veces está un caracter en un texto
    E: caracter y texto
    S: número de veces que aparece
    R: un solo caracter, ambos tipo str
    """
    if type(texto) != str:
        return 'Error02'
    elif type(caracter) != str or caracter[1:] != "":
        return 'Error01'
    else:
        return contar_caracter_cola_aux(texto, caracter, 0)


def contar_caracter_cola_aux(texto, caracter, resultado):
    # Función auxiliar
    if texto == "":
        return resultado
    elif texto[0] == caracter:
        return contar_caracter_cola_aux(texto[1:], caracter, resultado + 1)
    else:
        return contar_caracter_cola_aux(texto[1:], caracter, resultado)


def eliminar_sección_cola(inicio, final, texto):
    """
    Elimina una sección de un texto
    E: El texto y los índices
    S: Texto sin la sección
    R: texto tipo str, inicio y fin tipo int, inicio debe ser menor
    """
    if type(texto) != str:
        return "Error 0"
    elif type(inicio) != int or type(final) != int:
        return "Error 1"
    elif inicio > final:
        return "Error 2"
    else:
        return eliminar_sección_cola_aux(texto, inicio, final, "")


def eliminar_sección_cola_aux(texto, inicio, fin, resultado):
    # Función auxiliar
    if fin == 0:
        return resultado + texto[1:]

    elif inicio <= 0:
        return eliminar_sección_cola_aux(texto[1:], inicio, fin - 1, resultado)
    else:
        return eliminar_sección_cola_aux(texto[1:], inicio - 1, fin - 1, resultado + texto[0])


def eliminar_final_cola(indice, texto):
    """
    Elimina el final de un texto según un índice
    E: Un texto y un número.
    S: Un texto sin el final
    R: Texto tipo str, índice entero positivo.
    """
    if type(texto) != str:
        return "Error 01"
    elif type(indice) != int or indice < 0:
        return "Error 02"
    else:
        return eliminar_final_cola_aux(indice, texto, "")


def eliminar_final_cola_aux(indice, texto, respuesta):
    # Función auxiliar
    if indice == 0:
        return respuesta
    else:
        return eliminar_final_cola_aux(indice - 1, texto[1:], respuesta + texto[0])


def juntar_asteriscos(número, respuesta):
    # Función auxiliar, devuelve str con el número de asteriscos
    if número == 0:
        return respuesta
    else:
        return juntar_asteriscos(número - 1, respuesta + "* ")


def dibujar_rectángulo_cola(largo, ancho):
    """
    Dibuja un rectángulo con asteriscos
    E: la largo y ancho, como números enteros
    S: Un string con el rectángulo
    R: deben ser números enteros positivos
    """
    if type(largo) != int or type(ancho) != int:
        return "Error 0"
    else:
        return dibujar_rectángulo_cola_aux(largo, ancho, "")


def dibujar_rectángulo_cola_aux(largo, ancho, rectángulo):
    # Función auxiliar
    if ancho == 0:
        return rectángulo
    else:
        return dibujar_rectángulo_cola_aux(largo, ancho - 1, rectángulo + "\n" + juntar_asteriscos(largo, ""))


def unir_elementos(lista, elemento, respuesta):
    """
    Función auxiliar
    """

    if lista == []:
        return respuesta
    else:
        return unir_elementos(lista[1:], elemento, respuesta + [[elemento] + [lista[0]]])


def permutaciones_cola(lista1, lista2):
    """
    Permuta dos listas
    E: Dos listas
    S: Una lista de listas
    R: Lista tipo list
    """
    if type(lista1) != list or type(lista2) != list:
        return "Error 0"
    else:
        return permutaciones_cola_aux(lista1, lista2, [])


def permutaciones_cola_aux(lista1, lista2, respuesta):
    # Función auxiliar
    if lista1 == []:
        return respuesta
    else:
        return permutaciones_cola_aux(lista1[1:], lista2, respuesta + unir_elementos(lista2, lista1[0], []))
