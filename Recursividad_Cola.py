
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
        pass

#print(f"Dibujar rectángulo:\n{dibujar_rectángulo(10,5)}")




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



