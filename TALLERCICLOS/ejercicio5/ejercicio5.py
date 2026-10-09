import random
x=0
y=0
for i in range(100):
    direccion=random. choice(["Arriba","Abajo","Izquierda","Derecha"])
    if direccion=="Arriba":
        y+=1
    elif direccion=="Abajo":
        y-=1
    elif direccion=="Izquierda":
        x-=1
    elif direccion=="Derecha":
        x+=1
print("ubicacion inicial:",(0,0))
print("ubicacion final:",(x,y))