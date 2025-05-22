# Creacion de una tupla
# Una tupla es una colección de elementos ordenados e inmutables.
# Se pueden crear tuplas con paréntesis () o sin ellos.
# Son mas rapidas que las listas y se utilizan para almacenar datos que no deben cambiar.
# Consumnen menos memoria que las listas.
frutas_tuplas = ("manzana", "banana", "naranja")


print("------Recorremos la tupla con un for------")
#Recorremos la tupla
for fruta in frutas_tuplas:
    print(fruta)


print("------CASO 2-----")
mi_tupla = ("rojo", "verde", "azul", "amarillo")

print("--- Recorriendo por índice con range(len()) ---")
for i in range(len(mi_tupla)):
    print(f"Elemento en el índice {i}: {mi_tupla[i]}")
    

print("------CASO 3-----")
mi_tupla = (10, 20, 30, 40, 50)

print("--- Recorriendo con enumerate() ---")
for indice, valor in enumerate(mi_tupla):
    print(f"Índice: {indice}, Valor: {valor}")
    

print("------CASO 4-----")
try:
    mi_tupla = (10, 20, 30, 40, 50)
    mi_tupla[0]=45
except TypeError as e:
    print(f"Error: {e}")
    print("Las tuplas son inmutables: no puedes modificar sus elementos una vez creadas.")
finally:
    print(f"Estas es la tupla: {mi_tupla}")
    

print("------CASO 5-----")
try:
    mi_tupla2= (10, 20, 30, 40, 50)
    mi_tupla2.append(60)
except AttributeError as e:
    print(f"Error: {e}")
    #print("Las tuplas son inmutables: no puedes modificar sus elementos una vez creadas.")
finally:
    print(f"Estas es la tupla: {mi_tupla2}")

