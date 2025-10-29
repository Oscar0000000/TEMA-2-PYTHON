#PEDIR CUANTOS NUMEROS INTRODUCIR Y POR TECLADO INTRODUCIR ESA CANTIDAD DE NUMEROS ENTEROS Y MOSTRAR EN ORDEN INVERSO AL INTRODUCIDO
cantidad = int(input("Cuantos numeros vas a introducir:"))
n = []  #CREO UNA LISTA VACIA PARA IR GUARDANDO LOS NUMEROS
for i in range (cantidad): #PIDO LOS NUMEROS UNO POR UNO
    n.append(int(input("Introduce un numero entero:")))
n.reverse() #INVIERRTE EL ORDEN DE LA LISTA
print(n)
    
