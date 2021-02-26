from controlador.Archivo import Archivo
from modelos.Lista_Circular import Lista_Circular

class main():


    def __init__(self):
        self.cargar_archivo = Archivo()
        self.lista = Lista_Circular()

    def __menu__(self):

        while True:
            print("""Menu Principal:
            1. Cargar Archivo
            2. Procesar Archivo
            3. Escribir archivo salida
            4. Mostrar datos del estudiante
            5. Generar gráfica""")
            try:
                variable = int(input("Opcion a escoger:"))
            

                if variable == 1:
                    print('Opcion 1')
                    self.cargar_archivo.__cargar__()
                elif variable == 2:
                    print('Opcion 2')
                    #self.lista.agregar(1,2,1)
                    #self.lista.agregar(1,2,2)
                    #self.lista.agregar(1,2,3)
                    #self.lista.agregar(1,2,4)
                    #self.lista.agregar(1,2,5)
                    
                elif variable == 3:
                    print('Opcion 3')
                    #self.lista.mostrar()
                    
                elif variable == 4:
                    print('Opcion 4')
                    #dato = int(input("datoL: "))
                    #self.lista.eliminar(dato)
                elif variable == 5:
                    print('Opcion 5')
                    return False
                elif variable == 6:
                    print("Exit")
                    return False
                else:
                    print(f"\nEsa Opcion no es correcta: {variable}\n")  
            except Exception as e:
                print(f"\nEsa Opcion no es correcta: {e}\n")
                
            
            

if __name__ == "__main__":
    instance = main()
    instance.__menu__()

