from TDA import *
from random import randint
import xml.etree.ElementTree as ET


def validate_number(value, minvalue, maxvalue):
    is_valid = True
    while is_valid:
        try:
            option = int(value)
            if option < minvalue or option > maxvalue:
                value = int(input("Ingresa un número de opción valido: "))
            else:
                return option
        except:
            is_valid = False
            print("Ingresa un número")


def load_xml(route):
    terrains = LinkedList()
    tree = ET.parse(route)
    root = tree.getroot()
    for terrain in root.findall('terreno'):
        name = terrain.get('nombre')
        ipx = ipy = fpx = fpy = m = n = 0
        ip = terrain.find('posicioninicio')
        fp = terrain.find('posicionfin')
        t_dim = terrain.find('dimension')
        t_values = BasicLinkedList()
        # print(f"Nombre del Terreno: {name}")
        for p in ip:
            if p.tag == "y":
                ipy = p.text
            elif p.tag == "x":
                ipx = p.text
            # print(f"Posicion inicial :en {p.tag} es {p.text}")
        for p in fp:
            if p.tag == "y":
                fpy = p.text
            elif p.tag == "x":
                fpx = p.text
            # print(f"Posicion final :en {p.tag} es {p.text}")
        for dim in t_dim:
            if dim.tag == "m":
                m = dim.text
            elif dim.tag == "n":
                n = dim.text
            # print(f"el tamaño para {dim.tag} es {dim.text}")
        for pos in terrain.findall('posicion'):
            px = pos.get('x')
            py = pos.get('y')
            pv = pos.text
            t_values.insert(int(px)-1, int(py)-1, int(pv))
            # print(f"en la posicion x({px}) y({py}) el peso de la casilla es {pv}")
        # if (int(m)*int(n)) < t_values.len():
        #    print("ERROR: hay menos posiciones de las necesarias para llenar el terreno")
        if name is None or name == " ":
            print("ERROR: el terreno no contiene un nombre")
        if ipx is None or ipy is None:
            print("ERROR: el terreno no tiene indicada una posicion inicial")
        if fpx is None or fpy is None:
            print("ERROR: el terreno no tiene indicada una posicion final")
        terrains.insert(ipx, ipy, fpx, fpy, name, m, n, t_values)
        print(f"Hay {terrains.len()} terrenos en la lista")
    return terrains
