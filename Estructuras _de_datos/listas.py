
#Creamos una lista 
#Una lista es una colección de elementos ordenados y mutables.
#Las listas pueden contener elementos duplicados y se pueden modificar después de haberlas creado.
#Las listas son útiles para almacenar datos que pueden cambiar a lo largo del tiempo.
#Agregar elementos con .append()
#Eliminar elementos con .remove() o .pop()
#Modificar el contenido de la lista después de haberla creado
#Recorrer la lista con un for
#Recorrer la lista con un while

lista = ["rojo", "verde", "azul", "amarillo", "rojo"]
print("------Recorremos la lista con un for------")
#Recorremos la lista
for color in lista:
    print(color)

print("-------------------------CASO 2------------------------------")
mi_listafrutas = ["manzana", "banana", "cereza", "dátil"]

for i in range(len(mi_listafrutas)):
    elemento = mi_listafrutas[i]
    print(f"El elemento '{elemento}' está en la posición (índice) {i}")

print("-------------------------CASO 3------------------------------")
mi_lista = ["rojo", "verde", "azul", "amarillo"]
print("--- Recorriendo con enumerate() ---")
for indice, valor in enumerate(mi_lista):
    if valor == "verde":
        print(f"este color es {valor} y esta en la posicion {indice}")
    else:
        print(f"Índice: {indice}, Valor: {valor}")

