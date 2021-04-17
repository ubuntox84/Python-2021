#lista[5,4,8,7,6,7,7], sumar y mostrar
lista=[5,4,8,[2,[2,5,6],4],6,4,1]
n=len(lista)
cad=" "

def listar (lista):
    for n in lista:
        if isinstance(n,list):
            listar(n)
        else:
            print(n,end=" ")

listar(lista)