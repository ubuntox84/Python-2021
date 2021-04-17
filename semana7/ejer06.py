#Se tiene una lista de elemento repetidos, se pide crear una lista de elementos unicos
lista=[]
from random import randint
for i in range(15):
    x=randint(0,5)
    lista.append(x)

conjunto=set(lista)
newlista=list(conjunto)
print(newlista)
print (lista)