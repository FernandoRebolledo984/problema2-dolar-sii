from cargar_datos import datos
import os
#original - aproximacion
os.system('cls' if os.name == 'nt' else 'clear')
listaOriginales = []

for num in datos["dolar_observado_promedio_clp"]:
    listaOriginales.append(float(num))

Arreglados_y_Significativos = [float(f"{num:.2g}") for num in listaOriginales]
i = 0
listaErrores = []

while i < len(datos["dolar_observado_promedio_clp"]):
    listaErrores.append(listaOriginales[i] - Arreglados_y_Significativos[i])
    i = i+1
    pass

print(listaErrores)
