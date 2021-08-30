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


def process_terrain(terrain):
    q = Queue()
    cont = 0
    px = pxo = int(terrain.pxo) - 1
    py = pyo = int(terrain.pyo) - 1
    pxf = int(terrain.pxf)-1
    pyf = int(terrain.pyf) - 1
    data = terrain.matrix.get_value(px, py)
    q.enqueue(px, py, data)

    values_list = BasicLinkedList()

    for x in range(terrain.m):
        for y in range(terrain.n):
            values_list.insert(x, y, 0)

    px = q.peek().px
    py = q.peek().py
    while px != pxf or py != pyf:
        print(f"Calculando la mejor ruta")
        pm = possible_moves(terrain, px, py)
        tmp = pm.First
        q.enqueue(tmp.px, tmp.py, tmp.data)
        cont += 1
        px = q.last().px
        py = q.last().py

    print(f"Calculando la cantidad de combustible")

    # q.show_queue()
    total_fuel = 0
    temp_list = BasicLinkedList()
    while q.length() > 0:
        node = q.dequeue()
        total_fuel += int(node.data)
        values_list.update(node.px, node.py, node.data)
        temp_list.insert(node.px, node.py, node.data)
    result = Node(terrain.pxo, terrain.pyo, terrain.pxf, terrain.pyf, terrain.name, terrain.m, terrain.n, values_list)
    result.update_fuel(total_fuel)
    result.save_positions(temp_list)
    return result


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
            # Verifies if the x position is lower than the matrix total columns
            if px + 1 >= terrain.matrix.columns:
                u_value = terrain.matrix.get_value(px, py - 1)
                poss_moves.insert(px, py - 1, u_value)
                return poss_moves
            # If the value is lower than it, we will move to the right
            else:
                r_value = terrain.matrix.get_value(px + 1, py)
            # Verifies if the y position is lower than 0
            if py - 1 < 0:
                r_value = terrain.matrix.get_value(px + 1, py)
                poss_moves.insert(px + 1, py, r_value)
                return poss_moves
            # If the value is greater than it, we will move up
            else:
                u_value = terrain.matrix.get_value(px, py - 1)
            # Compares to find the lower value to return it
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
    is programmed to reach by going to the lower weight cell on each iteration """


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
    processed_terrains = LinkedList()
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
                    terrain_processed = process_terrain(terrain)
                    terrain_processed.matrix.display_in_menu()
                    print(f"La cantidad total de combustible consumido es: {terrain_processed.total_fuel}")
                    processed_terrains.add(terrain_processed)
            elif validated_option == 3:
                if processed_terrains.len() == 0:
                    print("No has cargador ningún terreo, por favor carga al menos un terreno")
                else:
                    print("Terrenos previamente cargados:")
                    print("==============================")
                    processed_terrains.get_all_names()
                    print("==============================")
                    name = input("ingresa el nombre del terreno a procesar")
                    terrain = processed_terrains.get(name)
                    write_xml(f"{terrain.name}", terrain)
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
