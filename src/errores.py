from punto_flotante import listaErrores as errorAbsoluto, Arreglados_y_Significativos, listaOriginales as valorVerdadero
import os

os.system('cls' if os.name == 'nt' else 'clear')

errorRelativo = []

i = 0
while i < len(Arreglados_y_Significativos):
    errorRelativo.append((errorAbsoluto[i]/valorVerdadero[i])*100)
    i = i+1

#################################################OPERACIONES DE PROPAGACIÓN########################################################################################        

monto = 1_000_000
errorCompra = errorRelativo[0]
errorVenta = errorRelativo[6]

#Compras mes específico
precio_compra = Arreglados_y_Significativos[0]  # Enero 2022
usd_comprados = monto / precio_compra

errorDolar = errorCompra + 0 #0 ya que se suma el error de compra mas el error de monto que es 0

#Vendes mes diferente
precio_venta = Arreglados_y_Significativos[6]   # Julio 2022
pesos_final = usd_comprados * precio_venta

errorPesoFinal = errorDolar + errorVenta

#Ganancia real
ganancia_real = pesos_final - monto

errorAbsolutoPesoFinal = (errorPesoFinal/100)*pesos_final

errorGanancia = errorAbsolutoPesoFinal + 0 #0 otra vez por el error de monto que es 0
print(errorAbsolutoPesoFinal)

print(f"Por lo que las ganancias son: {ganancia_real:.2f} +/- {errorGanancia:.2f}.")


