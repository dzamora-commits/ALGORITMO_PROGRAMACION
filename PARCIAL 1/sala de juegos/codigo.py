precio=0
while True:
    edad= int(input("Ingrese la edad del cliente: "))
    if edad < 5:
     print("La entrada es gratis")
     precio += 0
    elif edad >= 5 and edad <= 18:
     print("El precio de la entrada es de $5")
     precio += 5
    else:         
     print ("El precio de la entrada es de $10")
     precio += 10
    while True:
        respuesta= input("¿Desea ingresar otra edad? (si/no): ").lower()
        if respuesta == "si":
            break
        elif respuesta == "no":
            print(f"El precio total de las entradas es de ${precio}")
            print("Gracias por su visita.")
            break
        else:
            print("Opción no válida. Por favor, responda con 'si' o 'no'.") 
    if respuesta == "no":
     break