#4-	Escribir una función que reciba una muestra de números en una lista y devuelva su media. 

n=float(input("Ingresar el nro de elementos de lista: "))
i=0
lista=[]
def media(l,p):
    acu=0.0
    for x in l:
        acu+=float(x)
    med=acu/p
    return med

while True:
    lista.append(input("ingresar un numero: "))
    i+=1
    if i==n:
        break


print(lista)
print ("La media es: ",str(media(lista,n)))


