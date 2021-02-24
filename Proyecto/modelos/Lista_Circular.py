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
    

    def agregar(self,x,y,dato):
        nuevo_nodo = Nodo(x,y,dato)
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
    
    def get_cabeza(self):
        return self.cabeza
    def set_cabeza(self,cabeza):
        self.cabeza = cabeza
        
    def get_ultimo(self):
        return self.utlimo
    def set_ultimo(self,ultimo):
        self.utlimo = ultimo
    

