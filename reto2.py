'''
-----------------------------
 RETO N°2
 Números primos
-----------------------------
Un número natural es primo si es mayor que 1 y no tiene  divisores más que 1 y si mismo. Tu tarea es escribir una función que verifique si un número es primo o no.

La función:
 - Se llama esPrimo
 - Toma un argumento (el valor a verificar)
 - Devuelve True si el argumento es un número primo, y False de lo contrario
-----------------------------
'''
def esPrimo(num):
  # coloca tu código aquí

for i in range(1, 20):
  if esPrimo(i + 1):
    print(i + 1, end=" ")
print()
