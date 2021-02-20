from controlador.Archivo import Archivo

class main():


    def __init__(self):
        self.cargar_archivo = Archivo()

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
                    return False
                elif variable == 2:
                    print('Opcion 2')
                    return False
                elif variable == 3:
                    print('Opcion 3')
                    return False
                elif variable == 4:
                    print('Opcion 4')
                    return False
                elif variable == 5:
                    print('Opcion 5')
                    return False
                else:
                    print(f"\nEsa Opcion no es correcta: {variable}\n")  
            except Exception as e:
                print(f"\nEsa Opcion no es correcta: {e}\n")
                
            
            

if __name__ == "__main__":
    instance = main()
    instance.__menu__()

