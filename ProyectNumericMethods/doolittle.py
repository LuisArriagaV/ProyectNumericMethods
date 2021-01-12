import numpy as np
print("Descomposicion Lu, matrices cuadradas")
m=int(input("Introduce el numero de renglones"))
matriz=np.zeros([m,m])
u=np.zeros([m,m])
l=np.zeros([m,m])
print("Introduce los elementos de la matriz")
for r in range(0,m):
    for c in range(0,m):
        matriz[r,c]=(input("Elemento a["+str(r+1)+","+str(c+1)+"]"))
        matriz[r,c]=float(matriz[r,c])
        u[r,c]=matriz[r,c]
#Operaciones para hacer ceros debajo de la diagonal
for k in range(0,m):
    for k in range(0,m):
        if(k==r):
           l[k,r]=1
        if(k<r):
           factor=(matriz[r,k]/matriz[k,k])
           l[r,k]=factor
           for c in range (0,m):
               matriz[r,c]=matriz[r,c]-(factor*matriz[k,c])
               u[r,c]=matriz[r,c]
print("Impresion de resultados")
print("Matriz L")
print(l)
print("Matriz U")
print(u)
#Comprobacion
matrizr=np.zeros([m,m])
for r in range(0,m):
    for c in range(0,m):
        for k in range(0,m):
            matrizr[r,c]+=(l[r,k]*u[k,c])
print (matrizr)
a=np.dot(l,u)
print(a)