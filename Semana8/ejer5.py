#retornos multiples
def operacion(x,y):
    r=x-y
    s=x+y
    p=x*y
    return r,s,p

a,b,c=operacion(5,2)

print("Resta: ",a)
print("Suma: ",b)
print("Producto: ",c)