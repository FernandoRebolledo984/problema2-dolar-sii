from punto_flotante import listaErrores as errorAbsoluto, Arreglados_y_Significativos, listaOriginales as valorVerdadero
from cargar_datos import datos
from pathlib import Path
import os
import csv
import matplotlib.pyplot as plt
from punto_flotante import deriva_ida_vuelta

os.system('cls' if os.name == 'nt' else 'clear')

#Conocemos el porcentaje de error de cada redondeo
i = 0
errorRelativo = []
while i < len(Arreglados_y_Significativos):
    errorRelativo.append((errorAbsoluto[i]/valorVerdadero[i])*100)
    i = i+1

#Búsqueda del mes con el mayor error relativo
max_relativo = max(errorRelativo)

print("\n=== Respuesta A1. Error de representación mes a mes ===")
print("\n|= Precios =|= Error absoluto =|= Error porcentual =|")
i = 0
while i < len(Arreglados_y_Significativos):
    print(f"|=  {Arreglados_y_Significativos[i]}  =|=      {round(errorAbsoluto[i],3)}      =|=       {round(errorRelativo[i],3)}      =|")
    i+=1
print(f"\nSiendo el mes de Abril aquel con el mayor error relativo ({round(max_relativo,3)}%).")

################## OPERACIONES DE PROPAGACIÓN ##################

monto = 1_000_000
errorCompra = errorRelativo[0] #Contiene el error relativo del primer mes
errorVenta = errorRelativo[6] #Lo mismo pero del mes 7

print("\n\n=== Respuesta A2. Evaluación entre dos puntos ===\n\nSe escogió el mes de enero y julio, ambos de 2022")
#Compras mes específico
precio_compra = Arreglados_y_Significativos[0]  # Enero 2022
usd_comprados = monto / precio_compra

errorDolar = errorCompra + 0 #0 ya que se suma el error de compra mas el error de monto que es 0

#Vendes mes diferente
precio_venta = Arreglados_y_Significativos[6]   # Julio 2022
pesos_final = usd_comprados * precio_venta

errorPesoFinal = errorDolar + errorVenta #Suma de errores relativos de ambos meses
print(f" - Los USD comprados en Enero son: {round(usd_comprados,3)}\n - Los USD vendidos (en pesos) en Julio son: {round(pesos_final,3)}")

#Ganancia real
ganancia_real = pesos_final - monto

errorAbsolutoPesoFinal = (errorPesoFinal/100)*pesos_final

errorGanancia = errorAbsolutoPesoFinal + 0 #0 otra vez por el error de monto que es 0
porcentajeErrorGanancia = (errorGanancia/ganancia_real)*100

print(f" - Por lo que las ganancias son: {ganancia_real:.2f} +/- {round(errorGanancia,3)} (o +/- {porcentajeErrorGanancia:.3g}%).")

################## CANCELACIÓN ##################
#Diciembre 2022 - diciembre 2023
dif_Dic1_Dic2 = f"{valorVerdadero[23] - valorVerdadero[11]:.3g}"
dif_Dic1_Dic2_fix = float(dif_Dic1_Dic2)
propAbs_Dic1_Dic2 = errorAbsoluto[23] + errorAbsoluto[11]
errorPrcntl_Dic1_Dic2 = (propAbs_Dic1_Dic2/float(dif_Dic1_Dic2))*100
print("\n\n=== Respuesta A3. Cancelación ===\n")
print(f" - Diferencia entre ambos meses: {abs(dif_Dic1_Dic2_fix)}\n - Error absoluto (+/-): {round(propAbs_Dic1_Dic2,3)} ")
print(" - Debido a que la diferencia verdadera entre ambos meses es menor al error absoluto se puede concluir que no se puede afirmar si subió o bajó.\n")

################## EXPORTACIÓN DE TABLA DE ERRORES ##################

ruta_data = Path(__file__).resolve().parent.parent / "data"     #Buscamos la carpeta "data"
ruta_salida = ruta_data / "tabla_errores.csv"                   #Ruta del archivo a crear

