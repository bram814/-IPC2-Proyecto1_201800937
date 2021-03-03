#http://www.graphviz.org/pdf/dotguide.pdf
from graphviz import Digraph, nohtml

class Graphviz():


    def __init__(self):
        self.archivo = None
        self.procesamiento = None


    def generar_reporte(self,archivo_file,procesamiento_file):

        self.archivo = archivo_file 
        self.procesamiento = procesamiento_file

        i = 0
        nodo_nombre = self.archivo.lista_nombre.get_cabeza()
        
        while i < self.archivo.lista_nombre.size:

            if nodo_nombre.get_estado()==True:
                print(f"{nodo_nombre.get_contador()}.- Nombre:{nodo_nombre.get_dato()}, n={nodo_nombre.get_x()} m={nodo_nombre.get_y()}")

            nodo_nombre = nodo_nombre.get_siguiente()
            i+=1
        
        contador = str(input("Seleccione una opcion: "))

        i = 0
        nodo_nombre = self.archivo.lista_nombre.get_cabeza()
        
        while i < self.archivo.lista_nombre.size:

            if nodo_nombre.get_estado()==True:
                if int(nodo_nombre.get_contador()) == int(contador):
                    variable_nombre = nodo_nombre.get_dato()
                    fila_limite = nodo_nombre.get_x()
                    columna_limite = nodo_nombre.get_y()
                    break
            nodo_nombre = nodo_nombre.get_siguiente()
            i+=1

        g = Digraph('g', format='svg',filename='Reporte_Final.gv',node_attr={'shape': 'record', 'height': '.1'})
        #g = Digraph('g', format='svg',filename='Reporte_Final.gv',node_attr={'shape': 'circle', 'height': '.1'})

        g.node(f'node00',nohtml('Matrices'))
        g.node(f'node01',nohtml(f'{variable_nombre}'))
        g.node(f'node02',nohtml(f'{fila_limite}'))
        g.node(f'node03',nohtml(f'{columna_limite}'))

        j = 0
        nodo_actual = self.archivo.lista_frecuencia.get_cabeza()
       
        while j < self.archivo.lista_frecuencia.size:

            if int(nodo_actual.get_contador()) == int(contador):
                g.node(f'node{nodo_actual.get_x()}{nodo_actual.get_y()}', nohtml(f'({nodo_actual.get_x()},{nodo_actual.get_y()}) |{nodo_actual.get_dato()}'))
                #g.node(f'node{nodo_actual.get_x()}{nodo_actual.get_y()}', nohtml(f'{nodo_actual.get_dato()}'))
                
            nodo_actual = nodo_actual.get_siguiente()
            j+=1
        

        g.edge(f'node00','node01')
        g.edge(f'node01','node02')
        g.edge(f'node01','node03')


        i = 0
        nodo_actual = self.archivo.lista_frecuencia.get_cabeza()

        while i < self.archivo.lista_frecuencia.size:

            if int(nodo_actual.get_contador()) == int(contador):
                if int(nodo_actual.get_x())==1:
                    g.edge(f'node01',f'node{nodo_actual.get_x()}{nodo_actual.get_y()}')

            nodo_actual = nodo_actual.get_siguiente()
            i+=1


        

        j = 0
        nodo_actual = self.archivo.lista_frecuencia.get_cabeza()
        
        while j < self.archivo.lista_frecuencia.size:

            if int(nodo_actual.get_contador()) == int(contador):
                if (self.archivo.lista_frecuencia.size != j+1):
                    if int(nodo_actual.get_x()) < int(fila_limite):
                        aux = self.nodo_fila_siguiente(nodo_actual.get_contador(),nodo_actual.get_x()+1,nodo_actual.get_y()) 
                        g.edge(f'node{nodo_actual.get_x()}{nodo_actual.get_y()}',f'node{aux.get_x()}{aux.get_y()}')
                    
            nodo_actual = nodo_actual.get_siguiente()
            j+=1
            
        g.view()






    def nodo_fila_siguiente(self,contador,x,y):
        i = 0
        nodo_actual = self.archivo.lista_frecuencia.get_cabeza()

        while i < self.archivo.lista_frecuencia.size:

            if int(nodo_actual.get_contador()) == int(contador):
                if int(nodo_actual.get_x()) == int(x) and int(nodo_actual.get_y())==int(y):

                    return nodo_actual

            nodo_actual = nodo_actual.get_siguiente()
            i+=1



