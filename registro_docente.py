from io import open 
from tkinter import *
from tkinter import messagebox as mb 
import getpass

print('BIENVENIDO USUARIO\n')
op=int(input('INGRESE OPCIÓN 1 PARA MODULO DE DOCENTE O 2 PARA MODULO DE ESTUDIANTE:'))
if op==1:
   def guardar():
      nombre_data =nombre.get()
      apellido_data =apellido.get()
      usuario_data =usuario.get()
      contra_data =str(contra.get())
      print(nombre_data,"\t",apellido_data,"\t",usuario_data,"\t",contra_data,"\t")

      archivo= open("registro_docente.txt","a")
      archivo.write(nombre_data)
      archivo.write("\t")
      archivo.write(apellido_data)
      archivo.write("\t")
      archivo.write(usuario_data)
      archivo.write("\t")
      archivo.write(contra_data)
      archivo.write("\n")
      archivo.close()
      print('nuevo registro. nombre:{}| apellido:{}'.format(usuario_data,nombre_data))

      nombre_entry.delete(0,END)
      apellido_entry.delete(0,END)
      usuario_entry.delete(0,END)
      contra_entry.delete(0,END)
    


   ventana= Tk()
   ventana.geometry("660x550")
   ventana.title("modulo de registro de docente")
   ventana.resizable(False,False)
   ventana.config(background="mint cream")
   main_tittle = Label(text="BIENVENIDO AL REGISTRO DE DOCENTE",font=("Cambria",13),bg="deep sky blue",fg="white",width="550",height="2")
   main_tittle.pack()
   idea_label=Label(text="RECUERDE CERRAR LA VENTANA PARA CONTINUAR CON EL REGISTRO DE NOTAS").pack(anchor=CENTER)
   nombre_label= Label(text="nombre",bg="salmon")
   nombre_label.place(x=22, y=70)
   apellido_label= Label(text="apellido",bg="salmon")
   apellido_label.place(x=22,y=120)
   usuario_label= Label(text="usuario",bg="salmon")
   usuario_label.place(x=22, y=170)
   contra_label= Label(text="contraseña",bg="salmon")
   contra_label.place(x=22,y=220)

   nombre= StringVar()
   apellido= StringVar()
   usuario= StringVar()
   contra= StringVar()
 

   nombre_entry= Entry(textvariable=nombre,width="40")
   apellido_entry= Entry(textvariable=apellido,width="40")
   usuario_entry= Entry(textvariable=usuario,width="40")
   contra_entry= Entry(textvariable=contra,width="40", show="*")


   nombre_entry.place(x=22, y=100)
   apellido_entry.place(x=22, y=150)
   usuario_entry.place(x=22,y=200)
   contra_entry.place(x=22, y=250)


   boton= Button(ventana,text="guardar informacion",command=guardar,width="30",height="2",bg="cyan")
   boton.place(x=22, y=320)

   ventana.mainloop()
   confirmar= getpass.getpass('INGRESE LA CONTRASEÑA:')
   contrasena=getpass.getpass('PARA CONFIRMAR SU CONTRASEÑA INGRESELA NUEVAMENTE:')
   if confirmar==contrasena:
      print('contraseña correcta')
      from registro import *
   else:
      print('CONTRASEÑA INCORRECTA POR FAVOR CIERRE LA VENTANA E INTENTE NUEVAMENTE')

if op==2:
   from graficas import*


