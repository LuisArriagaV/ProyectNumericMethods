import math
import sympy as sym 
from sympy import cos, sin, tan, exp
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np 
from fractions import Fraction 

def ValidadorMetodo(matriz,matrizRecursos):
		m = len(matriz.shape)
		if(m==1):
			print("No es necesario particionar")
		elif (m==2):
			cen= ValidarMatriz(matriz)
			if(cen == len(matrizRecursos)):			
				if(cen!=0 and cen>=4):
						print("Matriz aprobada, es cuadrada y es de",cen,"x",cen)
						return cen
				else:
					print("No puede aplicarse el metodo, porque la matriz no cumple con el requerimento de ser cuadradada o ser al menos 4x4")
			else:
				print ("El vector de recursos, debe de ser de la dimension:",cen)	
		return 0


def ValidarMatriz(matriz):
		if (len(matriz.shape)==1):
				return -1
		elif(matriz.shape[0]==matriz.shape[1] and matriz.shape != (0,0)):
				n = matriz.shape[0]
				return n
		else:
			return 0


def ParticionarMatriz(a,matriz,vectorRecursos,x,y):
		if(a>matriz.shape[1]):
			print("La particion no es posible")
			return 0
		else:
			A = np.array([])
			B = np.array([])
			arr = np.array([])
			vectorRecursos = vectorRecursos.reshape(len(vectorRecursos),1)
			list_for = [0,1]
			list_for1= [0,1,2,3]
			matriz = np.vsplit(matriz,(x,y))
			for i in list_for:
				B =  np.append(B,str(np.vsplit(vectorRecursos,(x,y))[i]))
				for j in list_for:
					arr = np.append(arr,np.hsplit(matriz[i],(x,y))[j].shape)
					A= np.append(A,str(np.hsplit(matriz[i],(x,y))[j]))
			ImprimirParticiones(A,B,arr)
		return A,B,arr

def ImprimirParticiones(A,B,arr):
		y= PrettyTable()
		y1= PrettyTable()
		y.field_names = ["A_11","A_12","b1"]
		y1.field_names = ["A_21","A_22","b2"]
		list_for1 = [0,1,2,3]
		y.add_row([A[0],A[1],B[0]])
		y1.add_row([A[2],A[3],B[1]])
		print(y,"\n",y1)

def GaussJordan(A,B,n,arr,par,order,k):
		Aaux = GenerarMatriz(A,n,arr,1)
		cen = ValidarMatriz(Aaux)
		print ("Iteración:",k+1)
		Explicacion(k)
		if n%(par+1)==0 and n<4:
			if cen!=0:
				n = Diagonal(A,B,order[k],arr,par,Aaux)
		else:
			n = NoDiagonal(A,B,order[k],arr,par,Aaux) 
		ImprimirParticiones(A,B,arr)	
		if n==2:
			return
		else:
			k=k+1
			return GaussJordan(A,B,order[k],arr,par,order,k) 


def Diagonal(A,B,n,arr,par,Aaux):
		Ainv =np.linalg.inv(Aaux)
		I = np.around(np.matmul(Aaux,Ainv),6).astype(int)
		print ("\tLa inversa de:\n",Aaux,"\n\tes:\n",Ainv,"\n\tes igual a:\n",I)
		A[n]=str(I)
		if n==par+1:
			Amod1 = GenerarMatriz(B,n%2,arr,0) 
			print ("\n\n\t Realizando las operaciones:\n",Amod1,"\n\t multiplicado por:\n",Ainv)
			Amod1 = np.around(np.matmul(Ainv,Amod1),6).astype(float) 
			print ("\n\tigual a:\n",Amod1)
			B[n%2] = str(Amod1)
		else:		
			Amod01 = GenerarMatriz(A,n+1,arr,1) 
			Amod11 = GenerarMatriz(B,0,arr,0) 
			Amod = np.around(np.matmul(Ainv,Amod01),6).astype(float) 
			Amod1 = np.around(np.matmul(Ainv,Amod11),6).astype(float)
			print ("\n\n\t Realizando las operaciones:\n",Ainv,"\n\t multiplicado por:\n",Amod01,"\n\tigual a:\n",Amod)
			print ("\n\n\t Realizando las operaciones:\n",Ainv,"\n\t multiplicado por:\n",Amod11,"\n\tigual a:\n",Amod1)
			A[n+1]=str(Amod)
			B[n%2] = str(Amod1)
		return n

