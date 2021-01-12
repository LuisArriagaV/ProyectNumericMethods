import math
import prettytable
import sympy as sym 
from sympy import *
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np 

def MetodoDeNewton(N,f,a,cen,TOL,cifra):
		y= PrettyTable()
		n=0
		val1=0
		val=a
		x=sym.symbols('x')
		g=sym.diff(f,x);
		print ("la derivada es: ",g)
		y.field_names=["n","x_n+1","f(x_n)","f'(x_n)","error"]
		while n<N:
			if val1==val:
				break
			else:
				if n==0:
					n+=1
					error=0
				else:
					if(cen!=0):
						xn=round(math.radians(f.evalf(subs={x:val})),cifra)
						xpn=round(math.radians(g.evalf(subs={x:val})),cifra)
					else:
						xn=round(f.evalf(subs={x:val}),cifra)
						xpn=round(g.evalf(subs={x:val}),cifra)
					y.add_row([n,val,xn,xpn,error])
					val1=val
					val=round(val-xn/xpn,cifra)
					error=round(abs((val1-val)/val),cifra)
					if(error<TOL):
						break
					n+=1	
		print (y,"\n\nLa raíz es:\n",val)
		return 

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
	print("\n\tMetodo de Newton\n")
	MetodoDeNewton(N,f,a,cen,TOL,cifra)
	GeneradorFucion(f)

main()



