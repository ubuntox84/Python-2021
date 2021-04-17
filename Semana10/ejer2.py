#Hallar el factorial

def func(n):
    cad+=n
    return cad

lista=[]
def facto(n):
    lista.append(n)
    if n==1:
       return 1
    else:        
        calc=n*facto(n-1)
        return calc
        # 5* facto(4)
        # 5* 4* facto(3)
        # 5* 4* 3* facto(2)
        # 5* 4* 3* 2* facto(1)
        # 5* 4* 3* 2* 1
print(facto(5))
print(lista)
