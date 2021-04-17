#split--> seperador--> genera una lista
cad="FIIS UNAS TINGO"
cad2=cad.split(" ")
print(cad2)

cad="2,5,8,6,7"
cad2=cad.split(",")
print(cad2)

#partition--> separador --> genera un tupla
url="https://www.unas.edu.pe"
party=url.partition("www")
print(party)


url="https://www.unas.edu.pe"
A,B,C=url.partition("www")
print("Dominio",C)
print("Protocolo",A)