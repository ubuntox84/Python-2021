class automovil:
    def __init__(self, a,b):
        self.x=a
        self.y=b
    def modificar(self,a,b):
        self.x=a
        self.y=b
    def display(self):
        print ("valores {} y {}".format(self.x,self.y))
    def mostrar(self):
        pass


obj=automovil(15,10)
obj.display()
obj.modificar(15,10)
obj.display()