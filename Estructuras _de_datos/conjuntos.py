
#Declaramos un conjunto
#Un conjunto es una colección de elementos no ordenados y sin duplicados.
#Los conjuntos son útiles para eliminar duplicados de una lista o para realizar operaciones matemáticas como la unión, intersección y diferencia.
#Agregar elementos con .add()

#Eliminar elementos con .remove() o .discard()

#Modificar el contenido del conjunto después de haberlo creado
print("<--------------CASO 1----------------->")
#El color rojo se repite, pero solo se guardara una vez.
conjunto= {"rojo", "verde", "azul", "amarillo", "rojo"}

print("------Recorremos el conjunto con un for------")
#Recorremos el conjunto
for color in conjunto:
    print(color)

print("<--------------CASO 2----------------->")
conjunto2= {"rojo", "verde", "azul", "amarillo", "rojo"}
conjunto2.add("morado")
print("------Recorremos el conjunto con un for------")
#Recorremos el conjunto
for color in conjunto2:
    print(color)