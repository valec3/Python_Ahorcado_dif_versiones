import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from usuario import Usuario

usuarios=[]
def create_gui():
    # Ventana Principal
    root = tk.Tk()
    root.title("Login usuario")
    # Subventanas
    mainframe = tk.Frame(root)
    mainframe.pack()
    mainframe.config(width = 480,height=320,bg="lightblue")

    titulo=tk.Label(mainframe,text="Login de usuario",font=("Arial",24))
    titulo.grid(column=0,row=0,padx=10,pady=15,columnspan=2)

    name =tk.Label(mainframe,text="Nombre: ")
    name.grid(column=0,row=1)
    contra =tk.Label(mainframe,text="Contraseña: ")
    contra.grid(column=0,row=2)

    # INPUT
    global name_user
    name_user=tk.StringVar()
    name_user.set("")
    name_i = tk.Entry(mainframe,textvariable=name_user)
    name_i.grid(column=1,row=1)

    global contra_user
    contra_user=tk.StringVar()
    contra_user.set("")
    contra_i = tk.Entry(mainframe,textvariable=contra_user, show="*")
    contra_i.grid(column=1,row=2)

    # BOTONES

    style = ttk.Style()
    style.configure('my.TButton', background='blue', foreground='black')

    iniciar_ses_btn = ttk.Button(mainframe, text='Iniciar sesión', style='my.TButton',command=iniciar_sesion)
    iniciar_ses_btn.grid(column=1,row=3,ipadx=5,ipady=2,padx=10,pady=10)

    registrar_ses_btn=ttk.Button(mainframe,text="Registrar",style = "my.TButton",command=registrar_usuario)
    registrar_ses_btn.grid(column=0,row=3,ipadx=5,ipady=2,padx=10,pady=10)
    
    # CORRER VENTANA
    root.mainloop()


def iniciar_sesion():
    for user in usuarios:
        if user.nombre==name_user.get():
            estado = user.conectar(contra_user.get())
            if estado:
                messagebox.showinfo("Conectado","Se inicio sesion con exito")
            else:
                messagebox.showinfo("Error","Contraseña incorrecta")
            break
    else:
        messagebox.showerror("Error","Usuario inexistente")
def registrar_usuario():
    name = name_user.get()
    password = contra_user.get()
    usuarios.append(Usuario(name,password))
    messagebox.showinfo("Exito",f"Se registro el nuevo usuario {name}")
    contra_user.set("")
    name_user.set("")

    
if __name__ == "__main__":
    user_1=Usuario("Juan","147")
    usuarios.append(user_1)
    create_gui()

