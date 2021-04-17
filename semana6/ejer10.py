#sumar digitos numericos de una lista

def sumardigitos(a):
    acumulador=0
    for i in a:
        acumulador+=i
    return acumulador

v=[1,2,3,1,2,10]
v.append(1)
v.append(2)
v.append(3)
varsum=sumardigitos(v)
print(v)
print(varsum)

if 10 in v:
    print("7 esta contenido en la lista")
else:
    print("7 no esta contenido en la lista!")