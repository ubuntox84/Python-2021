#cierto reyes acostrumbre a saludar n veces
n=int(input("ingrese el numero de saludos"))

def saludar():
    return "Buenos dias"

def repitirsaludo(x):
    for i in range(x):
        print(saludar())

repitirsaludo(n)