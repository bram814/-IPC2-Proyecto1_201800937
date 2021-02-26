from modelos.Nodo import Nodo

class Lista_Circular():

    def __init__(self, cabeza = None, ultimo = None):
        self.cabeza = cabeza
        self.utlimo = ultimo
        self.size = 0
    
    def vacia(self):
        if self.cabeza == None:
            return True
        return False
    

    def agregar(self,contador,x,y,dato,estado):
        nuevo_nodo = Nodo(contador,x,y,dato,estado)
        if self.vacia() == True:
            self.set_cabeza(nuevo_nodo)
            self.set_ultimo(self.get_cabeza())
            self.get_cabeza().set_siguiente(self.get_ultimo())
        else:
            self.get_ultimo().set_siguiente(nuevo_nodo)
            nuevo_nodo.set_siguiente(self.get_cabeza())
            self.set_ultimo(nuevo_nodo)
        
        self.size += 1

    def mostrar(self):
        nodo_actual = self.get_cabeza()
        print('MOSTRAR DATOS ----------')
        while nodo_actual.get_siguiente() != self.get_cabeza():
            print(nodo_actual.get_dato())
            nodo_actual = nodo_actual.get_siguiente()
            if nodo_actual.get_siguiente() == self.get_cabeza():
                print(nodo_actual.get_dato())

    def modificar_estado(self,contador,x,y,dato,estado):
        nodo_actual = self.get_cabeza()
        
        while nodo_actual.get_siguiente() != self.get_cabeza():
            
            if nodo_actual.get_x() == x and nodo_actual.get_y() == y and nodo_actual.get_contador() == contador and nodo_actual.get_estado() == estado:
                nodo_actual.set_estado(estado)
            nodo_actual = nodo_actual.get_siguiente()
            if nodo_actual.get_siguiente() == self.get_cabeza():
                if nodo_actual.get_x() == x and nodo_actual.get_y() == y and nodo_actual.get_contador() == contador and nodo_actual.get_estado() == estado:
                    nodo_actual.set_estado(estado)


    def eliminar(self,dato):

        nodo_actual = self.get_cabeza()
        nodo_anterior = self.get_ultimo()

        while nodo_actual.get_siguiente() != self.get_cabeza():
           
            if nodo_actual.get_dato() == dato:
                if (nodo_actual == self.get_cabeza()):
                    self.set_cabeza(self.get_cabeza().get_siguiente())
                    self.get_ultimo().set_siguiente(self.get_cabeza())
                else:
                    nodo_anterior.set_siguiente(nodo_actual.get_siguiente())

            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.get_siguiente()

            if nodo_actual.get_siguiente() == self.get_cabeza():
                if nodo_actual.get_dato() == dato:
                    if nodo_actual == self.get_ultimo():
                        nodo_anterior.set_siguiente(self.get_ultimo().get_siguiente())
                        self.set_ultimo(nodo_anterior)
    
    def get_cabeza(self):
        return self.cabeza
    def set_cabeza(self,cabeza):
        self.cabeza = cabeza
        
    def get_ultimo(self):
        return self.utlimo
    def set_ultimo(self,ultimo):
        self.utlimo = ultimo
    

