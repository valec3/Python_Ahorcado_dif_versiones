class Usuario:
    usuarios_cant = 0
    def __init__(self,name,password):
        self.nombre=name
        self.contra=password
        
        self.conectado=False
        self.intentos=3
        self.usuarios_cant+=1
        
    def conectar(self,contra_inp=None):
        if contra_inp == None:
            contra_inp=input("Ingresa tu contraseña: ")
        # else:
        #     self.contra=contra_inp
            
        if contra_inp == self.contra:
            print("Te has logeado correctamente")
            self.conectado=True
        else:
            self.intentos-=1
            if self.intentos==0:
                print("ERROR no se pudo iniciar sesion :(")
            else:    
                print(f"Intentos restantes: {self.intentos}\nContraseña Incorrecta")
                # self.conectar()
        return self.conectado
    def desconectar(self):
        if self.conectado == True:
            print("Se cerro secion con exito")
            self.conectado=False
        else:
            print("Error No has iniciado sesion :)")
    def __str__(self):
        estado="conectado" if self.conectado == True else "desconectado"
        return f"Mi nombre de usuario es {self.nombre} y estoy {estado}"            
    
