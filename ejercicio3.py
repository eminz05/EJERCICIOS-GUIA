nombres = []
resp = "si"
while resp == "si":
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre) #hay un error aqui :(

    while True:
        resp = input("¿Desea ingresar otro? (si/no): ").lower()
        if resp == "si" or resp == "no":
            break
        else:
            print("Por favor debe escribir 'si' o 'no'")

    menor = nombres[0]

    for nombre in nombres:
        if len(nombre) < len(menor):
            menor = nombre

    print(nombres)

    nombres.remove.lower()
