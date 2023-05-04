import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from main import *

class CajeroApp:
    def __init__(self, cajero):
        self.cajero = cajero
        
        self.root = tk.Tk()
        self.root.title("Cajero Automático")
        
        self.nombre_label = tk.Label(self.root, text="Nombre:")
        self.nombre_label.grid(row=0, column=0)
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.grid(row=0, column=1)
        
        self.apellido_label = tk.Label(self.root, text="Apellido:")
        self.apellido_label.grid(row=1, column=0)
        self.apellido_entry = tk.Entry(self.root)
        self.apellido_entry.grid(row=1, column=1)
        
        self.edad_label = tk.Label(self.root, text="Edad:")
        self.edad_label.grid(row=2, column=0)
        self.edad_entry = tk.Entry(self.root)
        self.edad_entry.grid(row=2, column=1)
        
        self.deposito_label = tk.Label(self.root, text="Depósito:")
        self.deposito_label.grid(row=3, column=0)
        self.deposito_entry = tk.Entry(self.root)
        self.deposito_entry.grid(row=3, column=1)
        
        self.retiro_label = tk.Label(self.root, text="Retiro:")
        self.retiro_label.grid(row=4, column=0)
        self.retiro_entry = tk.Entry(self.root)
        self.retiro_entry.grid(row=4, column=1)
        
        self.saldo_label = tk.Label(self.root, text="Saldo:")
        self.saldo_label.grid(row=5, column=0)
        self.saldo_entry = tk.Entry(self.root)
        self.saldo_entry.grid(row=5, column=1)
        
        self.id_label = tk.Label(self.root, text="ID: ")
        self.id_label.grid(row=6, column=0)
        self.id_entry = tk.Entry(self.root)
        self.id_entry.grid(row=6, column=1)
        # BOTONES
        
        self.deposito_button = tk.Button(self.root, text="Depositar", command=self.deposito,padx=20)
        self.deposito_button.grid(row=7, column=0)
        
        self.retiro_button = tk.Button(self.root, text="Retirar", command=self.retiro,padx=20)
        self.retiro_button.grid(row=7, column=1)
        
        self.saldo_button = tk.Button(self.root, text="Ver Saldo", command=self.mostrar_saldo)
        self.saldo_button.grid(row=8, column=0)
        
        self.salir_button = tk.Button(self.root, text="Salir", command=self.salir)
        self.salir_button.grid(row=8, column=1)
        
        self.root.mainloop()
    
    
    # En proceso
    
    def deposito(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        ide = int(self.id_entry.get())
        
        cuenta = self.cajero.buscar_cuenta(ide)
        if cuenta:
            cuenta.depositar(deposito)
            self.saldo_entry.delete(0, tk.END)
            self.saldo_entry.insert(0, cuenta.get_dinero())
        else:
            self.saldo_entry.delete(0, tk.END)
            self.saldo_entry.insert(0, "Cuenta no encontrada")
    
    def retiro(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        edad = int(self.edad)
    def mostrar_saldo(self):
        pass
    def salir(self):
        pass
    
    
cuenta_1=CajeroApp(Cajero())




# root = tk.Tk()
# root.title("Cajero Automático")
# nombre_label = tk.Label(root, text="Nombre:")
# nombre_label.grid(row=0, column=0)
# nombre_entry = tk.Entry(root)
# nombre_entry.grid(row=0, column=1)

# apellido_label = tk.Label(root, text="Apellido:")
# apellido_label.grid(row=1, column=0)
# apellido_entry = tk.Entry(root)
# apellido_entry.grid(row=1, column=1)

# edad_label = tk.Label(root, text="Edad:")
# edad_label.grid(row=2, column=0)
# edad_entry = tk.Entry(root)
# edad_entry.grid(row=2, column=1)

# deposito_label = tk.Label(root, text="Depósito:")
# deposito_label.grid(row=3, column=0)
# deposito_entry = tk.Entry(root)
# deposito_entry.grid(row=3, column=1)

# retiro_label = tk.Label(root, text="Retiro:")
# retiro_label.grid(row=4, column=0)
# retiro_entry = tk.Entry(root)
# retiro_entry.grid(row=4, column=1)
        
# saldo_label = tk.Label(root, text="Saldo:")
# saldo_label.grid(row=5, column=0)
# saldo_entry = tk.Entry(root)
# saldo_entry.grid(row=5, column=1)

# root.mainloop()

