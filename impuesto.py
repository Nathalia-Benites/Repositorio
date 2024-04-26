"""Calculadora de Impuestos
Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
"""
#Nombre: Nathalia Benites
def calcular(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

print("\t\t\tCalculadora de Impuestos\n")
pago_sin_impuesto = float(input("Pago sin impuesto: "))
impuesto = float(input("Impuesto aplicado: "))

pago_total = calcular(pago_sin_impuesto, impuesto)
valor_impuesto=pago_total - pago_sin_impuesto

print("El impuesto a pagar es: ", "{:.2f}".format(valor_impuesto))
print("Total a pagar con impuesto:", "{:.2f}".format(pago_total))