from punto_flotante import Arreglados_y_Significativos, listaErrores
import os
os.system('cls' if os.name == 'nt' else 'clear')

#De enero a dic de cada año cuanto ganó o perdió el dolar ...
#Para poder verlo tenemos que restar enero - dic de cada año, tomando los índices correspondientes de 
#cada elemento en la lista


enero_anios = [Arreglados_y_Significativos[0],Arreglados_y_Significativos[12],Arreglados_y_Significativos[24],Arreglados_y_Significativos[36]]
diciembre_anios = [Arreglados_y_Significativos[11],Arreglados_y_Significativos[23], Arreglados_y_Significativos[35],Arreglados_y_Significativos[47]]

resta_enero_diciembre = []
i = 0
while i < len(enero_anios):
    resta_enero_diciembre.append(diciembre_anios[i] - enero_anios[i])
    i = i+1

erroes_enero = [listaErrores[0],listaErrores[12],listaErrores[24],listaErrores[36]]
erroes_diciembre = [listaErrores[11],listaErrores[23],listaErrores[35],listaErrores[47]]

propagacion_erroes_resta = []
j = 0
while j < len(enero_anios):
    propagacion_erroes_resta.append(erroes_enero[j] + erroes_diciembre[j])
    j = j+1

propagacion_porcentual = []
l = 0
while l < len(propagacion_erroes_resta):
    propagacion_porcentual.append((propagacion_erroes_resta[l]/resta_enero_diciembre[l])*100)
    l = l+1

print("//////////LISTA DE DIFERENCIAS ENE-DIC Y SUS ERRORES CORRESPONDIENTES//////////")

k = 0
while k < len(resta_enero_diciembre):
    print(f"{resta_enero_diciembre[k]:.2f} +/- {propagacion_erroes_resta[k]:.2f} o {propagacion_porcentual[k]:.2f}%")
    k = k+1

