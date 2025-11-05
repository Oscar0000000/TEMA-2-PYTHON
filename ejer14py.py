inventario = ["Manzanas", "Plátanos", "Naranjas", "Peras"]
#Llega mercancia uvas y kiwis
inventario.append("uvas")
inventario.append("kiwis")

#Llega caja grande melones unirla
melones = ["melon"]
inventario.extend(melones)

#Reordenamiento

inventario.insert(2, "platanos frescos")

#Vender melones
producto_vendido = inventario.pop(-1)

#Eliminar peras
inventario.remove("Peras")

#Reporte emergencia los 4 primeros
emergencia = inventario[0:4]

for e in emergencia:
    print(e)

print(inventario)
print(producto_vendido)