'''
-----------------------------
 RETO N°1
 Años bisiestos
-----------------------------
Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False si no lo es. Se incluye una lista de datos y resultados de prueba. 
-----------------------------
'''
def esAñoBisiesto(año):

  # coloca tu código aquí

testDatos = [1900, 2000, 2016, 1987]
testResultados = [False, True, True, False]
for i in range(len(testDatos)):
	an = testDatos[i]
	print(an,"->",end="")
	resultado = esAñoBisiesto(an)
	if resultado == testResultados[i]:
		print("OK")
	else:
		print("Error")

'''
-----------------------------
Ahora, haremos que tome dos argumentos (un año y un mes) y devuelva el número de días del mes/año dado (siendo febrero diferente en un año bisiesto). Intenta hacer que la función devuelva None si los argumentos no tienen sentido.
-----------------------------
'''
def esAñoBisiesto(año):
  # tu código del laboratorio anterior

def diasEnMes(año, mes):
  # coloca tu código aquí

testAños = [1900, 2000, 2016, 1987]
testMeses = [2, 2, 1, 11]
testResultados = [28, 29, 31, 30]
for i in range(len(testAños)):
	an = testAños[i]
	me = testMeses[i]
	print(an, me, "->", end="")
	resultado = diasEnMes(an, me)
	if resultado == testResultados[i]:
		print("OK")
	else:
		print("Error")
