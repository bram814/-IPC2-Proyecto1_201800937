class Matriz():

    def __init__(self,x,y,valor):
        self.contador = 1
        self.x = x
        self.y = y
        self.valor = valor
    
    def getX(self):
        return self.x
    def setX(self,x):
        self.x = x
    
    def getY(self):
        return self.y
    def setY(self,y):
        self.y = y
    
    def getDato(self):
        return self.valor
    def setDato(self,valor):
        self.valor = valor