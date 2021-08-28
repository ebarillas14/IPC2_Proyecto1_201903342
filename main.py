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
            dot.node(f"r{y}c{x}", f"{value}", shape="box")
        for x in range(matrix.columns-1):
            dot.edge(f"r{y}c{x}", f"r{y}c{x+1}", "", constraint="false")
    for y in range(matrix.rows-1):
        for x in range(matrix.columns):
            dot.edge(f"r{y}c{x}", f"r{y+1}c{x}")
    dot.render(terrain.name)
    os.system(f"{terrain.name}.jpg")
    pass


def process_terrain_v2(terrain):
    st = Stack()
    cont = 0
    px = pxo = int(terrain.pxo) - 1
    py = pyo = int(terrain.pyo) - 1
    pxf = int(terrain.pxf)-1
    pyf = int(terrain.pyf) - 1
    pm = possible_moves(terrain, px, py)
    tmp = pm.First
    while tmp.Next is not None:
        st.push(tmp.px, tmp.py, tmp.data)
        tmp = tmp.Next
    st.push(tmp.px, tmp.py, tmp.data)

    px = st.peek().px
    py = st.peek().py
    while px != pxf or py != pyf:
        print(f"Se han realizado {cont} iteraciones")
        pm = possible_moves(terrain, px, py)
        tmp = pm.First
        while tmp.Next is not None:
            st.push(tmp.px, tmp.py, tmp.data)
            cont += 1
            tmp = tmp.Next
        st.push(tmp.px, tmp.py, tmp.data)
        cont += 1
        px = st.peek().px
        py = st.peek().py

    st.show_stack()


def process_terrain(terrain):
    st = Stack()
    cont = 0
    px = pxo = int(terrain.pxo) - 1
    py = pyo = int(terrain.pyo) - 1
    pxf = int(terrain.pxf)-1
    pyf = int(terrain.pyf) - 1
    data = terrain.matrix.get_value(px, py)
    st.push(px, py, data)

    px = st.peek().px
    py = st.peek().py
    while px != pxf or py != pyf:
        print(f"Se han realizado {cont} iteraciones")
        pm = possible_moves(terrain, px, py)
        tmp = pm.First
        st.push(tmp.px, tmp.py, tmp.data)
        cont += 1
        px = st.peek().px
        py = st.peek().py

    st.show_stack()


def possible_moves(terrain, px, py):
    poss_moves = BasicLinkedList()
    pxo = int(terrain.pxo) - 1
    pyo = int(terrain.pyo) - 1
    pxf = int(terrain.pxf) - 1
    pyf = int(terrain.pyf) - 1
    r_value = l_value = u_value = d_value = 0
    if pyo < pyf:
        if pxo < pxf:
            if px + 1 >= terrain.matrix.columns:
                d_value = terrain.matrix.get_value(px, py + 1)
                poss_moves.insert(px, py + 1, d_value)
                return poss_moves
            else:
                r_value = terrain.matrix.get_value(px + 1, py)
            if py + 1 >= terrain.matrix.rows:
                r_value = terrain.matrix.get_value(px + 1, py)
                poss_moves.insert(px + 1, py, r_value)
                return poss_moves
            else:
                d_value = terrain.matrix.get_value(px, py + 1)
            if r_value >= d_value:
                poss_moves.insert(px, py + 1, d_value)
            else:
                poss_moves.insert(px + 1, py, r_value)
        else:
            if px - 1 <= 0:
                d_value = terrain.matrix.get_value(px, py + 1)
                poss_moves.insert(px, py + 1, d_value)
                return poss_moves
            else:
                l_value = terrain.matrix.get_value(px - 1, py)
            if py + 1 >= terrain.matrix.rows:
                l_value = terrain.matrix.get_value(px - 1, py)
                poss_moves.insert(px - 1, py, l_value)
                return poss_moves
            else:
                d_value = terrain.matrix.get_value(px, py + 1)
            if l_value >= d_value:
                poss_moves.insert(px, py + 1, d_value)
            else:
                poss_moves.insert(px - 1, py, l_value)
    else:
        if pxo < pxf:
            if px + 1 >= terrain.matrix.columns:
                u_value = terrain.matrix.get_value(px, py - 1)
                poss_moves.insert(px, py - 1, u_value)
                return poss_moves
            else:
                r_value = terrain.matrix.get_value(px + 1, py)
            if py - 1 <= 0:
                r_value = terrain.matrix.get_value(px + 1, py)
                poss_moves.insert(px + 1, py, r_value)
                return poss_moves
            else:
                u_value = terrain.matrix.get_value(px, py - 1)
            if r_value >= u_value:
                poss_moves.insert(px, py - 1, u_value)
            else:
                poss_moves.insert(px + 1, py, r_value)
        else:
            if px - 1 <= 0:
                u_value = terrain.matrix.get_value(px, py - 1)
                poss_moves.insert(px, py - 1, u_value)
                return poss_moves
            else:
                l_value = terrain.matrix.get_value(px - 1, py)
            if py - 1 <= 0:
                l_value = terrain.matrix.get_value(px - 1, py)
                poss_moves.insert(px - 1, py, l_value)
                return poss_moves
            else:
                u_value = terrain.matrix.get_value(px, py - 1)
            if l_value >= u_value:
                poss_moves.insert(px, py - 1, u_value)
            else:
                poss_moves.insert(px - 1, py, l_value)
    return poss_moves


