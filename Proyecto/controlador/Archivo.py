class Archivo():

    def __init__(self):
        pass

    def __cargar__(self,ruta,lista_error,lista_token):
        ruta = str(input('Ingrese la Ruta del Archivo: '))
        try:
        
            archivo = open(f"{ruta}","r")
            texto = archivo.readlines()
            archivo.close()
            print(texto)
            
        except (FileNotFoundError):
            print("Error")