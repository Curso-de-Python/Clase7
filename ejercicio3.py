'''
-----------------------------
 EJERCICIO N°3
 La instrucción return
-----------------------------
 1° variante: SOLO RETURN
-----------------------------
'''
def felizAñoNuevo(deseos = True):
  print("Tres ...")
  print("Dos ...")
  print("Uno ...")
  if not deseos:
    return
    
  print("¡Feliz año nuevo!") 

felizAñoNuevo() #Invocación
#felizAñoNuevo(False)

'''
-----------------------------
 2° variante: RETURN + EXPRESIÓN
-----------------------------
def funcion_aburrida():
  return 123

x = funcion_aburrida()

print("La funcion_aburrida ha devuelto su resultado. Es: ", x)
'''
