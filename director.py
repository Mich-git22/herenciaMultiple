# director.py
from empleado import Empleado
from area import Area

class Director(Empleado, Area):
    def __init__(self, nombre, edad, id_empleado, salario, nombre_depto, nombre_area, responsabilidades):
        Empleado.__init__(self, nombre, edad, id_empleado, salario)
        Area.__init__(self, nombre_depto, nombre_area)
        self._responsabilidades = responsabilidades  # atributo privado

    def get_responsabilidades(self):
        return self._responsabilidades

    def set_responsabilidades(self, responsabilidades):
        self._responsabilidades = responsabilidades
