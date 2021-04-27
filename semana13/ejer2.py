
import panda as pd
file='semana13/subvenciones.csv'
f=open(file,'r')
while 1:
    txt=f.read()
    print(txt)
    if txt=="":
        break