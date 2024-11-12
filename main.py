# main.py
from director import Director
from gerente import Gerente
from jefearea import JefeArea

def main():
    director = Director("Carlos", 45, "D001", 80000, "Recursos Humanos", "Contratación", "Gestionar estrategia")
    gerente = Gerente("Laura", 38, "G001", 60000, "Finanzas", "Presupuesto", "Supervisar proyectos")
    jefe_area = JefeArea("Ana", 35, "J001", 50000, "Tecnología", "Desarrollo", "Equipo de desarrollo")

    print(f"Director: {director.get_nombre()}, Edad: {director.get_edad()}, Departamento: {director.get_nombre_depto()}, Área: {director.get_nombre_area()}, Responsabilidades: {director.get_responsabilidades()}")
    print(f"Gerente: {gerente.get_nombre()}, Edad: {gerente.get_edad()}, Departamento: {gerente.get_nombre_depto()}, Área: {gerente.get_nombre_area()}, Proyectos: {gerente.get_proyectos()}")
    print(f"Jefe de Área: {jefe_area.get_nombre()}, Edad: {jefe_area.get_edad()}, Departamento: {jefe_area.get_nombre_depto()}, Área: {jefe_area.get_nombre_area()}, Equipo: {jefe_area.get_equipo()}")

if __name__ == "__main__":
    main()
