from cargar_datos import datos
import os

os.system('cls' if os.name == 'nt' else 'clear')
print(datos["dolar_observado_promedio_clp"])
listaArreglados = []

for linea in datos["dolar_observado_promedio_clp"]:
    linea_str = str(linea)
    if len(linea_str) <= 6:
        if int(linea_str[2]) >= 5:
            aux = float(linea+10)
            listaArreglados.append(aux)
        else:
            listaArreglados.append(float(linea))
    elif len(linea_str)>6:
        if int(linea_str[2]) >= 5:
            aux = float(linea+100)
            listaArreglados.append(aux)
        else:
            listaArreglados.append(float(linea))

print(listaArreglados)
print(type(listaArreglados[0]))
for num in listaArreglados:
    pass