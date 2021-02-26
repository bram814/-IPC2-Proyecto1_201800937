import xml.etree.ElementTree as ET 

class Archivo():

    def __init__(self):
        # LISTA CIRCULAR
        self.contador = 1
        self.estado = 1
        
        # ANALIZADOR
        self.fila = 1
        self.columna = 1
        
        self.fila_limite = 0
        self.columna_limite = 0


    def __cargar__(self):
        
        name_route = str(input("Ruta: "))
        file_route = ET.parse(name_route)
        root = file_route.getroot()

        print(root)

        for element in root:
            print(f"Tag: {element.tag} Nombre: {element.attrib['nombre']}  n: {element.attrib['n']} m: {element.attrib['m']}")
            for subelement in element:
                print(f"Posicion[ x = {subelement.attrib['x']} y = {subelement.attrib['y']}] Dato:{subelement.text}")   