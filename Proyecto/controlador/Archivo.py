import xml.etree.ElementTree as ET 
from modelos.Lista_Circular import Lista_Circular

class Archivo():

    def __init__(self):
        # LISTA CIRCULAR
        self.lista_nombre = Lista_Circular()
        self.lista_frecuencia = Lista_Circular()
        self.lista_acceso = Lista_Circular()
        self.lista_reducida = Lista_Circular()

        self.contador = 1
        self.validacion = 1 #   1-> aceptado      0-> no aceptado
        
        # ANALIZADOR
        self.fila = 1
        self.columna = 1
        
        self.fila_limite = 0
        self.columna_limite = 0

        self.cantidad_dato = 0
        self.cantidad_limite = 0

        self.estado = False


    def __cargar__(self):
        
        name_route = str(input("Ruta: "))
        file_route = ET.parse(name_route)
        root = file_route.getroot()
        print('\n')
        for element in root:            # n -> fila     m -> columna
            self.fila_limite = element.attrib['n']
            self.columna_limite = element.attrib['m']
            self.cantidad_limite = int(self.fila_limite) * int(self.columna_limite)
            self.cantidad_dato = 0

            for subelement in element:
                
                if (0 < int(subelement.attrib['x']) <= int(self.fila_limite) and 0 < int(subelement.attrib['y']) <= int(self.columna_limite)):
                    self.estado = True
                    if (int(subelement.text)<0):
                        print(f"Algo anda mal: {subelement.text}")
                        self.estado = False
                        break
                else:
                    self.estado = False
                    break
                self.cantidad_dato +=1
            if (self.estado == True):
                if (int(self.cantidad_dato) == int(self.cantidad_limite)):
                    print(f"{self.cantidad_dato} == {self.cantidad_limite}")

                    for subelement in element:
                        if self.lista_frecuencia.buscar(self.contador,int(subelement.attrib['x']),int(subelement.attrib['y'])) == True:
                            print(f"DATO REPETIDO ({int(subelement.attrib['x'])} {int(subelement.attrib['y'])}) {subelement.text}")
                            self.estado = False
                            break
                        self.lista_frecuencia.agregar(self.contador,int(subelement.attrib['x']),int(subelement.attrib['y']),subelement.text,self.estado)
                    
                    self.lista_nombre.agregar(self.contador,int(element.attrib['n']),int(element.attrib['m']),str(element.attrib['nombre']),self.estado)
                    self.contador += 1

        
        print()
        i = 0
        nodo_lista_nombre = self.lista_nombre.get_cabeza()
        while i < self.lista_nombre.size:

            if (nodo_lista_nombre.get_estado()==True):
                print(f"CONTADOR: {nodo_lista_nombre.get_contador()}")
                contador = nodo_lista_nombre.get_contador()
                
                nodo_actual = self.lista_frecuencia.get_cabeza()
                j = 0
                while j < self.lista_frecuencia.size:
                    if (int(nodo_actual.get_contador()) == int(contador)):
                        if 0 < int(nodo_actual.get_dato()): # si es el dato es mayor a 0, se AGREGA un 1
                            self.lista_acceso.agregar(nodo_actual.get_contador(),nodo_actual.get_x(),nodo_actual.get_y(),1,nodo_lista_nombre.get_estado())
                        elif 0 == int(nodo_actual.get_dato()): # si es dato es igual a 0, se AGREGA un 0
                            self.lista_acceso.agregar(nodo_actual.get_contador(),nodo_actual.get_x(),nodo_actual.get_y(),0,nodo_lista_nombre.get_estado())
                        
                    nodo_actual = nodo_actual.get_siguiente()
                    j += 1
                
            nodo_lista_nombre = nodo_lista_nombre.get_siguiente()
            i += 1
        
        
        #estado_frecuencia = False
        
        
        self.frecuencia()
        
        
        
        print('\nMatriz Frecuencia Parte 1')
        self.lista_nombre.mostrar()
        print('\nMatriz Frecuencia Parte 2')
        self.lista_frecuencia.mostrar() 
        print('\nMatriz Frecuencia Parte 3')
        self.lista_acceso.mostrar()
        print()
        self.asignar_frecuencia_vacia()
        print('\nMatriz Frecuencia ARREGLADA Parte 3')
        self.lista_acceso.mostrar()
        

    def frecuencia(self):
        i = 0
        self.global_x = 0
        nodo_lista_nombre = self.lista_nombre.get_cabeza()
        while i < self.lista_nombre.size:

            if (nodo_lista_nombre.get_estado()==True):
                contador = nodo_lista_nombre.get_contador()
                limite_y = nodo_lista_nombre.get_y()
                limite_x = nodo_lista_nombre.get_x()
                x = 0
                nodo_acceso_actual = self.lista_acceso.get_cabeza()
                while x < self.lista_acceso.size:
                    
                    if (int(nodo_acceso_actual.get_contador()) == int(contador)):
                        global_x = nodo_acceso_actual.get_x()
                        if (self.comparacion_acceso(nodo_lista_nombre,nodo_acceso_actual,nodo_acceso_actual.get_x(),nodo_acceso_actual.get_y(),nodo_acceso_actual.get_dato())==True):
                            pass
                        else:
                            pass

                    nodo_acceso_actual = nodo_acceso_actual.get_siguiente()
                    x += 1

            nodo_lista_nombre = nodo_lista_nombre.get_siguiente()    
            i += 1



    # Funcion buscar si coincide el numero 1 o 0
    def comparacion_acceso(self,matriz_nombre,nodo_acceso_actual,x,y,dato,contador_=0):
        estado_frecuencia = False
        contador_fila = contador_
        i = 0
        nodo_actual = self.lista_acceso.get_cabeza()
        while i < self.lista_acceso.size:

            if (nodo_actual.get_contador() == matriz_nombre.get_contador()):
                if (nodo_actual.get_x()>x):
                    if nodo_actual.get_y() == y:
                        if nodo_actual.get_dato() == dato:
                            
                            #print(f"({nodo_acceso_actual.get_x()},{y})-----------------{nodo_actual.get_contador()}.- ({nodo_actual.get_x()},{nodo_actual.get_y()}) ENCONTRADO? {nodo_actual.get_dato()}")
                            tem = y
                            contador_fila += 1
                            y = int(nodo_actual.get_y()) + 1
                            dato = self.buscador_nodo(nodo_actual.get_contador(),nodo_acceso_actual.get_x(),y)
                            
                            if (contador_fila == matriz_nombre.get_x()):
                                #print(f"{nodo_actual.get_x()},{nodo_actual.get_y()} ESTE TIENE GRUPO ({nodo_acceso_actual.get_x()},{tem})")
                                estado_frecuencia = True
                                if (self.buscar_grupo(nodo_actual.get_contador(),nodo_acceso_actual.get_x())==True):
                                    frecuencia = nodo_acceso_actual.get_frecuencia()
                                    
                                    self.asignar_grupo(nodo_actual.get_contador(),nodo_actual.get_x(),frecuencia)
                                else:
                                    self.asignar_grupo(nodo_actual.get_contador(),nodo_acceso_actual.get_x(),nodo_acceso_actual.get_x())
                                    self.asignar_grupo(nodo_actual.get_contador(),nodo_actual.get_x(),nodo_acceso_actual.get_x())
                                contador_fila = 0
                           
                                
                            

                        else:
                            
                            #print(f"({nodo_acceso_actual.get_x()},{y})-----------------{nodo_actual.get_contador()}.- ({nodo_actual.get_x()},{nodo_actual.get_y()}) FALSO {nodo_actual.get_dato()}")
                            x = int(nodo_actual.get_x()) 
                            y = 1
                            dato = self.buscador_nodo(nodo_actual.get_contador(),nodo_acceso_actual.get_x(),y)
                            #print(f"({nodo_acceso_actual.get_x()},{y})-----------------{nodo_actual.get_contador()}.- ({nodo_actual.get_x()},{nodo_actual.get_y()}) FALSO {nodo_actual.get_dato()}")
                            #print(f'--- {x},{y}')
                            estado_frecuencia = False
                            contador_fila = 0
                            self.comparacion_acceso(matriz_nombre,nodo_acceso_actual,x,y,dato,contador_fila)

            nodo_actual = nodo_actual.get_siguiente()
            i+=1
        
        return estado_frecuencia    
    

    def buscador_nodo(self,contador,x,y):
        dato = 0

        nodo_actual = self.lista_acceso.get_cabeza()

        i = 0 
        while i < self.lista_acceso.size:

            if (nodo_actual.get_contador()==contador):
                if (nodo_actual.get_x()==x and nodo_actual.get_y()==y):
                    dato = nodo_actual.get_dato()
                    return dato
            nodo_actual = nodo_actual.get_siguiente()
            i+=1

        return dato

    

    def asignar_grupo(self,contador,x,frecuencia):

        # frecuencia es el inicial
        # x posicion donde se encuentra

        nodo_actual = self.lista_acceso.get_cabeza()
        i = 0
        while i < self.lista_acceso.size:

            if (int(nodo_actual.get_contador()) == int(contador)):
                if int(nodo_actual.get_x()) == int(x):
                    nodo_actual.set_frecuencia(int(frecuencia))
            nodo_actual = nodo_actual.get_siguiente()
            i+=1
    

    def buscar_grupo(self,contador,x):
        estado = False
        nodo_actual = self.lista_acceso.get_cabeza()
        i = 0
        while i < self.lista_acceso.size:

            if (int(nodo_actual.get_contador()) == int(contador)):
                if int(nodo_actual.get_x()) == int(x) and nodo_actual.get_frecuencia() != None:
                    estado = True
                    return estado
            nodo_actual = nodo_actual.get_siguiente()
            i+=1

        return estado

    def asignar_frecuencia_vacia(self):

        nodo_matriz_nombre = self.lista_nombre.get_cabeza()
        i = 0

        while i < self.lista_nombre.size:

            if (nodo_matriz_nombre.get_estado()==True):

                j = 0
                nodo_actual = self.lista_acceso.get_cabeza()
                while j < self.lista_acceso.size:
                    
                    if int(nodo_matriz_nombre.get_contador()) == int(nodo_actual.get_contador()):
                        if (nodo_actual.get_frecuencia()==None):
                            self.asignar_grupo(nodo_actual.get_contador(),nodo_actual.get_x(),nodo_actual.get_x())
                    nodo_actual = nodo_actual.get_siguiente()
                    j+=1

            nodo_matriz_nombre = nodo_matriz_nombre.get_siguiente()
            i += 1
