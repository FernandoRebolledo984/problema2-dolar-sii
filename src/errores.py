from punto_flotante import listaErrores, Arreglados_y_Significativos, listaOriginales
import os

os.system('cls' if os.name == 'nt' else 'clear')

valoeVerdadero = listaOriginales
errorAbsoluto = listaErrores
errorRelativo = []

i = 0
while i < len(Arreglados_y_Significativos):
    errorRelativo.append((errorAbsoluto[i]/valoeVerdadero[i])*100)
    i = i+1


