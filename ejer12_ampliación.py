def iguales(lista1,lista2):
    if lista1 == lista2:
        return True
    elif lista1 > lista2:
        return 'Lista1 es mayor'
    else:
        return 'Lista2 es mayor'
    
    
    

lista1 = [3,6,8,3]
lista2 = [4,8,3,2]
print(iguales(lista1,lista2))
        