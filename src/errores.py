from punto_flotante import listaErrores as errorAbsoluto, Arreglados_y_Significativos, listaOriginales as valorVerdadero
import os

os.system('cls' if os.name == 'nt' else 'clear')

errorRelativo = []

i = 0
while i < len(Arreglados_y_Significativos):
    errorRelativo.append((errorAbsoluto[i]/valorVerdadero[i])*100)
    i = i+1

#OPERACIONES DE PROPAGACIÓN (UNA DE CADA UNA)##          

monto = 1000000

#DIVISION (COMPRA DOLARES) USD = MONTO / PRECIO_COMPRA

USD = []

for i in Arreglados_y_Significativos:
    USD.append(monto/i)

print(USD)