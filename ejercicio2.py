nombres = []
apellidos = []

for i in range(3):
    nombre = input(f"Ingrese nombre: {i+1}:")
    apellido = input(f"Ingrese apellido {i+1}:")
    nombres.append(nombre)
    apellidos.append(apellido)

nombres.sort()
apellidos.sort()
nombre = nombres.reverse()
num = [2,4,1]
print(num.reverse())

print("Nombres ordenados: ", nombres)
print("Apellidos ordenados: ", apellidos)
print("Nombre al revés: ")

