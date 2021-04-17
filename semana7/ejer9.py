t=((1,2,3),(4,5,6),(7,8,9))
#print(type(t))
#print(t)
for x,y,z in t:
    suma=x+y+z
    print(x,"\t",y,"\t",z,"La suma es",suma)


for x in t:
    cad=''
    suma=0
    for y in x:
        suma+=y
        cad+=str(y)+"\t"    
    print(cad,"La suma es ",suma)