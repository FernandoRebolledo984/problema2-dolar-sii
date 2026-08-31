from cargar_datos import datos

print(datos["dolar_observado_promedio_clp"])

for linea in datos["dolar_observado_promedio_clp"]:

    if len(str(linea)) <= 6:
        auxLine = 0
        if int(linea)[2] >= 5:
            auxLine = linea+10
            print(auxLine)
    else:
        pass