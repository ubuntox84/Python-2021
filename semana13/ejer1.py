f=open("arch.txt",'w')
for i in range (10):
    if i==9:
        f.write(str(i))
    else: f.write(str(i)+',')
f.close()

f=open("arch.txt",'r')
text=f.read()
li=text.split(',')
print(type(li))
for i in li:
    print(i)

print("La cantidad de elemento es ",len(li))