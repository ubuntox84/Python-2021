#Se tiene un juego, cada vez que se pierda pierdes una vida
import random as num

def intento(vida=3):
    cad=input("Ingresar un numero: ")
    n=num.randrange(5)
    if cad!=n:
        if vida>1:
            print("Fallaste! intento de nuevo")
            intento(vida-1)
        else:
            print("Perdiste!!")
        
    else:        
        print("Ganaste")
    
intento()
