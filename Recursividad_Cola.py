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

print(elim_digi(12345,3))