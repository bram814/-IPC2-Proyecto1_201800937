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

        print('\nMatriz Frecuencia Parte 1')
        self.lista_nombre.mostrar()
        print('\nMatriz Frecuencia Parte 1')
        self.lista_frecuencia.mostrar() 
        print()