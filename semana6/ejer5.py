#factorial de numero:  4!= 1*2*3*4

def factorial(x):
    temp=1
    for i in range(1,x+1):
        temp*=i
    x=10
    return temp

n=int(input("ingresar un número "))
factor=factorial(n)
print("Factorial de {} es {}".format(n,factor))