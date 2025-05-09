def verificar_numéricos(string, string2=""):
    """
    Verifica si el input es un número
    E: un string
    S: si es un número, lo pasa a la función verificar_elegir
    si no, dice eso
    R: nada
    """
    if string == "":
        return string2
    elif string[0] == "0" or string[0] == "1" or string[0] == "2" or string[0] == "3" or string[0] == "4" or string[0] == "5" or string[0] == "6" or string[0] == "7" or string[0] == "8" or string[0] == "9":
        return verificar_numéricos(string[1:], string2+string[0])
    else:
        return "JAJAJEJE"


