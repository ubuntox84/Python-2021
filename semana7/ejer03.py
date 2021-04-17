
# simular una PILA, tambien conocida como LIFO
from collections import deque
lista=deque()

def apilar(x):
    lista.append("Plato {}".format(x))
    print(lista)
def desapilar():
    lista.pop()
    print(lista)
i=1
while True:
    op=input("deseas apilar? [s/n]")
    if op=='s' or op=='S':
        apilar(i)
        i+=1
    else:
        break
while True:
    op=input("deseas desapilar? [s/n]")
    if op=='s' or op=='S':
        if len(lista)==0:
            print(lista)
            print("No hay platos!!")
            break
        else:
            desapilar()        
    else:
        break
print(lista)
print("Hasta pronto!!")