#Abrimos el archivo en modo escritura
with open(ruta_salida, mode='w', newline='', encoding='utf-8') as archivo_csv:
    escritor = csv.writer(archivo_csv, delimiter=',')
    
    escritor.writerow(["Mes", "Año", "Precio_aprox", "Error_absoluto", "Error_relativo_porcentual"])
    
    m = 0
    while m < len(Arreglados_y_Significativos):
        #Accedemos al mes y año desde la lista original de datos (datos)
        mes = datos[m][1]
        anio = datos[m][0]
        precio = Arreglados_y_Significativos[m]
        err_abs = round(errorAbsoluto[m], 5)
        err_rel = round(errorRelativo[m], 5)
        
        escritor.writerow([mes, anio, precio, err_abs, err_rel])
        m += 1

print(f"Tabla de errores creada y guardada en 'data'.\n")

################## CREACIÓN DE GRÁFICOS ##################

ruta_graficos = Path(__file__).resolve().parent.parent / "graficos"

#Eje X (Mes Año)
etiquetas = []
i = 0
while i < len(datos):
    etiquetas.append(f"{datos[i][1][:3]} {datos[i][0]}")
    i += 1

#Gráfica 1: Serie mensual
plt.figure(figsize=(10, 5))
plt.plot(etiquetas, valorVerdadero, label='Original')
plt.plot(etiquetas, Arreglados_y_Significativos, label='Aproximado')
plt.title('Serie mensual del dólar observado')
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.savefig(ruta_graficos / "serie_mensual_1.png")
plt.close()

#Lógica para la gráfica 2
variaciones = []
errores_propagados_resta = []
etiquetas_g2 = []
k=1
while k < len(Arreglados_y_Significativos):
    variacion = Arreglados_y_Significativos[k] - Arreglados_y_Significativos[k-1]
    err_prop = errorAbsoluto[k] + errorAbsoluto[k-1] 
    variaciones.append(variacion)
    errores_propagados_resta.append(err_prop)
    etiquetas_g2.append(f"{datos[k][1][:3]} - {datos[k-1][1][:3]}")
    k+=1

#Gráfica 2: Variación mes a mes
plt.figure(figsize=(10, 5))
plt.bar(etiquetas_g2, variaciones, label='Variación (\u0394P)', alpha=0.7)
plt.bar(etiquetas_g2, errores_propagados_resta, label='Error propagado', color='red', alpha=0.5)
plt.title('Variación mes a mes y error (Cancelación)')
plt.xticks(rotation=90, fontsize=8)
plt.legend()
plt.tight_layout()
plt.savefig(ruta_graficos / "variacion_cancelacion_2.png")
plt.close()

#Gráfica 3: Error de representación
plt.figure(figsize=(10, 5))
plt.bar(etiquetas, errorAbsoluto, color='orange')
plt.title('Error de representación mensual absoluto')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(ruta_graficos / "error_representacion_3.png")
plt.close()

#Lógica para la gráfica 4
precio_minimo = min(Arreglados_y_Significativos)
idx_min = Arreglados_y_Significativos.index(precio_minimo)
rentabilidades = []
errores_rentabilidad = []
etiquetas_g4 = []
j = idx_min + 1
while j < len(Arreglados_y_Significativos):
    usd = monto / precio_minimo
    pesos_final = usd * Arreglados_y_Significativos[j]
    ganancia = pesos_final - monto
    rent = (ganancia / monto) * 100
    
    err_rel_mult = errorRelativo[idx_min] + errorRelativo[j]
    err_abs_pesos = (err_rel_mult / 100) * pesos_final
    err_rent = (err_abs_pesos / monto) * 100
    
    rentabilidades.append(rent)
    errores_rentabilidad.append(err_rent)
    etiquetas_g4.append(etiquetas[j])
    j += 1

#Gráfica 4: Rentabilidad
plt.figure(figsize=(10, 5))
plt.bar(etiquetas_g4, rentabilidades, yerr=errores_rentabilidad, color='skyblue', edgecolor='black', ecolor='red', capsize=4)
plt.axhline(0, color='black', linewidth=1)
plt.title('Rentabilidad (%) comprando en el mínimo histórico')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(ruta_graficos / "rentabilidad_minimo_4.png")
plt.close()

#Gráfica 5: Deriva
plt.figure(figsize=(10, 5))
plt.plot(etiquetas, deriva_ida_vuelta, color='purple')
plt.axhline(0, color='black', linewidth=1)
plt.title('Deriva del ciclo ida y vuelta')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(ruta_graficos / "deriva_ida_vuelta_5.png")
plt.close()

print("Gráficos creados y generados en la carpeta 'gráficos'\n")