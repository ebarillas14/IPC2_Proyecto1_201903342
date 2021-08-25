from helpers import *
from TDA import *
from graphviz import *
import os


def show_developer_info():
    print("============= DATOS DEL DESARROLLADOR =============")
    print(" Eduardo Abraham Barillas del Aguila")
    print(" Introducción a la Programación y Computación \"C\"")
    print(" Carné: 201903342")
    print("Ingeniería en Ciencias y Sistemas")
    print("4to Semestre")
    print("===================================================")


def generate_graphic(terrain):
    matrix = terrain.matrix
    dot = Graph(f'{terrain.name}', format='jpg')
    dot.graph_attr['rankdir'] = 'TB'
    for y in range(matrix.rows):
        for x in range(matrix.columns):
            value = matrix.get_value(x, y)
            # dot.node(f"r{y}c{x}", f"y{y}x{x}  VALUE {value}", shape="box")
            dot.node(f"r{y}c{x}", f"{value}", shape="box")
        for x in range(matrix.columns-1):
            dot.edge(f"r{y}c{x}", f"r{y}c{x+1}", "", constraint="false")
    for y in range(matrix.rows-1):
        for x in range(matrix.columns):
            dot.edge(f"r{y}c{x}", f"r{y+1}c{x}")
    dot.render(terrain.name)
    os.system(f"{terrain.name}.jpg")
    pass


def display_menu():
    menu_flag = True
    terrains = LinkedList()
    while menu_flag:
        print("===================================================")
        print("              QUE DESEAS HACER ?                   ")
        print("===================================================")
        print("(1) Cargar Archivo")
        print("(2) Procesar Archivo")
        print("(3) Escribir Archivo de Salida")
        print("(4) Mostrar Datos del Estudiante")
        print("(5) Generar Gráfica")
        print("(6) Salida")
        response = input("Ingresa solo el numero de la opcion \n")
        validated_option = validate_number(response, 1, 6)
        if validated_option is not None:
            if validated_option == 1:
                route = input("Ingresa la ruta del archivo a abrir \n")
                tmp_terrains = load_xml(route)
                terrains.append(tmp_terrains)
            elif validated_option == 2:
                pass
            elif validated_option == 3:
                pass
            elif validated_option == 4:
                show_developer_info()
            elif validated_option == 5:
                if terrains.len() == 0 :
                    print("No has cargador ningún terreo, por favor carga al menos un terreno")
                else:
                    print("Terrenos previamente cargados:")
                    print("==============================")
                    terrains.get_all_names()
                    print("==============================")
                    name = input("ingresa el nombre del terreno a mostrar")
                    terrain = terrains.get(name)
                    generate_graphic(terrain)
            else:
                menu_flag = False




if __name__ == '__main__':
    display_menu()


