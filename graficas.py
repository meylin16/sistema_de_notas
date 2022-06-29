from re import T
import matplotlib.pyplot as plt
from registro import *
def reporte1():
    print('BIENVENIDO ESTUDIANTE')
    x = []
    for renglon in llenar:
        arg=renglon.get('DOCUMENTO')
        x.append(arg)
    print(x)

    y= []
    for renglon in llenar:
        arg=renglon.get('NOTA1')
        y.append(arg)
    print(y)
    
    plt.plot(x, y, marker= 'o', linestyle='--')
    plt.xlabel('DOCUMENTOS')
    plt.ylabel('NOTAS')
    plt.title('REPORTE DE NOTAS CORTE 1')
    plt.show()
nota1=reporte1()

def reporte2():
    x = []
    for renglon in llenar:
        arg=renglon.get('DOCUMENTO')
        x.append(arg)
    print(x)

    y= []
    for renglon in lista:
        arg=renglon.get('NOTA2')
        y.append(arg)
    print(y)

    plt.plot(x, y, marker= 'o', linestyle='--')
    plt.xlabel('DOCUMENTOS')
    plt.ylabel('NOTAS')
    plt.title('REPORTE DE NOTAS CORTE 2')
    plt.show()
nota2=reporte2()

def menu_reportes():
    print("Elige opcion 1: Reporte de Notas corte 1")
    print("Elige opcion 2: Reporte de Notas corte 2")
    print("Elige opcion 3: Salir")
    opcion=int(input("Elige una opcion: "))
    while (opcion<1 or opcion>3):
        print("Opcion no valida")
        opcion=int(input("Elige una opcion: "))
        if (opcion==1):
            print(reporte1())
        elif (opcion==2):
            print(reporte2())
        elif (opcion==3):
            print(quit())

menu=menu_reportes()



