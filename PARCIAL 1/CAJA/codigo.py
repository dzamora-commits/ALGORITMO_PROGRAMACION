import random
caja=[]

while True:
    sensor=random.randint(1,200)
    if sensor<=199:
        print("El sensor detecto una bolsa")
        print("llenando la bolsa de arroz ...")
        print("bolsa de arroz llena")
        caja.append("bolsa de arroz")
        print("bolsa empacada en la caja")
        print("bolsa numero:", len (caja))
        print("-------------------------------------------")
    else:
        print("El sensor ya no detecto ninguna bolsa")
        break
print("Total de bolsas empacadas:", len(caja))

