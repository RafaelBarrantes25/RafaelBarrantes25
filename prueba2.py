def prueba(lista1,lista2):
    if lista1 == []:
        return []
    elif lista1[0] != lista2[0]:
        return [lista1[0]]+prueba(lista1[1:],lista2)
    else:
        return blaps(lista1[1:],lista2)

def blaps(lista1,lista2):
    if lista2 == []:
        return lista1
    else:
        return blaps(prueba(lista1,lista2),lista2[1:])

print(prueba([1,2,3,4],[2,3,6]))



