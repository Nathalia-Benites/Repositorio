"""Crear una función para sumar los valores recibidos de tipo numérico, utilizando argumentos variables *args
como parámetro de la función y regresar como resultado la suma de todos los valores pasados como argumentos.
"""
def listar(*numeros):
    resultado = 0
    for valor in numeros:
        #resultado = resultado + valor
        resultado += valor
    return resultado

resultado = listar(12, 1004, 23, 46)
print(resultado)

# += es que va incrementando y asignando