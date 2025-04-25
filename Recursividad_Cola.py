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


def NOMBRE(VARIABLE):
    """
    COMENTARIO
    E: ENTRADA
    S: SALIDA
    R: RESTRICCIONES
    """
    pass

def NOMBRE_aux(VARIABLE):
    """
    COMENTARIO
    """
    pass