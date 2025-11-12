def iguales(lista1,lista2):
   return sorted (lista1) == sorted(lista2)

lista1 = [5,3,6,8]
lista2 = [0,3,2,6]
print(iguales(lista1,lista2))