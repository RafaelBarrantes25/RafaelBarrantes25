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

