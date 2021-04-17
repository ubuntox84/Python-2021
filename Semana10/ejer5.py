#cuenta regresiva
def regresiva(n):
    if n>0:
        print(n)
        n-=1
        regresiva(n)
    else:
        print("Booooom! Nave al espacio!!")

regresiva(3)