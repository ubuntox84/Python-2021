class mascota:
    def __init__(self,cad):
        self.tipo=cad
    def mostrar(self):
        return self.tipo
class genero:
    def __init__(self,gen):
        self.genero=gen

class perro(mascota,genero):
    def __init__(self,n, o,tipo,gen):
        mascota.__init__(self,tipo);
        genero.__init__(self,gen);
        self.name=n
        self.old=o
    def display(self): 
        return self.mostrar()+" "+self.name+" "+str(self.old)+" "+self.genero

obj=perro("Fido",10,"Domestico","Macho")
print(obj.display())