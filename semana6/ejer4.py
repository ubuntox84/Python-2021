#crear un funcion para hallar el mayor de 3 numeros

def hallar(num1,num2,num3):
    if num1!=num2 and num1!=num3 and num2!=num3:
        if num1>num2 and num1>num3:
            print("de {},{},{} el mayor es: {}".format(num1,num2,num3,num1))
            #print("de ",num1,num2,num3," el mayor es: ",num1)
        elif num2>num1 and num2>num3:
            print("de {},{},{} el mayor es: {}".format(num1,num2,num3,num2))
        elif num3>num2 and num3>num1:
            print("de {},{},{} el mayor es: {}".format(num1,num2,num3,num3))
    else:
        print("de {},{},{} son iguales, no existe mayor!!".format(num1,num2,num3))


a=int(input("ingresar numero entero: "))
b=int(input("ingresar numero entero: "))
c=int(input("ingresar numero entero: "))
hallar(a,b,c)