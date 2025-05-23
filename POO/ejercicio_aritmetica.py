class Aritmetica:
    
    def __init__(self, operando1, operando2):
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
    
    Operacin1 =Aritmetica(5, 7)
    
    print(f'La suma de {Operacin1.operando1} + {Operacin1.operando2} es: {Operacin1.sumar()}')
    print(f'La resta de {Operacin1.operando1} - {Operacin1.operando2} es: {Operacin1.restar()}')
    print(f'La multiplicacion de {Operacin1.operando1} * {Operacin1.operando2} es: {Operacin1.multiplicar()}')
    print(f'La division de {Operacin1.operando1} / {Operacin1.operando2} es: {int(Operacin1.dividir())}') 
