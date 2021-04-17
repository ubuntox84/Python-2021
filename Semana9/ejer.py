class persona:
    def __init__(self,nombre):
        self.name=nombre
    def saludar(self):
        print("Buenos dias!! ", self.name)


x=persona("Christian")
#print(type(x))
x.saludar()