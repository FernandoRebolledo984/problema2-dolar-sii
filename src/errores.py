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

# 1. Compras en un mes específico
precio_compra = Arreglados_y_Significativos[0]  # Enero 2022
usd_comprados = monto / precio_compra

# 2. Vendes en un mes diferente
precio_venta = Arreglados_y_Significativos[6]   # Julio 2022
pesos_final = usd_comprados * precio_venta

# 3. Ganancia real
ganancia_real = pesos_final - monto

print(usd_comprados)
print(pesos_final)
print(ganancia_real)
print(errorRelativo)