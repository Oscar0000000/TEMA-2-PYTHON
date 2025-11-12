def busqueda(numeros,clave):
    for i in range(len(numeros)):
        if numeros[i]==clave:
            return i
        i +=1
    return -1

numeros = [2,6,7,9,1,3]
clave = 9
print(busqueda(numeros,clave))
