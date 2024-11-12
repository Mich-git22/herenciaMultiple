# departamento.py
class Departamento:
    def __init__(self, nombre_depto):
        self._nombre_depto = nombre_depto  # atributo privado

    def get_nombre_depto(self):
        return self._nombre_depto

    def set_nombre_depto(self, nombre_depto):
        self._nombre_depto = nombre_depto
