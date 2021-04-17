# crea una funcion para dibujar un cuadrado, el usuario puede elegir vacio o lleno
# son lados iguales
def dibujar(x):
    temp=x;
    for i in range(temp):
        print("*"*temp)

def dibujarvacio(x):
    temp=x
    for i in range(temp):
        if(i==0):
            print("*"*temp)
        elif(i==temp-1):
            print("*"*temp) 
        else:  
            print("*",""*(temp-2),"*")


n=int(input("ingresar el lado del cuadrado"))
dibujar(n)
print()
dibujarvacio(n)