""" The difference between this version of the algorithm
    is that here we insert in the stack also de higher weight
    of the path trying to look for multiple paths because the 
    first version just tries to reach the one the algorithms 
    is programmed to reach by going to the lower weight cell on each iteration"""


def possible_moves_v2(terrain, px, py):
    poss_moves = BasicLinkedList()
    pxo = int(terrain.pxo) - 1
    pyo = int(terrain.pyo) - 1
    pxf = int(terrain.pxf) - 1
    pyf = int(terrain.pyf) - 1
    r_value = l_value = u_value = d_value = 0
    if pyo < pyf:
        if pxo < pxf:
            if px + 1 >= terrain.matrix.columns:
                d_value = terrain.matrix.get_value(px, py + 1)
                poss_moves.insert(px, py + 1, d_value)
                return poss_moves
            else:
                r_value = terrain.matrix.get_value(px + 1, py)
            if py + 1 >= terrain.matrix.rows:
                r_value = terrain.matrix.get_value(px + 1, py)
                poss_moves.insert(px + 1, py, r_value)
                return poss_moves
            else:
                d_value = terrain.matrix.get_value(px, py + 1)
            if r_value >= d_value:
                poss_moves.insert(px + 1, py, r_value)
                poss_moves.insert(px, py + 1, d_value)
            else:
                poss_moves.insert(px, py + 1, d_value)
                poss_moves.insert(px + 1, py, r_value)
        else:
            if px - 1 <= 0:
                d_value = terrain.matrix.get_value(px, py + 1)
                poss_moves.insert(px, py + 1, d_value)
                return poss_moves
            else:
                l_value = terrain.matrix.get_value(px - 1, py)
            if py + 1 >= terrain.matrix.rows:
                l_value = terrain.matrix.get_value(px - 1, py)
                poss_moves.insert(px - 1, py, l_value)
                return poss_moves
            else:
                d_value = terrain.matrix.get_value(px, py + 1)
            if l_value >= d_value:
                poss_moves.insert(px - 1, py, l_value)
                poss_moves.insert(px, py + 1, d_value)
            else:
                poss_moves.insert(px, py + 1, d_value)
                poss_moves.insert(px - 1, py, l_value)
    else:
        if pxo < pxf:
            if px + 1 >= terrain.matrix.columns:
                u_value = terrain.matrix.get_value(px, py - 1)
                poss_moves.insert(px, py - 1, u_value)
                return poss_moves
            else:
                r_value = terrain.matrix.get_value(px + 1, py)
            if py - 1 <= 0:
                r_value = terrain.matrix.get_value(px + 1, py)
                poss_moves.insert(px + 1, py, r_value)
                return poss_moves
            else:
                u_value = terrain.matrix.get_value(px, py - 1)
            if r_value >= u_value:
                poss_moves.insert(px + 1, py, r_value)
                poss_moves.insert(px, py - 1, u_value)
            else:
                poss_moves.insert(px, py - 1, u_value)
                poss_moves.insert(px + 1, py, r_value)
        else:
            if px - 1 <= 0:
                u_value = terrain.matrix.get_value(px, py - 1)
                poss_moves.insert(px, py - 1, u_value)
                return poss_moves
            else:
                l_value = terrain.matrix.get_value(px - 1, py)
            if py - 1 <= 0:
                l_value = terrain.matrix.get_value(px - 1, py)
                poss_moves.insert(px - 1, py, l_value)
                return poss_moves
            else:
                u_value = terrain.matrix.get_value(px, py - 1)
            if l_value >= u_value:
                poss_moves.insert(px - 1, py, l_value)
                poss_moves.insert(px, py - 1, u_value)
            else:
                poss_moves.insert(px, py - 1, u_value)
                poss_moves.insert(px - 1, py, l_value)
    return poss_moves


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
                if terrains.len() == 0:
                    print("No has cargador ningún terreo, por favor carga al menos un terreno")
                else:
                    print("Terrenos previamente cargados:")
                    print("==============================")
                    terrains.get_all_names()
                    print("==============================")
                    name = input("ingresa el nombre del terreno a procesar")
                    terrain = terrains.get(name)
                    process_terrain(terrain)
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
    """st = Stack()
    st.push(0, 0, 1)
    st.push(0, 1, 2)
    st.push(0, 2, 3)
    st.push(0, 3, 2)
    st.push(0, 4, 5)
    st.push(0, 5, 1)
    st.push(1, 5, 4)
    st.show_stack()
    print(f"The length is {st.length()}")
    print(f"The item that was popped is {st.pop().data}")
    print(f"The length is {st.length()}")
    st.show_stack()"""
    display_menu()
