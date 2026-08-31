from cargar_datos import datos
import os

os.system('cls' if os.name == 'nt' else 'clear')
print(datos["dolar_observado_promedio_clp"])


Arreglados_y_Significativos = [[float(f"{num:.2g}") for num in datos["dolar_observado_promedio_clp"]]]
print(Arreglados_y_Significativos)