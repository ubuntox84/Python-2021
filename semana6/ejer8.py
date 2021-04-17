#dibujar una matriz
def strcolum(matriz, r):
    cad=""
    for j in range(len(matriz[r])):
        cad+=str(matriz[r][j])+" "
    return cad

def dibujarmatriz(matriz):
    for i in range(len(matriz)):
        print ("[ ",strcolum(matriz,i)," ]")

m=[[1,2],[4,5],[5,8],[5,7]]
print(m)
print("\nLa matriz es: ")
dibujarmatriz(m)