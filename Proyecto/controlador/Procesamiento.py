class Procesamiento():

    def __init__(self):
        self.archivo = None


    def procesar_datos(self,documento):
        self.archivo = documento

        print('\nMatriz Frecuencia Parte 1')
        self.archivo.lista_nombre.mostrar()
        print('\nMatriz Frecuencia Parte 2')
        self.archivo.lista_frecuencia.mostrar() 
        print('\nMatriz Frecuencia Parte 3')
        self.archivo.lista_acceso.mostrar()
        print('\nMatriz Frecuencia Parte 4 ------- GRUPOS')
        self.archivo.lista_grupos.mostrar()

        print()
        
        