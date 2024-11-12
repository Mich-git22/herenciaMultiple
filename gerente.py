# gerente.py
from empleado import Empleado
from area import Area

class Gerente(Empleado, Area):
    def __init__(self, nombre, edad, id_empleado, salario, nombre_depto, nombre_area, proyectos):
        Empleado.__init__(self, nombre, edad, id_empleado, salario)
        Area.__init__(self, nombre_depto, nombre_area)
        self._proyectos = proyectos  # atributo privado

    def get_proyectos(self):
        return self._proyectos

    def set_proyectos(self, proyectos):
        self._proyectos = proyectos
