import os 
import numpy as np
os.system("clear")
print("\t\tMetodos Numericos I")
print ("\t1. Metodo de Newton")
print ("\t2. Metodo de Secante")
print ("\t3. Metodo de Gauss Particionado")
print ("\t4. Metodo de Doolittle")
print ("\t5. Documentacion Completa de los Metodos")
print ("\t6. Salir")


print ("Elige una opcion")
 
salir = False
opcion = 0
while not salir:
    
    opcion = int(input())
    if opcion == 1:
        os.system("clear")
        print("\n\tMetodo de Newton")
        print("El método de Newton es una de las técnicas numéricas más poderosas y \nconocidas,para determinar las raíces de una ecuación")
        print("a única manera de alcanzar la convergencia es seleccionar un valor inicial \nlo suficientemente cercano a la raíz buscada. \nAsí, se ha de comenzar la iteración con un valor razonablemente cercano al cero ")
        os.system("python3 MetodoDeNewton.py")
        salir= input("Presione una numero y enter para regresar al menu: ")
        os.system("clear")
        os.system("python3 menu.py")
    elif opcion == 2:
        os.system("clear")
        print("\n\tMetodo de Secante")
        print("Es una variación del método de Newton-Raphson donde en vez de calcular la derivada de la función")
        print("en el punto de estudio, teniendo en mente la definición de derivada, \nse aproxima la pendiente a la recta que une la función")
        print("evaluada en el punto de estudio y en el punto de la iteración anterior. ")
        print("Este método es de especial interés cuando el coste computacional de derivar la función de estudio y ")
        print("evaluarla es demasiado elevado, por lo que el método de Newton \nno resulta atractivo.")
        os.system("python3 MetodoDeSecante.py")
        salir= input("Presione una numero y enter para regresar al menu: ")
        os.system("clear")
        os.system("python3 menu.py")
    elif opcion == 3:
        os.system("clear")
        print("\n\tMetodo de Gauss Particionado")
        print("Este método nos ayuda a encontrar la solución de un sistema de ecuaciones con un")
        print("número muy grande de variables, utilizando el método de Gass-Jordan \npero con matrices en vez de valores.")
        print("")
        os.system("python3 GaussParticionado.py")
        salir= input("Presione una numero y enter para regresar al menu: ")
        os.system("clear")
        os.system("python3 menu.py")
    elif opcion == 4:
        os.system("clear")
        print("Metodo de Doolittle")
        print("En álgebra lineal, se conoce por factorización LU de matrices al proceso que a partir de una matriz cuadrada A")
        print("halla dos matrices triangulares inferior y superior, tal que A=LU, donde L es la matriz triangular inferior (L de lower)")
        print("y U es la matriz triangular superior (U de upper).") 
        os.system("python3 doolittle.py")
        salir= input("Presione una numero y enter para regresar al menu: ")
        os.system("clear")
        os.system("python3 menu.py")
    elif opcion == 5:
        os.system("evince DocMeth.pdf")
        salir= input("Presione una numero y enter para regresar al menu: ")
        os.system("clear")
        os.system("python3 menu.py")
    elif opcion == 6:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 5")


print ("Fin")
os.system("clear")
print("Programa creado por:")
print("Arriaga Vazquez Luis Fernando")
print("Garcia Perez Salomon")
print("Orozco Pacheco Moises")
print("Ramirez Valdespino Alan")
