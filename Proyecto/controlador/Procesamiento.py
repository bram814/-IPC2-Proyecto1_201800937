from modelos.Lista_Circular import Lista_Circular

class Procesamiento():

    def __init__(self):
        self.archivo = None
        self.lista_reducida = Lista_Circular()


    def procesar_datos(self,documento):
        self.archivo = documento

        self.__inicio_reducida__()
        self.arreglar_fila_reducida()

        print('\nMatriz Frecuencia Parte 1')
        self.archivo.lista_nombre.mostrar()
        print('\nMatriz Frecuencia Parte 2')
        self.archivo.lista_frecuencia.mostrar() 
        print('\nMatriz Frecuencia Parte 3')
        self.archivo.lista_acceso.mostrar()
        print('\nMatriz Frecuencia Parte 4 ------- GRUPOS')
        self.archivo.lista_grupos.mostrar()
        print('\nMatriz REDUCIDA Parte 5 ------- REDUCIDA')
        self.lista_reducida.mostrar()

        print()
        
        

    def __inicio_reducida__(self):

        

        i = 0
        nodo_frecuencia = self.archivo.lista_grupos.get_cabeza()

        while i < self.archivo.lista_grupos.size:

            nodo_nombre = self.archivo.lista_nombre.get_cabeza()
            j = 0

            while j < self.archivo.lista_nombre.size:
                if (nodo_nombre.get_estado() == True):
                    if (int(nodo_frecuencia.get_contador()) == int(nodo_nombre.get_contador())):

                        x = 0
                        nodo_actual = self.archivo.lista_frecuencia.get_cabeza()
                        while x < self.archivo.lista_frecuencia.size:

                            if int(nodo_actual.get_contador()) == int(nodo_frecuencia.get_contador()):
                                if int(nodo_frecuencia.get_frecuencia()) == int(nodo_actual.get_frecuencia()):
                                    
                                    dato = self.buscar_nodo(nodo_actual.get_contador(),nodo_actual.get_y(),nodo_actual.get_frecuencia())

                                    if (self.validar_posicion(nodo_actual.get_contador(),nodo_actual.get_y(),nodo_actual.get_frecuencia())==False):
                                        self.lista_reducida.agregar(nodo_actual.get_contador(),nodo_actual.get_x(),nodo_actual.get_y(),int(dato),nodo_nombre.get_estado())
                                        self.agregar_frecuencia(nodo_actual.get_contador(),nodo_actual.get_x(),nodo_actual.get_y(),nodo_actual.get_frecuencia())
                                    
                            nodo_actual = nodo_actual.get_siguiente()
                            x+=1

                nodo_nombre = nodo_nombre.get_siguiente()
                j+=1


            nodo_frecuencia = nodo_frecuencia.get_siguiente()
            i+=1


    def buscar_nodo(self,contador,y,frecuencia):
        dato = 0
        i = 0
        nodo_actual = self.archivo.lista_frecuencia.get_cabeza()
        while i < self.archivo.lista_frecuencia.size:

            if (int(nodo_actual.get_contador())==int(contador)):
                if (int(nodo_actual.get_y())==int(y) and int(nodo_actual.get_frecuencia())==int(frecuencia)):
                    dato = int(dato) + int(nodo_actual.get_dato())
            nodo_actual = nodo_actual.get_siguiente()
            i+=1

        return dato


    def validar_posicion(self,contador,y,frecuencia):
        estado = False
        i = 0
        nodo_actual = self.lista_reducida.get_cabeza()

        while i < self.lista_reducida.size:

            if int(nodo_actual.get_contador()) == int(contador):
                if int(nodo_actual.get_y()) == int(y) and int(nodo_actual.get_frecuencia())==int(frecuencia):
                    estado = True 
                    return estado
            nodo_actual =nodo_actual.get_siguiente()
            i+=1

        return estado

    def agregar_frecuencia(self,contador,x,y,frecuencia):
        
        nodo_actual = self.lista_reducida.get_cabeza()
        i = 0
        while i < self.lista_reducida.size:

            if int(nodo_actual.get_contador()) == int(contador) and int(nodo_actual.get_x())==int(x) and int(nodo_actual.get_y())==int(y):
                nodo_actual.set_frecuencia(int(frecuencia))
            nodo_actual= nodo_actual.get_siguiente()
            i+=1

    def arreglar_fila_reducida(self):

        i=0
        nodo_nombre = self.archivo.lista_nombre.get_cabeza()
        while i < self.archivo.lista_nombre.size:


            if (nodo_nombre.get_estado()==True):

                j=0
                nodo_actual = self.lista_reducida.get_cabeza()
                fila = 1
                while j < self.lista_reducida.size:

                    if int(nodo_actual.get_contador()) == int(nodo_nombre.get_contador()):
                        columna_limite = nodo_nombre.get_y()

                        if int(nodo_actual.get_y()< int(columna_limite)) :
                            nodo_actual.set_x(int(fila))
                        elif int(nodo_actual.get_y()) == int(columna_limite):
                            nodo_actual.set_x(int(fila))
                            fila += 1

                    nodo_actual = nodo_actual.get_siguiente()
                    j+=1
                    

            nodo_nombre = nodo_nombre.get_siguiente()
            i += 1


