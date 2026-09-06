from punto_flotante import Arreglados_y_Significativos, listaErrores
import os
os.system('cls' if os.name == 'nt' else 'clear')

#De enero a dic de cada año cuanto ganó o perdió el dolar ...
#Para poder verlo tenemos que restar enero - dic de cada año, tomando los índices correspondientes de 
#cada elemento en la lista

print(Arreglados_y_Significativos)
enero_diciembre_anios = [Arreglados_y_Significativos[0], Arreglados_y_Significativos[11],Arreglados_y_Significativos[12],Arreglados_y_Significativos[23],Arreglados_y_Significativos[24], Arreglados_y_Significativos[35], Arreglados_y_Significativos[36],Arreglados_y_Significativos[47]]
print(enero_diciembre_anios)
