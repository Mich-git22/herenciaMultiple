# empleado.py
from persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, id_empleado, salario):
        super().__init__(nombre, edad)
        self._id_empleado = id_empleado  # atributo privado
        self._salario = salario          # atributo privado

    def get_id_empleado(self):
        return self._id_empleado

    def set_id_empleado(self, id_empleado):
        self._id_empleado = id_empleado

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        self._salario = salario
