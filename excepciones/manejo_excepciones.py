
def operaciones_archivo():
    try:
        archivo = open("mi_archivoException.txt", "r")
        contenido = archivo.read()
        print("Contenido del archivo:", contenido)
    except FileNotFoundError:
        print("¡Error! El archivo no existe.")
    except Exception as e: # Captura cualquier otra excepción
        print(f"Ocurrió un error inesperado: {e}")
    finally:
        if 'archivo' in locals() and not archivo.closed:
            archivo.close()
            print("El archivo ha sido cerrado (desde finally).")
            

operaciones_archivo()