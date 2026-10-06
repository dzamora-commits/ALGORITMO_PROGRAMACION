numero=int(input("Ingrese un numero entre 10 y 50:"))
if numero ==30:
    print("GANASTE UN PREMIO!!")
elif numero < 10 or numero > 50:
    print("El numero ingresado no esta en el rango de 10 y 50")
else:
    print("PERDISTE")