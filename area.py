# area.py
from departamento import Departamento

class Area(Departamento):
    def __init__(self, nombre_depto, nombre_area):
        super().__init__(nombre_depto)
        self._nombre_area = nombre_area  # atributo privado

    def get_nombre_area(self):
        return self._nombre_area

    def set_nombre_area(self, nombre_area):
        self._nombre_area = nombre_area
