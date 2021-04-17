

def producto(*r):
    resp=1
    for i in r:
        resp*=i
    return resp
    
p=producto(2,2,2,2,2)
print(p)
