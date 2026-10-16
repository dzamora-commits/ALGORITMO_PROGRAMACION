total_pedido=0
while True:
    print("\n--Menu de Comidas Rapidas--")
    print("1. Hamburguesa:     $15,000" )
    print("2. Perro caliente:  $10,000" )
    print("3. Sandwitch:       $8,000" )
    print("4. salchipapa:      $20,000" )
    print("5. Pizza:           $7,000")
    comida = int(input("Ingrese el numero de la comida que desea: "))
    if comida == 1:
        precio=15000
    elif comida == 2:
        precio=10000
    elif comida == 3:
        precio=8000
    elif comida == 4:
        precio=20000
    elif comida == 5:
        precio=7000
    else:
        print("Esta comida es tan misteriosa que no aparece en el menú.")
        continue
    total_pedido= total_pedido + precio
    print(f"Precio del pedido: ${precio}")
    while True:
        continuar = input("¿Desea agregar otro pedido? (si/no): ").lower()
        if continuar == "no":
            print(f"\nTotal a pagar: ${total_pedido}")
            break
        elif continuar == "si":
            break
        else:
            print("Opción no válida.")
    if continuar == "no":
     break
        