# jefearea.py
from empleado import Empleado
from area import Area

class JefeArea(Empleado, Area):
    def __init__(self, nombre, edad, id_empleado, salario, nombre_depto, nombre_area, equipo):
        Empleado.__init__(self, nombre, edad, id_empleado, salario)
        Area.__init__(self, nombre_depto, nombre_area)
        self._equipo = equipo  # atributo privado

    def get_equipo(self):
        return self._equipo

    def set_equipo(self, equipo):
        self._equipo = equipo
