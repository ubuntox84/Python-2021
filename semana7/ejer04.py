# simular un cola, FIFO
from collections import deque
lista=deque()
def encolar(x):
    lista.append("Alumno {}".format(x))
    print(lista)
def desencolar():
    lista.popleft()
    print(lista)
i=1
while True:
    op=input("Desea encolar [S/N]")
    if op=='s' or op =='S':
        encolar(i)
        i+=1
    else:
        break
while True:
    op=input("Desea desencolar [S/N]")
    if op=='s' or op =='S':
        if len(lista)==0:
            print("No existe alumnos!!")
        else:
            desencolar()
        
    else:
        break
print(lista)
print("Hasta la vista Baby!!")