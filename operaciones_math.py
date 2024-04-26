def suma (a, b):
    return a + b
def resta (a, b):
    return a - b
def multiplicacion (a, b):
    return a * b
def division (a, b):
    return a / b

n1=int(input("Primer número: "))
n2=int(input("Segundo número: "))

print("1. Suma"
      "\n2. Resta"
      "\n3. Multiplicación"
      "\n4. División")
opcion=int(input("Elija el número de la opción: "))

if opcion == 1:
    print(n1, "+", n2, "=", suma(n1, n2))
elif opcion == 1:
    print(n1, "-", n2, "=", resta(n1, n2))
elif opcion == 1:
    print(n1, "*", n2, "=", multiplicacion(n1, n2))
elif opcion == 1:
    print(n1, "/", n2, "=", division(n1, n2))
else:
    print("Error. Ingrese un número válido.")