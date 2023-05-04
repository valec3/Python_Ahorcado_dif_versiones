
class Cajero:
    
    def __init__(self):
        self.__cuentas = []
    
    def agregar_cuenta(self, cuenta):
        self.__cuentas.append(cuenta)
    
    def buscar_cuenta(self, numero_cuenta):
        for cuenta in self.__cuentas:
            if cuenta.get_id() == numero_cuenta:
                print("\n>>> Cuenta encontrada <<<")
                return cuenta
        return None
    
    def mostrar_cuentas(self):
        for c in self.__cuentas:
            print(c)

class Cuenta:
    last_id=0
    def __init__(self,nombre,apellido,edad,dinero=5000):
        self.id = Cuenta.last_id + 1
        self.name=nombre
        self.lname=apellido
        self.age=edad
        self.__dinero=dinero
        Cuenta.last_id += 1
    
    def retirar(self,monto):
        if monto < self.__dinero:
            self.__dinero-=monto
        else:
            print("Monto invalido")
    def __str__(self):
        return f"{'_'*20}\nID: {self.id}\nName: {self.name}\nLast name: {self.lname}\nAge: {self.age}\nBalance: {self.__dinero}"
    def depositar(self,monto):
        self.__dinero+=monto
    def get_dinero(self):
        return self.__dinero
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.id
    def mostrar_historial(self):
        return 
    def transferir_saldo(self,cuenta_obj):
        pass
    
    
cuentas=[]
cuentas.append(Cuenta("Juan", "Diaz",18,6000))
cuentas.append(Cuenta("Juan", "Pérez", 25, 5000))
cuentas.append(Cuenta("María", "García", 32, 5000))
cuentas.append(Cuenta("Pedro", "Martínez", 40, 5000))
cuentas.append(Cuenta("Ana", "Sánchez", 19, 5000))
cuentas.append(Cuenta("Luis", "González", 55, 5000))

Piura_cjr=Cajero()
for c in cuentas:
    Piura_cjr.agregar_cuenta(c)
    

# Piura_cjr.mostrar_cuentas()
# print(Piura_cjr.buscar_cuenta(6))