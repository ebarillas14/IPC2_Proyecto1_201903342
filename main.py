from helpers import *


def show_developer_info():
    print("============= DATOS DEL DESARROLLADOR =============")
    print(" Eduardo Abraham Barillas del Aguila")
    print(" Introducción a la Programación y Computación \"C\"")
    print(" Carné: 201903342")
    print("Ingeniería en Ciencias y Sistemas")
    print("4to Semestre")
    print("===================================================")


def display_menu():
    menu_flag = True
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
                pass
            elif validated_option == 2:
                pass
            elif validated_option == 3:
                pass
            elif validated_option == 4:
                show_developer_info()
            else:
                menu_flag = False


if __name__ == '__main__':
    display_menu()
