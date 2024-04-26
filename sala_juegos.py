"""Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular
de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario
la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si
tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, $10."""
while True:
    opcion = input("Desea ingresar usuario (si=1 no=2): ")
    if opcion != '1':
        break
    print("\t\t\t\033[94mSala de juegos 'Happy Kids'\033[0m")
    print("\t\t\n\033[3m - Datos del cliente\033[0m")

    nom = input("\nNombre: ")
    try:
        edad = int(input("Edad: "))
    except ValueError:
        print("Por favor, ingrese una edad válida.")
        continue

    if edad < 4:
        print("\n\t\t\t\033[4mNo paga entrada\033[0m")
    elif 4 <= edad < 18:
        print("\n\t\t\t\033[4mValor de la entrada: $5\033[0m")
    else:
        print("\n\t\t\t\033[4mValor de la entrada: $10\033[0m")