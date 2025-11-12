def iguales(lista1, lista2):
    if len(lista1) != len(lista2):
        return False
    for i in range(len(lista1)):
        if lista1[i] != lista2[i]:
            return False 
    return True

lista1 = [3,6,8,3]
lista2 = [4,8,3,2]
print(iguales(lista1,lista2))
