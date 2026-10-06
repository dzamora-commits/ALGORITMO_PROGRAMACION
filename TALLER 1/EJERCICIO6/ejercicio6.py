letra=input("Ingrese una letra: "). lower()
if len(letra)>1 or len(letra)==0:
    print("NO se puede procesar el dato .")
elif letra== "a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
    print("La letra ingresada es una vocal.")
else:
    print("La letra ingresada no es una vocal.")