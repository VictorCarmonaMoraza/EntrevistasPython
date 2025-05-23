class Aritmetica:
    #Python no acepta sobrecarga de constructores, pero podemos simularlo
    #def __init__(self, operando1):
        #self.operando1 = operando1
        
    
    
    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2
    
    def sumar(self):
        return self.operando1 + self.operando2
    
    def restar(self):
        return self.operando1 - self.operando2
    
    def multiplicar(self):
        return self.operando1 * self.operando2
    
    def dividir(self):
        return self.operando1 / self.operando2
    
#Ejemplo de uso
if __name__ == '__main__':
    Operacin1 = Aritmetica(5, 7)
    print(f'La suma de {Operacin1.operando1} + {Operacin1.operando2} es: {Operacin1.sumar()}')
    print(f'La resta de {Operacin1.operando1} - {Operacin1.operando2} es: {Operacin1.restar()}')
    print(f'La multiplicacion de {Operacin1.operando1} * {Operacin1.operando2} es: {Operacin1.multiplicar()}')
    # Convertir a int la división puede truncar el resultado (5/7 = 0.71 -> 0)
    print(f'La division de {Operacin1.operando1} / {Operacin1.operando2} es: {Operacin1.dividir()}') 

    print('\n*** ----------------------- Creacion de Operacion 2 ----------------***') # <-- ¡Este es el print que ves!
    Operacion2 = Aritmetica(3) # operando1=5, operando2=None
    Operacion2.operando2 = 9   # Ahora operando2=7
    print(f'La suma de {Operacion2.operando1} + {Operacion2.operando2} es: {Operacion2.sumar()}')
    print(f'La resta de {Operacion2.operando1} - {Operacion2.operando2} es: {Operacion2.restar()}')
    print(f'La multiplicacion de {Operacion2.operando1} * {Operacion2.operando2} es: {Operacion2.multiplicar()}')
    # Nota: Aquí también debes considerar la división por cero si operando2 pudiera ser 0.
    print(f'La division de {Operacion2.operando1} / {Operacion2.operando2} es: {Operacion2.dividir()}')
