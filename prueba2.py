def resta_conjuntos(lista1,lista2):
    if lista1 == []:
        return []
    elif lista1[0] != lista2[0]:
        return [lista1[0]]+resta_conjuntos(lista1[1:],lista2)
    else:
        return resta_conjuntos_aux(lista1[1:],lista2)

def resta_conjuntos_aux(lista1,lista2):
    if lista2 == []:
        return lista1
    else:
        return resta_conjuntos_aux(resta_conjuntos(lista1,lista2),lista2[1:])

print(resta_conjuntos([1,2,3,4],[2,3,6]))



