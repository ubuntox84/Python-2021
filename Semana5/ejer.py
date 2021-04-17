lista=[1,5,8,7,7]
for v in lista:
    print(v)
lista.append(8)
print("Nueva lista")
for v in lista:
    print(v)
print(type(lista))


print(lista[-1])

print(lista[:3])
print(lista[3:])