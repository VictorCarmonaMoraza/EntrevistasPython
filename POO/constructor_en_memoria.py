#Defincion de una clase 
class Persona:
    
    #Constructor
    def __init__(self, nombre, apellido):
        #Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido
        
    def mostrar_persona(self):
        print(f'''Persona:
              Nombre:{self.nombre}
              Apellido:{self.apellido}''')
        print(f'Direccion de memoria self: {hex(id(self))}')
        

#Cracion de un objeto
if __name__ == '__main__':
    print('*** ----------------------- Creacion de Persona 1 ----------------***')
    #Creamos un objeto
    persona1 = Persona('Juan', 'Pérez') #Crea un objeto en memoria
    persona1.mostrar_persona() #Llamamos al metodo mostrar_persona
    #Obtener la direccions de memoria del objeto
    #print(f'Direccion de memoria del objeto persona1: {hex(id(persona1))}')