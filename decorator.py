def mi_decorador(func):
    def envoltura():
        print("Antes de ejecutar la función")
        func()
        print("Después de ejecutar la función")
    return envoltura

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()


