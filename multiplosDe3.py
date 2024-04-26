"""Escribir un programa que muestre la sumatoria de todos
los múltiplos de 3 encontrados entre el 0 y el 100."""
total=0
for numero in range(101):
    if numero%3 == 0:
        total=total+numero
print("Sumatoria de los múltiplos de 3 encontrados entre el 0 y el 100:", total)