from punto_flotante import listaErrores as errorAbsoluto, Arreglados_y_Significativos, listaOriginales as valorVerdadero
import os

os.system('cls' if os.name == 'nt' else 'clear')

#Conocemos el porcentaje de error de cada redondeo
i = 0
errorRelativo = []
while i < len(Arreglados_y_Significativos):
    errorRelativo.append((errorAbsoluto[i]/valorVerdadero[i])*100)
    i = i+1

#################################################OPERACIONES DE PROPAGACIÓN########################################################################################        

monto = 1_000_000
errorCompra = errorRelativo[0] #Contiene el error relativo del primer mes
errorVenta = errorRelativo[6] #Lo mismo pero del mes 7

#Compras mes específico
precio_compra = Arreglados_y_Significativos[0]  # Enero 2022
usd_comprados = monto / precio_compra

errorDolar = errorCompra + 0 #0 ya que se suma el error de compra mas el error de monto que es 0

#Vendes mes diferente
precio_venta = Arreglados_y_Significativos[6]   # Julio 2022
pesos_final = usd_comprados * precio_venta

errorPesoFinal = errorDolar + errorVenta #Suma de errores relativos de ambos meses

#Ganancia real
ganancia_real = pesos_final - monto

errorAbsolutoPesoFinal = (errorPesoFinal/100)*pesos_final

errorGanancia = errorAbsolutoPesoFinal + 0 #0 otra vez por el error de monto que es 0
porcentajeErrorGanancia = (errorGanancia/ganancia_real)*100

print(errorAbsolutoPesoFinal)
print(f"Por lo que las ganancias son: {ganancia_real:.2f} +/- {errorGanancia:.2f} (o +/- {porcentajeErrorGanancia:.3g}%)")

##################CANCELACIÓN########################


