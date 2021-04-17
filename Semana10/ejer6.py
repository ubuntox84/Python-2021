lista=[2,5,7,6,7]
def ingresa():
    a=int(input("Ingrese valor"))
    return a
try:
    #print(lista[7])
    x=ingresa()
    y=ingresa()
except IndexError:
    print("La lista esta fuera de rango!")
except ValueError:
    print("Se ingreso un texto!!")
    ingresa()
else:
    print("La suma es: {}".format(x+y))
