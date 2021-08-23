from TDA import *
from random import randint


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


def create_matrix(row_count, col_count):
    matrix = BasicLinkedList()
    for y in range(row_count):
        row = BasicLinkedList()
        for x in range(col_count):
            value = randint(1, 10)
            row.insert(x, y, value)
        matrix.insert(0, y, row)
    row = matrix.get_value(0, 3)
    data = row.data
    item = data.get_value(3, 3)
    print(item.data)
    return 
