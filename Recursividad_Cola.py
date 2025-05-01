
def cuenta_digito(num):
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
        return cuenta_digito_aux(num,0)

def cuenta_digito_aux(num,cant):
    #Función auxiliar
    if num == 0:
        return cant
    else:
        return cuenta_digito_aux(num//10,cant+1)

print(f"Cuenta dígitos: {cuenta_digito(364773)}")


#-------------------------------------------------------------------


def factorial(número):
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
        return factorial_aux(número,1)

def factorial_aux(número, resultado):
    # Función auxiliar
    if número == 0:
        return resultado
    else:
        return factorial_aux(número - 1, número * resultado)

print(f"Factorial: {factorial(5)}")


#-------------------------------------------------------------------


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

print(f"Máximo común divisor: {mcd(12,8)}")




def elim_digi(número, dígito):
    """
    Elimina un dígito de un número más largo
    E: El número y el dígito, enteros positivos
    S: El número sin el dígito
    R: tienen que ser enteros positivos, dígito debe ser más corto
    """
    if type(número) != int or type(dígito) != int:
        return "Error 0"
    elif dígito >= 10 or dígito < 0:
        return "Error 1"
    elif número < 0:
        return "Error 2"
    else:
        return elim_digi_aux(número,dígito,1,0)

def elim_digi_aux(número,dígito,número_nuevo,extra):
    """
    función auxiliar
    """
    if número == 0:
        return extra
    elif número % 10 == dígito:
        return elim_digi_aux(número//10,dígito,número_nuevo,extra)
    else:
        return elim_digi_aux(número//10,dígito,número_nuevo*10,extra+(número%10)*número_nuevo)

print(f"Elimina dígito: {elim_digi(12345,3)}")




def inv_num(num):
    """
    invierte número entero positivo
    E: número
    S: número invertido
    R: entero positivo número
    """
    if type(num) != int:
        return "Error 0"
    elif num < 0:
        return "Error 1"
    else:
        return inv_num_aux(num,10**(cuenta_digito(num)-1),0)

def inv_num_aux(num,potencia,result):
    """
    función auxiliar
    """
    if num == 0:
        return result
    else:
        return inv_num_aux(num//10,potencia//10,result+(num%10)*potencia)

print(f"Invertir número: {inv_num(12345)}")




def número_palíndromo(num):
    """
    Revisa si un número es palíndromo
    E: número
    S: True o False, dependiendo si es palíndromo o no
    R: debe ser número entero positivo
    """
    if type(num) != int:
        return "Error 0"
    elif num < 0:
        return "Error 1"
    else:
        return número_palíndromo_aux(num)

def número_palíndromo_aux(num):
    #Función auxiliar
    if num == inv_num(num):
        return True
    else:
        return False

print(f"Número palíndromo: {número_palíndromo(123454321)}")


def contar_elementos(lista):
    """
    Cuenta los elementos de una lista
    E: una lista
    S: el número de elementos
    R: la lista debe ser tipo
    """
    if type(lista) != list:
        return "Error 0"
    else:
        return contar_elementos_aux(lista,0)

def contar_elementos_aux(lista, respuesta):
    #Función auxiliar
    if lista == []:
        return respuesta
    else:
        return contar_elementos_aux(lista[1:], respuesta+1)

print(f"Contar elementos: {contar_elementos(["a",1,5,"b"])}")




def juntar_elementos(lista, elemento, respuesta):
    """
    Crea una lista con listas con un elemento junto con cada elemento
    E: una lista y un elemento
    S: Una lista con listas
    R: Lista debe ser tipo list

    Es una función auxiliar, por lo que no lleva validaciones
    """

    if lista == []:
        return respuesta
    else:
        return juntar_elementos(lista[1:], elemento, respuesta+[elemento,lista[0]])


def juntar_asteriscos(número,respuesta):
    #Función auxiliar, devuelve str con el número de asteriscos
    if número == 0:
        return respuesta
    else:
        return juntar_asteriscos(número-1,respuesta+"* ")

def dibujar_rectángulo(base,altura):
    """
    Dibuja un rectángulo con asteriscos
    E: la base y altura, como números enteros
    S: Un string con el rectángulo
    R: deben ser números enteros positivos
    """
    if type(base) != int or type(altura) != int:
        return "Error 0"
    else:
        return dibujar_rectángulo_aux(base,altura,"")

def dibujar_rectángulo_aux(base,altura,rectángulo):
    #Función auxiliar
    if altura == 0:
        return rectángulo
    else:
        return dibujar_rectángulo_aux(base,altura-1,rectángulo+"\n"+juntar_asteriscos(base,""))

print(f"Dibujar rectángulo:{dibujar_rectángulo(10,5)}")




def eliminar_final(texto,índice):
    """
    Elimina el final de un texto usando recursividad de cola
    a partir de un índice
    E: texto y el índice
    S: el texto sin el final
    R: texto tipo str, índice tipo int
    """
    if type(texto) != str:
        return "Error 0"
    elif type(índice) != int:
        return "Error 1"
    else:
        return eliminar_final_aux(texto,índice,"")


def eliminar_final_aux(texto, índice, respuesta):
    #Función auxiliar
    if texto == "":
        return respuesta
    if índice == 0:
        return respuesta
    else:
        return eliminar_final_aux(texto[1:],índice-1,respuesta+texto[0])




def buscar_texto(textoG,textoC):
    """
    Busca un texto corto dentro de uno más largo
    E: Un texto largo y uno corto
    S: True o False
    R: textos deben ser tipo string
    """
    if type(textoG) != str or type(textoC) != str:
        return "Error 0"
    else:
        return buscar_texto_aux(textoG,textoC)

def buscar_texto_aux(textoG,textoC):
    #Función auxiliar
    if textoG == "":
        return False
    elif eliminar_final(textoG,len(textoC)) == textoC:
        return True
    else:
        return buscar_texto_aux(textoG[1:],textoC)


print(f"Buscar texto: {buscar_texto_aux("Sapo verde to you","verde")}")



def eliminar_sección(texto,inicio,fin):
    """
    Elimina una sección de un texto
    E: un texto, y números con el rango que se va a eliminar
    S: El texto con la sección eliminada
    R: texto debe ser tipo string, inicio y fin deben ser int
    """
    if type(texto) != str or type(inicio) != int or type(fin) != int:
        return "Error 0"
    elif inicio > fin:
        return "Error 1"
    else:
        return eliminar_sección_aux(texto,inicio,fin,"")

def eliminar_sección_aux(texto,inicio,fin,resultado):
    #Función auxiliar
    if fin == 0:
        return resultado+texto[1:]
    elif inicio <= 0:
        return eliminar_sección_aux(texto[1:], inicio, fin-1, resultado)
    else:
        return eliminar_sección_aux(texto[1:], inicio-1, fin-1, resultado+texto[0])


print(f"Eliminar sección: {eliminar_sección("Hola, cómo está Eduardo",4,14)}")



def contar_vocales(texto):
    """
    Cuenta las vocales de un texto
    E: texto
    S: número de vocales
    R: texto debe ser tipo string
    """
    if type(texto) != str:
        return "Error 0"
    else:
        return contar_vocales_aux(texto,["A","E","I","O","U",
                                         "a","e","i","o","u",
                                         "Á","É","Í","Ó","Ú",
                                         "á","é","í","ó","ú",
                                         "Ü","ü"],0)


def comparar(texto,lista):
    #verifica si un str pertenece a una lista
    if lista == []:
        return False
    elif texto == lista[0]:
        return True
    else:
        return comparar(texto,lista[1:])

def contar_vocales_aux(texto,vocales,respuesta):
    #función auxiliar
    if texto == "":
        return respuesta
    elif comparar(texto[0],vocales) == True:
        return contar_vocales_aux(texto[1:],vocales,respuesta+1)
    else:
        return contar_vocales_aux(texto[1:],vocales,respuesta)


print(f"Contar vocales: {contar_vocales("No le crean nada a ese mae")}")



def invertir_texto(texto):
    """
    Invierte un texto
    E: texto
    S: el texto al revés
    R: debe ser tipo str
    """
    if type(texto) != str:
        return "Error 0"
    else:
        return invertir_texto_aux(texto,"")

def invertir_texto_aux(texto,respuesta):
    if texto == "":
        return respuesta
    else:
        return invertir_texto_aux(texto[1:],texto[0]+respuesta)

print(f"Invertir texto: {invertir_texto("Buenas tardes")}")

def palíndromo_texto(texto):
    """
    Revisa si un texto es palíndromo o no
    E: texto
    S: True o False
    R: debe ser tipo str
    """
    if type(texto) != str:
        return "Error 0"
    elif texto == invertir_texto(texto):
        return True
    else:
        return False

print(f"Palíndromo texto: {palíndromo_texto("reconocer")}")


def extraer_pares(lista):
    """
    Cuenta los elementos pares de una lista
    E: lista
    S: lista de pares
    R: lista debe ser tipo list
    """
    if type(lista) != list:
        return "Error 0"
    else:
        return extraer_pares_aux(lista, [])

def extraer_pares_aux(lista,respuesta):
    #Función auxiliar
    if lista == []:
        return respuesta
    elif type(lista[0]) != int:
        return extraer_pares_aux(lista[1:],respuesta)
    elif lista[0]%2 == 0:
        return extraer_pares_aux(lista[1:],respuesta+[lista[0]])
    else:
        return extraer_pares_aux(lista[1:],respuesta)


print(f"Extraer pares: {extraer_pares([1,2,"buenas",3,4,5,"a"])}")



def extraer_impares(lista):
    """
    Cuenta los elementos impares de una lista
    E: lista
    S: lista de impares
    R: lista debe ser tipo list
    """
    if type(lista) != list:
        return "Error 0"
    else:
        return extraer_impares_aux(lista, [])

def extraer_impares_aux(lista,respuesta):
    #Función auxiliar
    if lista == []:
        return respuesta
    elif type(lista[0]) != int:
        return extraer_impares_aux(lista[1:],respuesta)
    elif lista[0]%2 != 0:
        return extraer_impares_aux(lista[1:],respuesta+[lista[0]])
    else:
        return extraer_impares_aux(lista[1:],respuesta)


print(f"Extraer impares: {extraer_impares([1,2,"buenas",3,4,5,"a"])}")



def invertir_lista(lista):
    """
    Invierte una lista
    E: lista
    S: lista invertida
    R: debe ser tipo list
    """
    if type(lista) != list:
        return "Error 0"
    else:
        return invertir_lista_aux(lista,[])

def invertir_lista_aux(lista,respuesta):
    #Función auxiliar
    if lista == []:
        return respuesta
    else:
        invertir_lista_aux(lista[1:],[lista[0]]+respuesta)


print(f"Invertir lista: {invertir_lista([1,2,"buenas",3,4,"a"])}")



def escalar_vector(número,lista):
    """
    Multiplica un escalar por todos los elementos de la lista
    E: número y lista
    S: lista escalada
    R: debe ser tipo list y el número int o float
    """
    if type(lista) != list:
        return "Error 0"
    elif type(número) != int and type(número) != float:
        return "Error 1"
    else:
        return escalar_vector_aux(número,lista,[])

def escalar_vector_aux(número, lista, respuesta):
    #Función auxiliar
    if lista == []:
        return respuesta
    else:
        return escalar_vector_aux(número,lista[1:],respuesta+[lista[0]*número])


print(f"Escalar vector: {escalar_vector(5,[1,2,3,4,5])}")


def dibujar_triángulo(número):
    """
    Dibuja un triángulo de asteriscos
    E: número
    S: triángulo de asteriscos
    R: debe ser tipo int positivo
    """
    if type(número) != int:
        return "Error 0"
    else:
        return dibujar_triángulo_aux(número,"",0)

def dibujar_triángulo_aux(número,triángulo,espacios):
    #Función auxiliar
    if número == 0:
        return triángulo
    else:
        return dibujar_triángulo_aux(número-1," "*espacios+juntar_asteriscos(número,"")+"\n",espacios+1)

print(f"Triángulo:\n{dibujar_triángulo(5)}")




def contar_apariciones(número,dígito):
    """
    Cuenta las apariciones de un dígito en un número
    E: número y dígito
    S: número de veces
    R: int positivo, dígito debe ser solo 1
    """
    if type(número) != int:
        return "Error 0"
    elif type(dígito) != int or dígito < 0 or dígito > 9:
        return "Error 1"
    else:
        return contar_apariciones_aux(número,dígito,0)

def contar_apariciones_aux(número, dígito, resultado):
    #Función auxiliar
    if número == 0:
        return resultado
    elif número % 10 == dígito:
        return contar_apariciones_aux(número//10,dígito,resultado+1)
    else:
        return contar_apariciones_aux(número//10,dígito,resultado)

print(f"Contar apariciones: {contar_apariciones(12345613243,4)}")


def pertenece(lista,elemento):
    """
    Verifica si un elemento pertenece a una lista
    E: elemento y lista
    S: true o false
    R: tipo list
    """
    if type(lista) != list:
        return "Error 0"
    else:
        return pertenece_aux(lista,elemento)

def pertenece_aux(lista,elemento):
    #Función auxiliar
    if lista == []:
        return False
    elif lista[0] == elemento:
        return True
    else:
        return pertenece_aux(lista[1:],elemento)




def suma_conjuntos(lista1,lista2):
    """
    Une 2 conjuntos
    E: dos listas
    S: una lista
    R: deben ser tipo list
    """
    if type(lista1) != list or type(lista2) != list:
        return "Error 0"
    else:
        return suma_conjuntos_aux(lista1,lista2)

def suma_conjuntos_aux(lista1,lista2):
    #Función auxiliar
    if lista2 == []:
        return lista1
    elif pertenece(lista1,lista2[0]):
        return suma_conjuntos_aux(lista1,lista2[1:])
    else:
        return suma_conjuntos_aux(lista1+[lista2[0]],lista2[1:])


print(f"Suma conjuntos: {suma_conjuntos([1,2,"buenas",3,4,"a"],[2,5,777,345,"Navidad feliz"])}")


def separar_pares_impares(lista):
    """
    Crea una lista con 2 listas, una de pares y una de impares
    E: lista
    S: lista con listas
    R: tipo list
    """
    if type(lista) != list:
        return "Error 0"
    else:
        return [extraer_impares(lista)]+[extraer_pares(lista)]


print(f"Separar pares impares: {separar_pares_impares([1,5,3,2,2,6,765,554])}")



def verificar_elementos(lista):
    """
    Verifica que los elementos de una lista sean números
    E: lista
    S: True o False
    R: tipo list
    """
    if type(lista) != list:
        return "Error 0"
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




def contar_impares(lista):
    """
    Cuenta la cantidad de números impares
    E: lista
    S: número de impares
    R: tipo list
    """
    if type(lista) != list:
        return "Error 0"
    elif verificar_elementos(lista) == False:
        return "Error 1"
    else:
        return contar_impares_aux(lista,0)


def contar_impares_aux(lista, respuesta):
    #Función auxiliar
    if lista == []:
        return respuesta
    elif lista[0] %2 != 0:
        return contar_impares_aux(lista[1:],respuesta+1)
    else:
        return contar_impares_aux(lista[1:],respuesta)


print(f"Contar impares: {contar_impares([1,5,3,2,2,6,765,554])}")


def contar_apariciones_txt(texto,caracter):
    """
    Cuenta las apariciones de un caracter
    E: texto y caracter
    S: número de veces que aparece
    R: tipo str, caracter len 1
    """
    if type(texto) != str or type(caracter) != str:
        return "Error 0"
    elif caracter[1:] != "":
        return "Error 1"
    else:
        return contar_apariciones_txt_aux(texto,caracter,0)

def contar_apariciones_txt_aux(texto,caracter, resultado):
    #Función auxiliar
    if texto == "":
        return resultado
    elif texto[0] == caracter:
        return contar_apariciones_txt_aux(texto[1:],caracter,resultado+1)
    else:
        return contar_apariciones_txt_aux(texto[1:],caracter,resultado)


print(f"Contar apariciones texto: {contar_apariciones_txt("Mamá amasa la masa","a")}")

def separa_palabras(texto,caracter):
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
        return separa_palabras_aux(texto, caracter,[],"")

def separa_palabras_aux(texto,caracter,lista,respuesta):
    #Función auxiliar
    if texto == "":
        return lista
    elif texto[0] == caracter:
        return separa_palabras_aux(texto[1:], caracter, lista + [respuesta], "")
    else:
        return separa_palabras_aux(texto[1:], caracter, lista, respuesta + texto[0])

print(f"Separa palabras: {separa_palabras("Feliz día a todos","a")}")


def eliminar_espacios_cola(texto):
  """
  Esta elimina los espacios de un texto usando recursividad de cola.
  E: Un texto
  S: Un texto
  R: Texto tipo str.
  """
  if type(texto) != str:
    return "Error 01"
  else:
    return eliminar_espacios_cola_aux(texto, "")

def eliminar_espacios_cola_aux(texto, respuesta):
  """Función auxiliar de Eliminar_espacios_cola."""
  if texto == "":
    return respuesta
  elif texto[0] == " ":
    return eliminar_espacios_cola_aux(texto[1:], respuesta)
  else:
    return eliminar_espacios_cola_aux(texto[1:], respuesta + texto[0])


print(f"Eliminar espacios: {eliminar_espacios_cola("hola hola buenas tardes")}")



def eliminar_final_cola(texto, indice):
  """
  Esta elimina el final de un texto a partir de un
  indice, usando recursividad de cola.
  E: Un texto y un número.
  S: Un texto
  R: Texto tipo str, indice entero positivo.
  """
  if type(texto) != str:
    return "Error 01"
  elif type(indice) != int or indice < 0:
    return "Error 02"
  else:
    return eliminar_final_cola_aux(texto, indice, "")

def eliminar_final_cola_aux(texto, indice, respuesta):
  """Función auxiliar de eliminar_final_cola."""
  if indice == 0:
    return respuesta
  else:
    return eliminar_final_cola_aux(texto[:-1], indice - 1, texto[:-1])


print(f"Eliminar final: {eliminar_final_cola("Hola feliz día", 3)}")



def permutaciones_lista_cola(listaA, listaB):
  """
  Esto da el producto cartesiano de dos listas.
  E: Dos listas
  S: Una lista de listas
  R: Lista tipo list
  """
  if type(listaA) != list or type(listaB) != list:
    raise TypeError('Error 01')
  else:
    return permutaciones_lista_cola_aux(listaA, listaB, [])

def permutaciones_lista_cola_aux(listaA, listaB, respuesta):
  """Función auxiliar de Permutaciones_lista_cola."""
  if listaA == []:
    return respuesta
  else:
    return permutaciones_lista_cola_aux(listaA[1:], listaB, respuesta + juntar_elementos(listaB, listaA[0], []))


print(f"Permutaciones: {permutaciones_lista_cola([1,2,3,4],[4,3,2,1])}")

