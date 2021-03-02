class Nodo():

    def __init__(self,contador,x,y,dato,estado,frecuencia=None,siguiente = None):

        self.contador = contador
        self.estado = estado
        self.x = x
        self.y = y
        self.dato = dato
        self.frecuencia = frecuencia
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
    
    def get_contador(self):
        return self.contador
    def set_contador(self,contador):
        self.contador = contador
    
    def get_estado(self):
        return self.estado
    def set_estado(self,estado):
        self.estado = estado
    
    def get_frecuencia(self):
        return self.frecuencia
    def set_frecuencia(self,frecuencia):
        self.frecuencia = frecuencia

    def __str__(self):
        return f" {self.contador}.-  (n: {self.x} m: {self.y}) Dato: {self.dato} Frecuencia: g{self.frecuencia}"