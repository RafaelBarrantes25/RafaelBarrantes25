def verificar_números(lista):
    número = 0
    while número < len(lista):
        if type(lista[número]) != int:
            return False
        else:
            número+=1
    return True


def verificar_ordenados(lista):
    número = 1
    while número < len(lista):
        if lista[número-1] > lista[número]:
            return False
        número += 1

    return True




def búsqueda_binaria(lista,número):


    max = len(lista)-1
    min = 0

    while min <= max:
        med = (max+min) // 2
        if lista[med] == número:
            return med
        elif lista[med] < número:
            min = med+1
        else:
            max = med-1




def invertir_txt(texto):

    texto2 = ""
    num = len(texto)-1


    while num >= 0:
        texto2 += texto[num]
        num -= 1
    return texto2

print(invertir_txt("hola"))
