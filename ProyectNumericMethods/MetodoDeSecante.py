import math
import prettytable
import sympy as sym 
from sympy import *
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np 

def MetodoDeSecante(N,f,a,b,cen,TOL,cifra):
		y= PrettyTable()
		n=0
		val1=0
		val_act =b
		val_ant =a
		x=sym.symbols('x')
		xi=val_act -val_ant
		y.field_names=["n","x_i+1","f(x_i)","f(x_i-1)","x_i-x_i-1","error"]
		while n<N:
			if val1==val_act:
				break
			else:
				if n==0:
					error=0
					y.add_row([n,val_ant,'-','-','-','-'])
					n+=1
				else:
					if(cen!=0):
						xn=round(math.radians(f.evalf(subs={x:val_act})),cifra) 
						xn1=round(math.radians(f.evalf(subs={x:val_ant})),cifra) 
					else:
						xn=round(f.evalf(subs={x:val_act}),cifra) 
						xn1=round(f.evalf(subs={x:val_ant}),cifra) 
					xi=round(val_act -val_ant,cifra) 
					y.add_row([n,val_act,xn,xn1,xi,error])
					val=round(val_act-xn*(xi/(xn-xn1)),cifra)
					val1=val_act
					val_ant=val_act
					val_act=val
					error=round(abs((val-val1)/val),cifra)
					if(error<TOL):
						break
					n+=1
		print (y,"\n\nLa raíz es:\n",val)
		return n

def GeneradorFucion(f):
		n=0
		m=5000
		xaxis = np.linspace(-10,10,m)
		x=sym.symbols('x')
		val=xaxis[n]
		xn=round(f.evalf(subs={x:val}),10)
		np_yaxis=np.array([xn])
		while (n<=m-2):
			val=xaxis[n]
			xn=round(f.evalf(subs={x:val}),10)
			yaxis=np.append(np_yaxis,xn)
			np_yaxis=yaxis
			n+=1 
		Grafica(xaxis,yaxis)

def Grafica(x,y):
		fig = plt.figure()
		ax = fig.add_subplot(1, 1, 1)
		ax.spines['left'].set_position('zero')	
		ax.spines['bottom'].set_position('zero')	
		ax.spines['right'].set_color('none')
		ax.spines['top'].set_color('none')
		ax.xaxis.set_ticks_position('bottom')
		ax.yaxis.set_ticks_position('left')
		plt.plot(x,y,'r')
		plt.show()		



def NumeroIteraciones(a,b,TOL):
		val = (b-a)/TOL
		N= (math.log10(val)/math.log10(2))
		print (N)
		return N

def TabulaFuncion(a,b,f,cen,cifra):
		n=0
		m=10
		y = PrettyTable()
		y.field_names=["x","f(x)"]
		x=sym.symbols('x')
		xaxis = np.linspace(a,b,m)
		while n<=m-1:
			val = round(xaxis[n],cifra)
			if(cen!=0):
				xn=round(math.radians(f.evalf(subs={x:val})),cifra)
			else:
				xn=round(f.evalf(subs={x:val}),cifra)
			y.add_row([val,xn])
			n+=1
		print("\tGrafica de la función:\n",y)

def main():
	print("Ingresa intervalo inicial")
	a= int(input("a:"))
	b= int(input("b:"))
	TOL= float(input("ingresa la tolerancia:"))
	cifra = int(input("ingresa el numero de cifras significativas:"))
	cen1 = input("¿Tu función contiene alguna identidad trigonomtrica?[y/n]:")
	if(cen1 == 'y'):
		cen=1
	elif(cen1 =='n'):
		cen=0
	else:
		print("Opción equivocada")
	ingress = input("dame la función: ") 
	x=sym.symbols('x')
	f = parse_expr(ingress)
	N = NumeroIteraciones(a,b,TOL)
	TabulaFuncion(a,b,f,cen,cifra)
	print("\n\tMetodo de Secante\n")
	MetodoDeSecante(N,f,a,b,cen,TOL,cifra)
	GeneradorFucion(f)

main()


