# Ejercicio 19: Comparacion de arrays
lista_a = [10, 20, 30]
lista_b = [10, 20, 30]
lista_c = [30, 20, 10] # Mismos elementos, orden diferente
lista_d = [10, 20]     # Longitud diferente

print(f"A == B: {lista_a == lista_b}") # True
print(f"A == C: {lista_a == lista_c}") # False (el orden importa)
print(f"A == D: {lista_a == lista_d}") # False (la longitud importa)

#TODO: Algoritmo que dice si dos arrays son iguales
def iguales(lista1, lista2):
    #Comparo la longitud
    longitud1 = len(lista1)
    longitud2 = len(lista2)
    if longitud1 != longitud2:
        return False
    #Recorro el array
    for i in range(len(lista1)):
        if lista1[i] != lista2[i]:
             return False
    return True  
    
    
