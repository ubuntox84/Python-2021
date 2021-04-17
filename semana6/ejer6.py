# ingresar una lista y duplicarlo 
def duplicar(l):
    n=len(l)
    for i in range (0,n):
        l[i]*=2

islista=[2,5,8,7,9]
print(islista)
duplicar(islista)
print(islista)
