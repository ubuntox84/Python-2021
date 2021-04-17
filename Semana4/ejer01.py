menu="""
Bienvenido al Menu
1:Multiplicar
2:Dividir
3:Sumar
4:Restar
0:Salir
"""
centinela=100
while(centinela):    
    print(menu)
    op=int(input("Que desea realizar?"))
    if (op>0) & (op <=4):
        a=float(input("Valor A:"))
        b=float(input("Valor B:"))
    #print(type(a))
    if op is 1:
        mul=a*b
        print("El producto de "+str(mul))
    elif op is 2:
        mul=a/b
        print("El Dividir de "+str(mul))
    elif op is 3:
        mul=a+b
        print("El Sumar de "+str(mul))
    elif op is 4:
        mul=a-b
        print("El Restar de "+str(mul))    
    elif op is 0:
        centinela=0
    else:
        print("Vuelva intentarlo!!")