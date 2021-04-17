# crear una funcion para un cajero automaticos, donde realiza las siguiente 
# operaciones: consulta, extraer, depositar, transferir, Salir
import random as ran

cad=" BIENVENIDA "
cad=cad.center(35,"*")
cad2= "\nQue desea realizar? \n1.consulta \n2. extraer \n3.depositar \n4.transferir \n0.Salir:  "
cad+=cad2


def consulta(sal):
    dinero=sal[0]
    print("El saldo es: ",dinero)

def extraer(sal,retiro):
    sal[0]=float(sal[0])-retiro
    print("Dinero retirado con exito!!", retiro)

def depositar(sal,deposito):
    sal[0]=float(sal[0])+deposito
    print("Dinero depositado con exito!!", deposito)

def transferir(sal,cuenta,monto):
    sal[0]=float(sal[0])-monto
    print("Dinero transferirdo a la cuenta ",cuenta," con exito!!, el monto de ", monto)

saldo=[int(input("Ingresar saldo:  "))]
while 100:    
    op=str(input(cad))
    if '1'==op:
        consulta(saldo)
    elif '2'==op:
        reti=int(input("Ingresar cuanto desea retirar"))
        extraer(saldo,reti)
    elif '3'==op:
        depo=int(input("Ingresar cuanto desea depositar"))
        depositar(saldo,depo)
    elif '4'==op:
        numcuenta=int(input("Ingresar numero de cuenta que desea depositar"))
        monto=int(input("Ingresar cuanto dinero quiere transferir"))
        transferir(saldo,numcuenta, monto)
    else:
        break
print("Tenga buen dia!!!")

