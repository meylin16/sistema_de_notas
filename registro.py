def llenar_registro():
    archivo=open('registro_estudiantes.txt',"w")
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
    print(lista,file=archivo)
    return lista



def sabernota():
    documentos=open('nota_estudiante.txt',"w")
    sabernotas=[]
    doc=int(input('ingrese documento:'))
    while doc<1000:
        print('error')
        doc=int(input('ingrese documento:'))
    for i in range (len(llenar)):
        for j in llenar[i].values():
            if j==doc:
                sabernotas.append(llenar[i])
    new_lista=[]
    for i in range(len(sabernotas)):
        for j in sabernotas[i].values():
            new_lista.append(j)
        new_lista.pop(0)
    suma=0
    for i in range(len(new_lista)):
        suma=suma+new_lista[i]
    resultado=suma/len(new_lista)
    print(resultado,file=documentos)
    return (resultado)
    