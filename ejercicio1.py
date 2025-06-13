#almacenar tres nombres solicitados por pantalla en una lista

nombre_1 = input("Ingrese el primer nombre: ")
nombre_2 = input("Ingrese el segundo nombre: ")
nombre_3 = input("Ingrese el tercer nombre: ")

lista_nombres = [nombre_1, nombre_2, nombre_3]

nombre_mayor = ""
longitud_maxima = 0

for nombre in lista_nombres:
    longitud_actual = len(nombre)

if longitud_actual > longitud_maxima:
    longitud_maxima = longitud_actual
    nombre_mayor = nombre

print (f"El nombre más largo es: {nombre_mayor}")


