"""Programa que tome las 3 notas de un estudiante y diga la nota final del curso.
La 1era y 2da nota valen el 30% y la 3era el 40%"""
def calcularNota(n1, n2, n3):
    return (n1*0.3) + (n2*0.3) + (n3*0.4)

n1=float(input("Nota 1: "))
n2=float(input("Nota 2: "))
n3=float(input("Nota 3: "))
print("La nota final del estudiante es", round(calcularNota(n1, n2, n3),2))
