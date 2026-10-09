palabra=input("Ingrese una palabra: ")
for letra in range(len(palabra)+1):
  for inicio in range(len (palabra)-letra+1):
    subcadena=palabra[inicio:inicio+letra]
    print(subcadena)    