def NoDiagonal(A,B,n,arr,par,Aaux):
			i = par
			arr1 = CreaCadenas(par)
			p = (pow(-1,n+1))
			Aaux1 = GenerarMatriz(A,n+p,arr,1)
			for j in arr1:
				if(j<par):
					pp = (pow(-1,n)*j).astype(int)    
				else:
					pp = 2-j
				Aaux0 = GenerarMatriz(A,n+pp,arr,1)
				B1 = np.around(np.matmul(Aaux1,Aaux0),6).astype(float)
				print ("\n\n\t Realizando las operaciones:\n",Aaux1,"\n\t multiplicado por:\n",Aaux0,"\n\tigual a:\n",B1)
				ppp= (pow(-1,n+1)*j).astype(int)
				Aaux0 = GenerarMatriz(A,n+ppp,arr,1)
				C= Aaux0 - B1
				print ("\n\n\t Realizando las operaciones:\n",Aaux0,"\n\t restado a:\n",B1,"\n\tigual a:\n",C)
				A[n+ppp] = str(C)
			Aaux2 = GenerarMatriz(B,n-1,arr,0)
			B2 = np.around(np.matmul(Aaux1,Aaux2),6).astype(float)
			Aaux3 = GenerarMatriz(B,n%2,arr,0)
			Aaux2 = Aaux3 - B2
			print ("\n\n\t Realizando las operaciones:\n",Aaux3,"\n\t restado a:\n",B2,"\n\tigual a:\n",Aaux2)
			B[n%2] = str(Aaux2) 
			return n

def CreaCadenas(n):
		arr = np.array([])
		x = range(1,n+1)
		for i in x:
			arr = np.append(arr,i).astype(int)
		return arr

def GenerarMatriz(A,i,arr,cen):
		if(cen == 0):  
			B = np.asmatrix(A[i])  
			n=i*4   
			B = B.reshape(int(arr[n]),1)  
		else:  
			B = np.asmatrix(A[i])  
			n = i * 2  
			B = B.reshape(int(arr[n]),int(arr[n+1]))  
		return B

def Explicacion(k):
		if (k==0):
			print ("\n\tPremultiplicación de todos los elementos del primer renglón de A por (A_11)^-1\n\t, la inversa del pivote obteniendóse:\n")
		elif (k==1):
			print ("\n\tRestar a los elementos matriciales del segundo renglón los correspondientes\n\t elementos del primer renglón premultiplicados por A_21, el elemento que se trata\n\t de eliminar, obteniéndose:\n")
		elif (k==2):
			print ("\n\tPremultiplicaci´pn de los elementos del segundo renglón por (A_22)^-1, la inversa\n\tdel nuevo pivote, obteniéndose:\n")
		elif (k==3):
			print ("\n\tFinalmente, restar de los elementos del primer renglón los correspondientes\n\telementos del segundo, premultiplicados previamente por A'_12, el elemento\n\tmatricial que ahora se trata de eliminar, obteniéndose:\n")
		else:
			print ("Iteración no reoonocida")
		return

def GeneradorMatriz():
	dim=int(input("¿Cual es la dimensión de la matriz? "))
	matriz = np.array([])
	list_for=range(dim)
	for i in list_for:	
		print(i)
		for j in list_for:
			print("a[",i+1,"][",j+1,"]")
			matriz = np.append(matriz,float(input()))
	matriz = matriz.reshape(dim,dim)
	vectorRecursos =np.array([])
	for i in list_for:
		print("b[",i+1,"]")
		vectorRecursos = np.append(vectorRecursos,float(input()))
	vectorRecursos=vectorRecursos.reshape(dim,1)
	print("A:\n",matriz,"\nb:\n",vectorRecursos)
	return matriz,vectorRecursos

matriz,matrizRecursos=GeneradorMatriz()
order=np.array([0,1,3,2])
a=ValidadorMetodo(matriz,matrizRecursos)
print(CreaCadenas(2))
if a!=0:
	A,B,arr = ParticionarMatriz(a,matriz,matrizRecursos,int(input("a : ")),int(input("b :")))
	GaussJordan(A,B,order[0],arr,2,order,0)

