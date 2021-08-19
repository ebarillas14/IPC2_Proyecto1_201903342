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