class Archivo_Salida():


    def __init__(self):
        self.archivo = None
        self.procesamiento = None

    def generar_archivo_salida(self,ruta,file_archivo,file_procesamiento):

        self.archivo = file_archivo
        self.procesamiento = file_procesamiento
        

        document = open(ruta,"w")

        #message = f"""{self.creacion_mensaje()}>"""
        message = f"""<matrices>\n{self.creacion_mensaje()}</matrices>"""
        
        document.write(message)
        document.close()
        print('Documento Creado --- -- --- 100%')


    def creacion_mensaje(self):
        mensaje = ""
        nodo_nombre = self.archivo.lista_nombre.get_cabeza()
        i = 0
        
        while i < self.archivo.lista_nombre.size:
            
            if nodo_nombre.get_estado() == True:

                j = 0
                nodo_actual = self.procesamiento.lista_reducida.get_cabeza()
                nombre = nodo_nombre.get_dato()
                y = nodo_nombre.get_y()
                x = self.obtener_fin_reducida(nodo_nombre.get_contador())
                mensaje += f'''  <matriz nombre="{str(nombre)}" n="{x}" m="{str(y)}" g="{x}">\n'''
                while j < self.procesamiento.lista_reducida.size:

                    if int(nodo_nombre.get_contador()) == int(nodo_actual.get_contador()):

                        mensaje += f'''    <dato x="{str(nodo_actual.get_x())}" y="{str(nodo_actual.get_y())}">{str(nodo_actual.get_dato())}</dato>\n'''

                    nodo_actual = nodo_actual.get_siguiente()
                    j+=1
                
                mensaje += f''' {self.buscando_frecuencia(nodo_nombre.get_contador(),nodo_nombre.get_y())}'''
                

                mensaje += f'''  </matriz>\n'''
            nodo_nombre = nodo_nombre.get_siguiente()
            i+=1

        return mensaje

    def obtener_fin_reducida(self,contador):
        i = 0
        x = 0 
        nodo_actual = self.procesamiento.lista_reducida.get_cabeza()

        while i < self.procesamiento.lista_reducida.size:
            aux = nodo_actual
            aux = aux.get_siguiente()
            if int(nodo_actual.get_contador()) == int(contador):

                if (int(aux.get_contador()) != int(contador)):
                    x = nodo_actual.get_x()

                    return x
                elif int(i+1) == int(self.procesamiento.lista_reducida.size):
                    x = nodo_actual.get_x()
                    return x
            nodo_actual = nodo_actual.get_siguiente()
            i+=1
        return x



    def buscando_frecuencia(self,contador,y):
        
        contador_frecuencia = 0
        i = 0 
        mensaje = ""
        nodo_grupo = self.archivo.lista_grupos.get_cabeza()

        while i < self.archivo.lista_grupos.size:

            if int(nodo_grupo.get_contador()) == int(contador):
                j = 0
                nodo_actual = self.archivo.lista_frecuencia.get_cabeza() 
                while j < self.archivo.lista_frecuencia.size:
                    
                    if(int(nodo_actual.get_contador())==int(contador) and int(nodo_grupo.get_frecuencia())==int(nodo_actual.get_frecuencia())):
                        contador_frecuencia+=1

                    nodo_actual = nodo_actual.get_siguiente()
                    j+=1
                calculo = int(contador_frecuencia)/int(y)
                contador_frecuencia = 0
                mensaje += f'''   <frecuencia g="{str(nodo_grupo.get_frecuencia())}">{str(calculo)}</frecuencia>\n '''

            nodo_grupo = nodo_grupo.get_siguiente()
            i+=1
            
        return mensaje

    
        """
        print('VIENDO LA FRECUENCIA')
        i = 0
        nodo_actual = self.archivo.lista_grupos.get_cabeza()
        contador = nodo_actual.get_contador()
        incremento = 0
        print(self.archivo.lista_grupos.size)

        while i < self.archivo.lista_grupos.size:
            print(i)
            if (int(nodo_actual.get_contador()) != int(contador)):
                print(f"____{incremento}")
                incremento = 1
                contador = nodo_actual.get_contador()
            elif (i+1) == self.archivo.lista_grupos.size :
                incremento += 1
                print(f"____{incremento}")
            else:
                incremento += 1

            nodo_actual = nodo_actual.get_siguiente()
            i += 1
        """