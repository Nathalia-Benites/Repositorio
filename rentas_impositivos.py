"""Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
Menos de $10000: 5%
Entre $10000 y $20000: 15%
Entre $20000 y $35000: 20%
Entre $35000 y $60000: 30%
Más de $60000: 45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo
que le corresponde."""
while True:
    continuar = input("\nDesea ingresar usuario (si/no): ")
    if continuar != "si":
        break

    print("\n\t\t\t\33[1mTramos impositivos de la declaración de la renta\33[0m")
    print ("\n\t\33[3mDatos del usuario\33[0m")
    nom = input("\nNombre: ")
    renta_anual= float(input("Renta anual: "))
    if renta_anual < 10000:
        tipo = 5
        print("\n\t\tSu tipo de impositivo es %", tipo, "\n\t\tDebe pagar $", renta_anual*tipo)
    elif renta_anual >= 10000 and renta_anual < 20000:
        tipo = 15
        print("\n\t\tSu tipo de impositivo es %", tipo, "\n\t\tDebe pagar $", renta_anual*tipo)
    elif renta_anual >= 20000 and renta_anual < 35000:
        tipo = 20
        print("\n\t\tSu tipo de impositivo es %", tipo, "\n\t\tDebe pagar $", renta_anual*tipo)
    elif renta_anual >= 35000 and renta_anual < 60000:
        tipo = 30
        print("\n\t\tSu tipo de impositivo es %", tipo, "\n\t\tDebe pagar $", renta_anual*tipo)
    else:
        tipo = 45
        print("\n\t\tSu tipo de impositivo es %", tipo, "\n\t\tDebe pagar $", renta_anual * tipo)