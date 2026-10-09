total = 0
while True:
    print("\n--Menu de Helados--")
    print("1. Sin topping:  $1.90")
    print("2. Frutas:       $0.50")
    print("3. Granola:      $1.50")
    print("4. Oreo:         $1.00")
    print("5. Brownie:      $0.75")
    topping = int(input("Ingrese el numero del topping que desea: "))
    if topping == 1:
        precio=1.90
    elif topping == 2:
        precio=0.50+1.90
    elif topping == 3:
        precio=1.50+1.90
    elif topping == 4:
        precio=1.00+1.90
    elif topping == 5:
        precio=0.75+1.90
    else:
        print("Ese sabor es tan misterioso que no aparece en el menú.")
        print("Por favor, seleccione un topping válido.")
        continue
    total= total + precio
    print(f"Precio del pedido: ${precio:.2f}")
    while True:
        continuar = input("¿Desea agregar otro pedido? (si/no): ").lower()
        if continuar == "no":
            break
        elif continuar == "si":
            break
        else:
            print("Opción no válida.")
    if continuar == "no":
        break
print (f"\nTotal a pagar: ${total:.2f}")