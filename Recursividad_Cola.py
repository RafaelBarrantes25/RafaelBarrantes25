from prueba3 import invertir_num


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


#-------------------------------------------------------------------


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


#-------------------------------------------------------------------


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


#-------------------------------------------------------------------


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
    if num == invertir_num(num):
        return True
    else:
        return False

print(f"Número palíndromo: {número_palíndromo(123454321)}")