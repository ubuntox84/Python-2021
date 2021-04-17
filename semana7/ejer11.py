formato_cheque="N° 0000","-2020-ID(",")"


for i in range(1,11):
    print(str(i).join(formato_cheque))


for i in range(1,11):
    cad=str(i)
    formato_cheque="N° 0000"+str(i)+"-2020-ID("+str(1)+")"
    print(formato_cheque)