from punto_flotante import listaErrores as errorAbsoluto, Arreglados_y_Significativos, listaOriginales as valorVerdadero
import os

os.system('cls' if os.name == 'nt' else 'clear')

errorRelativo = []

i = 0
while i < len(Arreglados_y_Significativos):
    errorRelativo.append((errorAbsoluto[i]/valorVerdadero[i])*100)
    i = i+1

##OPERACIONES DE PROPAGACIÓN (UNA DE CADA UNA)##

print(Arreglados_y_Significativos)

def comprar_dolares(monto, precio):
    dollars = monto / precio
    return dollars

montoTrabajo = 1000000

usd = comprar_dolares(montoTrabajo, Arreglados_y_Significativos)            
