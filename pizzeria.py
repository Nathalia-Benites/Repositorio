"""La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.
Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le
muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la
mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
vegetariana o no y todos los ingredientes que lleva."""
while True:
    continuar = input("\nDesea ingresar usuario (si/no): ")
    if continuar != "si":
        break
    print("\n\t\t\t\033[94mPizzería 'Bella Napoli'\033[0m")
    print("\n\t\033[1mIngredientes adicionales a la mozzarella y tomate\033[0m")
    print("\n\t\t\033[3mVegetarianos\033[0m"
          "\nOpción 1: Pimiento"
          "\nOpción 2: tofu. ")
    print("\n\t\t\033[3mNo vegetarianos\033[0m"
          "\nOpción 3: Peperoni"
          "\nOpción 4: Jamón"
          "\nOpción 5: Salmón")
    print("\t\t\n\033[3m - Datos del cliente\033[0m")
    nom = input("\nNombre: ")
    ci = input("Cédula: ")
    telf = input("Teléfono: ")
    direc = input("Dirección: ")
    tipo = int(input("Escoger el número de la opción del ingrediente: "))
    if tipo == 1 or tipo == 2:
        print("\n\t\tLa pizza elegida es vegetariana")
        if tipo == 1:
            print("\n\t\tLos ingredientes de la pizza son mozzarella, tomate y pimiento")
        elif tipo == 2:
            print("\n\t\tLos ingredientes de la pizza son mozzarella, tomate y tofu")
    elif tipo == 3 or tipo == 4 or tipo == 5:
        print("\n\t\tLa pizza elegida no es vegetariana")
        if tipo == 3:
            print("\n\t\tLos ingredientes de la pizza son mozzarella, tomate y peperoni")
        elif tipo == 4:
            print("\n\t\tLos ingredientes de la pizza son mozzarella, tomate y jamón")
        elif tipo == 5:
            print("\n\t\tLos ingredientes de la pizza son mozzarella, tomate y salmón")




