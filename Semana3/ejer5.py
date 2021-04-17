# ingresar un numero y decir si es neutro, positivo, negativo y complejo
x=float(input("Ingrese el numero a calcular:\n"))
if x==0:
    print("El numero es neutro\n")
elif x>0:
    print("El numero es positivo\n")
elif x<0:
    print("El numero es negativo\n")
else:
    print("El numero es complejo\n")