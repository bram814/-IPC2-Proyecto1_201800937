class Nodo():

    def __init__(self,x,y,dato,siguiente = None):

        self.contador = 0
        self.x = x
        self.y = y
        self.dato = dato
        self.siguiente = siguiente
        
    
    def get_x(self):
        return self.x
    def set_x(self,x):
        self.x = x
    
    def get_y(self):
        return self.y
    def set_y(self,y):
        self.y = y

    def get_dato(self):
        return self.dato
    def set_dato(self,dato):
        self.dato = dato
    
    def get_siguiente(self):
        return self.siguiente
    def set_siguiente(self,siguiente):
        self.siguiente = siguiente