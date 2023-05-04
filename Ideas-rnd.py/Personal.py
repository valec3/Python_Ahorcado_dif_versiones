class Persona:
    def __init__(self,nombre,apellido,edad,sexo) -> None:
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.sexo=sexo
    def __str__(self):
        return f"Usuario:\t{self.nombre}\n{self.apellido}\n{self.edad}\n{self.sexo}"
class Empresa:
    empleados=[]
    def agregar_empleado(self):
        datos = tuple(input().split())
        new_empleado = Empleado(*datos)
        self.empleados.append(new_empleado)
class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, sexo,salario,posicion):
        super().__init__(nombre, apellido, edad, sexo)
        self.salario=salario
        self.posicion=posicion
        
    def calcular_Salario(self)->None:
        """_summary_
        """
        self.salario=2000
    

