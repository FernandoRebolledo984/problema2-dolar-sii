from punto_flotante import listaErrores as errorAbsoluto, Arreglados_y_Significativos, listaOriginales as valorVerdadero
import os

os.system('cls' if os.name == 'nt' else 'clear')

#Conocemos el porcentaje de error de cada redondeo
i = 0
errorRelativo = []
while i < len(Arreglados_y_Significativos):
    errorRelativo.append((errorAbsoluto[i]/valorVerdadero[i])*100)
    i = i+1

print("\n=== Respuesta A1. Error de representación mes a mes")
print("\n|= Precios =|= Error absoluto =|= Error porcentual =|")
i = 0
while i < len(Arreglados_y_Significativos):
    print(f"|=  {Arreglados_y_Significativos[i]}  =|=      {round(errorAbsoluto[i],2)}      =|=       {round(errorRelativo[i],2)}       =|")
    i+=1

#################################################OPERACIONES DE PROPAGACIÓN#################################################

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
print(f"Los USD comprados en Enero son: {round(usd_comprados,2)}\nLos USD vendidos (en pesos) en Julio son: {round(pesos_final,2)}")

#Ganancia real
ganancia_real = pesos_final - monto

errorAbsolutoPesoFinal = (errorPesoFinal/100)*pesos_final

errorGanancia = errorAbsolutoPesoFinal + 0 #0 otra vez por el error de monto que es 0
porcentajeErrorGanancia = (errorGanancia/ganancia_real)*100

print(f"Por lo que las ganancias son: {ganancia_real:.2f} +/- {round(errorGanancia,2)} (o +/- {porcentajeErrorGanancia:.3g}%).")

##################CANCELACIÓN##################
#Diciembre 2022 - diciembre 2023
dif_Dic1_Dic2 = f"{valorVerdadero[23] - valorVerdadero[11]:.2g}"
propAbs_Dic1_Dic2 = errorAbsoluto[23] + errorAbsoluto[11]
errorPrcntl_Dic1_Dic2 = (propAbs_Dic1_Dic2/float(dif_Dic1_Dic2))*100
print("\n\n=== Respuesta A3. Cancelación ===\n")
print(f"== Diferencia entre ambos meses: {dif_Dic1_Dic2}\n== Error absoluto (+/-): {round(propAbs_Dic1_Dic2,2)} ")
print("== Debido a que la diferencia verdadera entre ambos meses es menor al error absoluto se puede concluir que no se puede afirmar\n" \
"subió o bajó.")
