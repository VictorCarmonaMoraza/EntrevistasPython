class Persona:
    contador_personas = 0
    
    #Constructor
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        

#Mostrar los atributos de un objeto
persona1 = Persona('Juan', 'Pérez')

#Nos devolvera un diccionario con los atributos del objeto
print(persona1.__dict__)

print("---------CASO 2---------")
# Crear un atributo al vuelo(en este momento)
persona1.contador_personas = 10
print(persona1.contador_personas)
print(persona1.__dict__)


print("---------CASO 3---------")
#Acceder a un atributo de la clase
print(Persona.contador_personas) #Accedemos al atributo de la clase
print(persona1.contador_personas) #Accedemos al atributo del objeto

print("---------CASO 4---------")
#Creacion de un nuevo objeto
persona2 = Persona('Ana', 'Gómez')
print(persona2.__dict__)
print(persona2.contador_personas) #Accedemos al atributo del objeto


print("---------CASO 5---------")
#Asociar un atribuot de clase al vuelo
Persona.contador2 = 20
print(Persona.contador2) #Accedemos al atributo de la clase