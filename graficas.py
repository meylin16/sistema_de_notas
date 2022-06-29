from re import T
import matplotlib.pyplot as plt
<<<<<<< HEAD

def llenar_registro():
    lista=[]
    estudiantes=int(input('cuantos estudiantes desea ingresar:'))
    for i in range(estudiantes):
        documento=int(input('ingrese el numero del documento:'))
        while documento<1000:
            print('error')
            documento=int(input('ingrese el numero del documento:'))
        nota1=float(input('ingrese la nota del corte 1:'))
        nota2=float(input('ingrese la nota del corte 2:'))
        datos={'DOCUMENTO':documento,'NOTA1':nota1,'NOTA2':nota2}
        lista.append(datos)
    return lista

lista=llenar_registro()
print(lista)

=======
from registro import *
>>>>>>> deb0ad3e028d3640955779bccf36c4adb1ddacc6
def reporte1():
    print('BIENVENIDO ESTUDIANTE')
    x = []
<<<<<<< HEAD
    for renglon in lista:
=======
    for renglon in llenar:
>>>>>>> deb0ad3e028d3640955779bccf36c4adb1ddacc6
        arg=renglon.get('DOCUMENTO')
        x.append(arg)
    print(x)

    y= []
<<<<<<< HEAD
    for renglon in lista:
=======
    for renglon in llenar:
>>>>>>> deb0ad3e028d3640955779bccf36c4adb1ddacc6
        arg=renglon.get('NOTA1')
        y.append(arg)
    print(y)
    
    plt.plot(x, y, marker= 'o', linestyle='--')
    plt.xlabel('DOCUMENTOS')
    plt.ylabel('NOTAS')
    plt.title('REPORTE DE NOTAS CORTE 1')
    plt.show()
<<<<<<< HEAD
#report1=reporte1()

def reporte2():
    x = []
    for renglon in lista:
=======
nota1=reporte1()

def reporte2():
    x = []
    for renglon in llenar:
>>>>>>> deb0ad3e028d3640955779bccf36c4adb1ddacc6
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
<<<<<<< HEAD
#report2=reporte2()
=======
nota2=reporte2()
>>>>>>> deb0ad3e028d3640955779bccf36c4adb1ddacc6

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
report=menu_reportes()

menu=menu_reportes()



