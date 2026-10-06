numero1=float(input("Ingrese el primer numero: "))
numero2=float(input("Ingrese el segundo numero: "))
if numero1 > numero2:
    print("EL numero", numero1, "es mayor que", numero2)
elif numero2 > numero1:
    print("EL numero", numero2, "es mayor que", numero1)
else:
    print("Los numeros son iguales")