from controlador.Archivo import Archivo
from controlador.Procesamiento import Procesamiento
from controlador.Archivo_Salida import Archivo_Salida

from modelos.Lista_Circular import Lista_Circular

class main():


    def __init__(self):
        self.cargar_archivo = Archivo()
        self.procesamiento = Procesamiento()
        self.generar_salida = Archivo_Salida()

    def __menu__(self):

        while True:
            print("""Menu Principal:
            1. Cargar Archivo
            2. Procesar Archivo
            3. Escribir archivo salida
            4. Mostrar datos del estudiante
            5. Generar gráfica
            6. Salida""")
            try:
                variable = int(input("Opcion a escoger:"))
            

                if variable == 1:
                    self.cargar_archivo.__cargar__()
                elif variable == 2:
                    self.procesamiento.procesar_datos(self.cargar_archivo)
                    
                elif variable == 3:
                    ruta_salida = str(input("Escribir ruta especifica: "))
                    self.generar_salida.generar_archivo_salida(ruta_salida,self.cargar_archivo,self.procesamiento)
                        
                elif variable == 4:
                    print('\n> Jose Abraham Solorzano Herrera\n> 201800937 \n> Introduccion a la Programación y computación 2 seccion "A" \n> Ingeniería en Ciencias y Sistemas\n> 4to Semestre\n')

                elif variable == 5:
                    print('Opcion 5')
                    
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

