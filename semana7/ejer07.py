# se tiene dos listas se pide juntar las listas 
# pero los elementos de la tercera lista deben ser unicos
from random import randint
def generar():
    lista=[]
    for i in range(10):
        lista.append(randint(0,5))
    return lista

lista1=generar()
lista2=generar()

lista3=list(set(lista1).union(set(lista2)))

print(lista1)
print(lista2)
print(lista3)