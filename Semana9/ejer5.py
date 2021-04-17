class fruta:
    def __init__(self, n):
        self.name=n
    def getfruta(self):
        return self.name

class caracteristicas:
    def __init__(self, c, s):
        self.color=c
        self.sabor=s
    def getcolor(self):
        return self.color
    def getsabor(self):
        return self.sabor

class mercado(fruta,caracteristicas):
    def __init__(self,n,c,s,nm):
        fruta.__init__(self,n)
        caracteristicas.__init__(self,c,s)
        self.mercado=nm
    
    def getmercado(self):
        return self.mercado
    
    def mostrar(self):
        return "Nombre del mercado: "+self.getmercado()+" fruta: "+self.getfruta()+ " Caracteristicas :"+self.getcolor()+" , "+self.getsabor() 

mer=mercado("Pera","Verde","Dulce","TINGO MARIA")
print(mer.mostrar())