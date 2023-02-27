accion_uno = "Ya estoy en la entrada del evento"
accion_dos = "Me estoy registrando"

#Estructura de control (condicional o sentencia if o si)
#Permite continua un flujo (realizar algo) si se cumple una condicion
# y en caso de no cumplirse, se puede o no continuar con otro flujo (hacer otra cosa)
# esta sentencia (condicional if) va acompañado de los operadores de comparacion
"""
if estructura_datos_uno < estructura_datos_dos
if estructura_datos_uno <= estructura_datos_dos
if estructura_datos_uno > estructura_datos_dos
if estructura_datos_uno >= estructura_datos_dos
if estructura_datos_uno == estructura_datos_dos
if estructura_datos_uno !=estructura_datos_dos
"""

#Hay varias maneras de utilizar la sentencia if
#if simple, if compuesto, if anidado

#if simple

dato_comparacion = 18
edad = 20
"""
if edad >= dato_comparacion:
    print("Ingresar, disfrutar del evento")
"""

#if compuesto
"""
if edad >= dato_comparacion:
    print("Ingresar, disfrutar del evento")
else:
    print("No ingresar")
"""


boleta = True
fecha_evento = "28-02-2023"
fecha_comparacion = "28-02-2023"
#if anidado
if edad >= dato_comparacion and boleta and fecha_evento == fecha_comparacion:
     print("Ingresar, disfrutar del evento")
else:
    print("No ingresar")


