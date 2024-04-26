from colorama import Fore, Back, Style, init
init()

dato = input("\033[1mIngresa un dato: \033[0m")
if dato.isdigit():
    print("Es un número.")
elif dato.isalpha():
    print("Es alfabético.")
    if dato.isupper():
        print("Está en mayúsculas.")
    elif dato.islower():
        print(Back.CYAN + "Está en minúsculas."+ Style.RESET_ALL)
elif dato.replace(".", "", 1).isdigit():
    print("Es un número decimal.")
elif dato.isspace():
    print("Es un espacio.")
elif all(char.isascii() and not char.isalnum() for char in dato):
    print("Es un código ASCII de caracteres especiales.")
else:
    print("Es una cadena de caracteres.")

