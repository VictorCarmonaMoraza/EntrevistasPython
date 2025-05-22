
#Defincion de una clase
class Persona:
    
    def inicializar_persona(self, nombre, apellido):
        #Creamos los atributos de la clase
        self.nombre = nombre
        self.apellido = apellido
        
    def mostrar_persona(self):
        print(f'''Persona:
              Nombre:{self.nombre}
              Apellido:{self.apellido}''')
        

#Cracion de un objeto
#Si estamos dentro este mismo archivo
if __name__ == '__main__':
    print('*** ----------------------- Creacion de Persona 1 ----------------***')
    #Creamos un objeto
    persona1 = Persona() #Crea un objeto vacio en memoria
    persona1.inicializar_persona('Juan', 'Pérez') #Llamamos al metodo inicializar_persona
    persona1.mostrar_persona() #Llamamos al metodo mostrar_persona

print('*** ----------------------- Creacion de Persona 2 ----------------***')
persona2 = Persona() #Crea un objeto vacio en memoria
persona2.inicializar_persona('Ana', 'Gómez') #Llamamos al metodo inicializar_persona
persona2.mostrar_persona() #Llamamos al metodo mostrar_persona

