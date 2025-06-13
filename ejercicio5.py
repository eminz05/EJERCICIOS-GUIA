
productos = {
    "Agua" : 600,
    "Azúcar" : 1200,
    "Aceite" : 1500,
    "Arroz" : 1250,
    "Fideos" : 799
}
canasta = []

while True:
    print("1. Agregar productos")
    print("2. Ver canasta")
    print("3. Ver total")
    print("4. Salir")
    try:
        opcion = int(input("Ingrese una opción: "))
        if opcion > 4 or opcion < 1:
             print("Opción inválida. Por favor, intente de nuevo")
        else:
            break
    except ValueError:
        print("Opción inválida")

    if opcion == 4:
        print("Saliendo...")
        break
    elif opcion == 1:
        print("----Seleccione un producto para agregar----")
        print("1. Agua → $ 600")
        print("2.Azúcar→ $1200")
        print("3.Aceite → $1500")
        print("4.Arroz → $1250")
        print("5.Fideos → $ 790")
        while True:
            seleccion_producto = input("Agregue un producto a la canasta: ")
            canasta.append(seleccion_producto)
            for producto in canasta:
                


            #ayudaaaaaaaaaaaaaaa