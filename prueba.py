def skibidi(lista,número):
    if lista == []:
        return []
    elif lista[0] == número:
        return [lista[0]]+[número]+skibidi(lista[1:],número)
    else:
        return [lista[0]] + skibidi(lista[1:], número)

print(skibidi([1,2,3,4,5],4))



def skobodo(texto):
    if texto == "":
        return ""
    elif texto[0] == "a" or texto[0] == "e" or texto[0] == "i" or texto[0] == "o" or texto[0] == "u":
        return texto[0]+skobodo(texto[1:])
    else:
        return skobodo(texto[1:])
print(skobodo("sapo azul y verde"))