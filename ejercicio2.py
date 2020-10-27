'''
-----------------------------
 EJERCICIO N°2
 Funciones con parámetros
-----------------------------
 ARGUMENTOS POSICIONALES
-----------------------------
'''
def presentar(primerNombre, segundoNombre):
  print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar("Luke", "Skywalker")
presentar("Jesse", "Quick")
presentar("Clark", "Kent")

'''
-----------------------------
 ARGUMENTOS CON PALABRAS CLAVE
-----------------------------
def presentar (primerNombre, segundoNombre):
  print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar(primerNombre = "James", segundoNombre = "Bond")
presentar(segundoNombre = "Skywalker", primerNombre = "Luke")

-----------------------------
 PARÁMETROS PREDEFINIDOS
-----------------------------
def presentar(primerNombre, segundoNombre="González"):
  print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar("María", "Pérez")  # Args posicionales
presentar("Enrique")

presentar (primerNombre="Guillermo")  # Arg con palabra clave

'''
