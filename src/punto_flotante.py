from cargar_datos import datos
import numpy as np
import os
os.system('cls' if os.name == 'nt' else 'clear')

listaOriginales = []
for num in datos["dolar_observado_promedio_clp"]:
    listaOriginales.append(float(num))

#Redondeamos y truncamos los numeros a 2 cifras significativas
Arreglados_y_Significativos = [float(f"{num:.2g}") for num in listaOriginales]

#Error de redondeo por cada mes
i = 0
listaErrores = []
while i < len(datos["dolar_observado_promedio_clp"]):
    listaErrores.append(abs(listaOriginales[i] - Arreglados_y_Significativos[i]))
    i = i+1

print("\n=== Respuesta B2. La ida y vuelta ===\n")
monto = 1_000_000
deriva_ida_vuelta = []

print("Ejemplos de meses que la pérdida o ganancia es mínima:")
i=0
while i < len(listaOriginales):
    precio = listaOriginales[i]
    usd_comprado = monto/precio             #Compra de usd
    usd_vendido = usd_comprado * precio     #Venta de usd
    #Diferencia entre lo que pusimos y el resultado de la máquina
    diferencia = usd_vendido - monto
    deriva_ida_vuelta.append(diferencia)
    #Mostramos posibles perdidas o ganancias no notorias 
    if diferencia != 0.0 and i < 12:
        print(f" - Mes {i+1}: Precio {precio}\n - CLP devuelto: {usd_vendido}\n - Pérdida o ganancia fantasma: {diferencia}")
    i += 1
print(f"\nConclusión: Matemáticamente se puede decir que '(M / P) * P = M', pero al llevar esto a computadora no siempre llega a ser así, debido\na que al multiplicar o dividir se pierden bits del número binario, provocando que no siempre se obtenga el monto inicial.\n")

print("=== Respuesta B4. Cancelación de la máquina ===")
num1 = 874.67
num2 = 875.66
resta = num1 - num2

#float32
num1_32 = np.float32(num1)
num2_32 = np.float32(num2)
resta_32 = num1_32 - num2_32

#float64
num1_64 = np.float64(num1)
num2_64 = np.float64(num2)
resta_64 = num1_64 - num2_64

print(f" - Resultado sin especificar bits (nativo de python): {resta}")
print(f" - Resultado en 32 bits: {resta_32}")
print(f" - Resultado en 64 btis: {resta_64}")