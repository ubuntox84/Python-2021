# Lista
pr=["tres",7,8,True,8,2,4]
print(type(pr))
print(len(pr))
print (5 in pr)
pr.append(5)
#dividir lista
tr=pr[4:]
print(tr)
lista=[7,5,6,3,6,7,2]
lista.append(9)
print(lista)
lista.sort()
print(lista)
lista.reverse()
print(lista)
lista.extend(pr)
print(lista)
print(lista*3)
#lista*=3
print (lista)
#count
print (lista.count(7))