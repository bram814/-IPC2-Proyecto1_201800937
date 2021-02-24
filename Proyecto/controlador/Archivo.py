import xml.etree.ElementTree as ET 

class Archivo():

    def __init__(self):
        pass

    def __cargar__(self):
        
        name_route = str(input("Ruta: "))
        file_route = ET.parse(name_route)
        root = file_route.getroot()

        print(root)

        for element in root:
            for subelement in element:
                print(subelement)   