
#Funciones con números

#--------------------------------------------------------------------

#Esto cuenta cuántas veces aparece un número en otro

def cuenta_dígito(x,y):
    """
    Revisa errores
    E: Número entero positivo
    Otro número entero positivo de 1 dígito
    S: Cuántas veces se repite y en x
    R: No números negativos, y solo es de 1 dígito
    """
    if type(x) != int or type(y) != int:
        return "Error 0"
    elif x < 0 or y < 0:
        return "Error 1"
    elif y >= 10:
        return "Error 2"
    else:
        return cuenta_dígito_aux(x,y)

def cuenta_dígito_aux(x,y):
    #Cuenta cuántas veces aparece y en x
    if x == 0:
        return 0
    elif x % 10 == y:
        return 1 + cuenta_dígito_aux(x//10,y)
    else:
        return cuenta_dígito_aux(x//10,y)

print(f"Cuenta dígitos: {cuenta_dígito(1245678456783764783904,7)}")



#--------------------------------------------------------------------


#Busca el máximo común divisor entre 2 dígitos
def mcm(num1,num2):
    '''
    E: 2 números
    S: el MCM entre ambos
    R: deben ser números
    '''
    if type(num1) != int or type(num2) != int:
        return "Error 0"
    elif num1 < 0 or num2 < 0:
        return "Error 1"
    else:
        return mcm_aux(num1,num2)

def mcm_aux(num1,num2):
    """
    función auxiliar
    """
    if num1 % num2 == 0:
        return num2
    else:
        return "No hay MCM"

print(f"Máximo común divisor: {mcm(8,4)}")



#--------------------------------------------------------------------



#Calcula el Fibonacci de un númerp
def fibonacci(num):
    '''
    E: Un número
    S: El Fibonacci de ese número
    R: Tiene que ser un número
    '''
    if type(num) != int:
        return "Error 0"
    else:
        return fibonacci_aux(num)

def fibonacci_aux(num):
    """
    Función auxiliar
    """
    if num == 0 or num == 1:
        return 1
    else:
        return fibonacci_aux(num-1) + fibonacci_aux(num-2)

print(f"Fibonacci: {fibonacci(8)}")

#--------------------------------------------------------------------



#Esto calcula el largo de un texto
def largo_texto(texto):
    if type(texto) != str:
        return "Error 0"
    elif texto == "":
        return 0
    else:
        return 1 + largo_texto(texto[1:])

print(f"Largo del texto: {largo_texto("Pizza")}")



#--------------------------------------------------------------------



#Esto invierte un texto
def invertir_texto(texto):
    '''
    E: Un texto
    S: El texto al revés
    R: Tiene que ser un str
    '''
    if type(texto) != str:
        return "Error 1"
    else:
        return invertir_texto_aux(texto)


def invertir_texto_aux(texto):
    """
    Función auxiliar
    """
    if texto == "":
        return ""
    else:
        return invertir_texto_aux(texto[1:])+texto[0]

print(f"Invertir texto: {invertir_texto("Pizza")}")



#--------------------------------------------------------------------



#Esto revisa si un texto es palíndromo
def palíndromo(texto):
    '''
    E: Texto
    S: True si es palíndromo y False si no
    R: Debe ser un texto
    '''
    if invertir_texto(texto) == texto:
        return True
    else:
        return False

print(f"Palíndromo: {palíndromo("Pizza")}")



#--------------------------------------------------------------------



#Esto cuenta cuántas vocales hay en un texto
def vocales(texto):
    '''
    E: Texto
    S: Número de vocales
    R: Tiene que ser un texto
    '''
    if type(texto) != str:
        return "Error 1"
    else:
        return vocales_aux(texto)

def vocales_aux(texto):
    """
    Función auxiliar
    """
    if texto == "":
        return 0
    elif texto[0] == "a" or texto[0] == "e" or texto[0] == "i" or texto[0] == "u" or texto[0] == "A" or texto[0] == "E" or texto[0] == "I" or texto[0] == "U":
        return 1+vocales_aux(texto[1:])
    else:
        return vocales_aux(texto[1:])

print(f"Vocales: {vocales('Pizza')}")



#--------------------------------------------------------------------



#Esto elimina el final a partir de una posición dada
def elim_final(texto,posición):
    '''
    E: Texto y la posición a partir de la cual se va a eliminar
    S: El texto sin el final
    R: El texto debe ser un str, la posición debe ser número,
    no puede ser mayor a la longitud del texto
    '''
    if type(texto) != str or type(posición) != int:
        return "Error 1"
    elif largo_texto(texto) < posición-1:
        return "Error 2"
    else:
        elim_final_aux(texto,posición)


def elim_final_aux(texto,posición):
    """
    Funcion auxiliar
    """
    pass



#--------------------------------------------------------------------



#Esto multiplica escalar por vector
def escalar_vector(escalar,vector):
    """
    E: Un número escalar y una lista vector
    S: La lista escalada
    R: Número y lista
    """
    if type(escalar) != int or type(vector) != list:
        return "Error 0"
    else:
        return escalar_vector_aux(escalar,vector)

def escalar_vector_aux(escalar,vector):
    """
    Función auxiliar
    """
    if vector == []:
        return []
    else:
        return [escalar * vector[0]] + escalar_vector_aux(escalar,vector[1:])

print(f"Escalar vector: {escalar_vector(2,[1,2,3,4,5])}")



#--------------------------------------------------------------------





#COMENTARIO
def triángulo(num):
    """
    COMENTARIO
    E: ENTRADA
    S: SALIDA
    R: RESTRICCIONES
    """
    if type(num) != int:
        return "Error 0"
    else:
        return triángulo_aux(num)

def triángulo_aux(num, num2=0):
    """
    COMENTARIO
    """
    if num == 0:
        return ""
    elif num > 0:
        return num2 * " " + num * "* " + "\n" + triángulo_aux(num-1, num2+1)
print(triángulo(4))




#COMENTARIO
def rectangulo(base,altura):
    '''
    COMENTARIO
    E: ENTRADA
    S: SALIDA
    R: RESTRICCIONES
    '''
    if type(base) != int or type(altura) != int:
        return "Error 0"
    elif base < 0 or altura < 0:
        return "Error 1"
    else:
        return rectangulo_aux(base,altura)




def rectangulo_aux(base,altura):
    """
    COMENTARIO
    """
    if base == 0 or altura == 0:
        return ""
    elif altura > 0:
        return "* " * base + "\n" + rectangulo_aux(base,altura-1)
    else:
        return "* " * base + rectangulo_aux(base,altura)


print(rectangulo(5,4))



#COMENTARIO
def encontrar_texto(texto1, texto2):
    """
    COMENTARIO
    E: ENTRADA
    S: SALIDA
    R: RESTRICCIONES
    """
    if type(texto1) != str or type(texto2) != str:
        return "Error 0"
    else:
        return encontrar_texto_aux(texto1+" ", texto2)

def encontrar_texto_aux(texto1, texto2):
    """
    COMENTARIO
    """
    if texto2 == "":
        return True
    elif texto1 == "":
        return False
    elif texto2[0] == texto1[0]:
        return encontrar_texto_aux(texto1[1:], texto2[1:])
    else:
        return encontrar_texto_aux(texto1[1:], texto2)


print(encontrar_texto_aux("Sgregr", "grer"))




#COMENTARIO
def NOMBRE(VARIABLE):
    '''
    COMENTARIO
    E: ENTRADA
    S: SALIDA
    R: RESTRICCIONES
    '''
    pass

def NOMBRE_aux(VARIABLE):
    """
    COMENTARIO
    """
    pass
