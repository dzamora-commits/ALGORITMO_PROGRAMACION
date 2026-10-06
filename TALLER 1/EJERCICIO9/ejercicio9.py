dia=input("ingrese el dia de la semana:"). lower()
if dia=="sabado" or dia=="domingo":
    print("Se produjo un error.")
fechaDia,fechaMes=map(int,input("Ingrese la fecha en formato dd/mm:").split("/"))
if int(fechaDia)>31 or int(fechaMes)>12:
    print("Se produjo un error.")
if dia=="lunes":
    print("Nivel Inicial.")
    examen=input("Se realizó un examen? (si/no):").lower()
    if examen=="si":
        aprobados=int(input("Ingrese la cantidad de alumnos aprobados:"))
        reprobados=int(input("Ingrese la cantidad de alumnos reprobados:"))
        total=aprobados+reprobados
        porcentajeAprobados=(aprobados/total)*100
        print("El porcentaje de alumnos aprobados es:", porcentajeAprobados,"%")
    else:
        print(f"Lunes {fechaDia}/{fechaMes} no se realizó examen.")
elif dia=="martes":
    print("Nivel intermedio.")
    examen=input("Se realizó un examen? (si/no):").lower()
    if examen=="si":
        aprobados=int(input("Ingrese la cantidad de alumnos aprobados:"))
        reprobados=int(input("Ingrese la cantidad de alumnos reprobados:"))
        total = aprobados+reprobados
        porcentajeAprobados=(aprobados/total)*100
        print("El porcentaje de alumnos aprobados es:", porcentajeAprobados,"%")
    else:
        print(f"Martes {fechaDia}/{fechaMes} no se realizó examen.")
elif dia=="miercoles":
    print("Nivel avanzado.")
    examen=input("Se realizó un examen? (si/no):").lower()
    if examen=="si":
        aprobados=int(input("Ingrese la cantidad de alumnos aprobados:"))
        reprobados=int(input("Ingrese la cantidad de alumnos reprobados:"))
        total = aprobados+reprobados
        porcentajeAprobados=(aprobados/total)*100
        print("El porcentaje de alumnos aprobados es:", porcentajeAprobados,"%")
    else:
        print(f"Miercoles {fechaDia}/{fechaMes} no se realizó examen.")
elif dia=="jueves":
    print("Practica Hablada")
    asistencia=float(input("Ingrese el porcentaje de asistencia:"))
    if asistencia>50:
        print("asistio la mayoria de los alumnos.")
    else:
        print("No asistio la mayoria de los alumnos.")
elif dia=="viernes":
    print("Ingles para viajeros.")
    if fechaDia==1 and (fechaMes==1 or fechaMes==7):
        print("Comienza el nuevo ciclo")
        alumnos=int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel=float(input("Ingrese el arancel por alumno: "))
        ingresos=alumnos*arancel
        print("Los ingresos totales del nuevo ciclo son:", ingresos)
    else:
        print(f"Viernes {fechaDia}/{fechaMes} no comienza un nuevo ciclo.")
