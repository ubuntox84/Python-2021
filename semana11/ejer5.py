class persona:
    def __init__(self,a,b):
        self.x=a
        self.y=b
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def __len__(self):
        return self.x+self.y
obj=persona(5,8)
print(obj)
print(len(obj))
