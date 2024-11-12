# persona.py
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # atributo privado
        self._edad = edad      # atributo privado

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad
