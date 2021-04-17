class persona:
    def __init__(self, n, a):
        self.name=n
        self.age=a
    def mostrar(self):
        return "Nombre "+str(self.name)+" Edad: " +str(self.age)

class celular(persona):
    def __init__(self, n, na, ag):
        super().__init__(na,ag)
        self.num=n
    def datos(self):
        return self.mostrar() +" Celular: "+str(self.num)

alu=celular(948016820,'Christian',37)
print(alu.mostrar())
print(alu.datos())



   