numeros=[2,4,3,1,6,7,5,8,9,10]
print("Lista original:", numeros)
for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):
        if numeros[i] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i]
print("Lista ordenada:", numeros)
verificacion = sorted(numeros)
if numeros == verificacion:
    print("La lista ha sido ordenada correctamente.")
    