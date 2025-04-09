def sacar_vocales(texto):
    if texto == "":
        return []
    elif texto[0] == "a" or texto[0] == "e" or texto[0] == "i" or texto[0] == "o" or texto[0] == "u":
        return [texto[0]]+sacar_vocales(texto[1:])
    else:
        return sacar_vocales(texto[1:])
print(sacar_vocales("sapo azul y verde"))


