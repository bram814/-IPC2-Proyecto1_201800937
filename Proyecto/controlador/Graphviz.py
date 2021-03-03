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

        g = Digraph('g', format='svg',filename='Reporte_Final.gv',node_attr={'shape': 'circle', 'height': '.1'})

        g.node(f'node0',nohtml('Matrices'))
        g.node(f'node1',nohtml(f'{variable_nombre}'))
        g.node(f'node2',nohtml(f'{fila_limite}'))
        g.node(f'node3',nohtml(f'{columna_limite}'))

        j = 0
        nodo_actual = self.archivo.lista_frecuencia.get_cabeza()
        incremento = 4
        while j < self.archivo.lista_frecuencia.size:

            if int(nodo_actual.get_contador()) == int(contador):
                g.node(f'node{incremento}', nohtml(f'{nodo_actual.get_dato()}'))
                incremento+=1
            nodo_actual = nodo_actual.get_siguiente()
            j+=1
        

        g.edge(f'node0','node1')
        g.edge(f'node1','node2')
        g.edge(f'node1','node3')

        j = 0
        nodo_actual = self.archivo.lista_frecuencia.get_cabeza()
        incremento = 4
        while j < self.archivo.lista_frecuencia.size:

            if int(nodo_actual.get_contador()) == int(contador):
                if (self.archivo.lista_frecuencia.size != j+1):
                    g.edge(f'node{incremento}',f'node{incremento+1}')
                    incremento+=1
            nodo_actual = nodo_actual.get_siguiente()
            j+=1
            
        g.view()









