# mostrar los numero de 10 al 1

def imprimir(x):
    if x==1:
        return 1
    else:
        cad =str(x)+" "+str(imprimir(x-1))
        return cad

print(imprimir(5)) 

#5+4+3+2+1