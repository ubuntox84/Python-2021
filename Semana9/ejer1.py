class sumados:
    def __init__(self, a, b):
        self.x=a
        self.y=b
    def suma(self):
        return self.x+self.y

sum=sumados(8,5)
print(sum.suma())