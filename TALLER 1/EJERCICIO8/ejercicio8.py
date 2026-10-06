print("""Candidatos disponibles:  
candidato A - partido rojo  
candidato B - partido verde   
candidato C - partido azul""") 
voto=input("Ingrese su voto ( A, B o C): ").upper()
if voto=="A":
    print("Usted ha votado por el candidato A del partido rojo.")
elif voto=="B":
    print("Usted ha votado por el candidato B del partido verde.")
elif voto=="C":
    print("Usted ha votado por el candidato C del partido azul.")
else:
    print("Opcion erronea")