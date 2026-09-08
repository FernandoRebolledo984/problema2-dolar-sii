from punto_flotante import Arreglados_y_Significativos, listaErrores, listaOriginales
import os
os.system('cls' if os.name == 'nt' else 'clear')

enero_anios = [Arreglados_y_Significativos[0],Arreglados_y_Significativos[12],Arreglados_y_Significativos[24],Arreglados_y_Significativos[36]]
diciembre_anios = [Arreglados_y_Significativos[11],Arreglados_y_Significativos[23], Arreglados_y_Significativos[35],Arreglados_y_Significativos[47]]

# Error absoluto
resta_enero_diciembre = []
i = 0
while i < len(enero_anios):
    resta_enero_diciembre.append(diciembre_anios[i] - enero_anios[i])
    i = i+1

erroes_enero = [listaErrores[0],listaErrores[12],listaErrores[24],listaErrores[36]]
erroes_diciembre = [listaErrores[11],listaErrores[23],listaErrores[35],listaErrores[47]]

# Propagación de error
propagacion_erroes_resta = []
j = 0
while j < len(enero_anios):
    propagacion_erroes_resta.append(erroes_enero[j] + erroes_diciembre[j])
    j = j+1

# Error relativo porcentual
propagacion_porcentual = []
l = 0
while l < len(propagacion_erroes_resta):
    propagacion_porcentual.append(abs((propagacion_erroes_resta[l]/resta_enero_diciembre[l])*100))
    l = l+1

k = 0
ulti = [[],[],[],[]]
while k < len(resta_enero_diciembre):
    ulti[k].append(resta_enero_diciembre[k])
    ulti[k].append(propagacion_erroes_resta[k])
    ulti[k].append(propagacion_porcentual[k])
    k = k+1

propagacion_porcentual.sort()
x=0
y=2
z=0
anio=2022
ulti2=[]
while x<len(ulti):
    if propagacion_porcentual[x] == ulti[z][y]:
        ulti2.append(ulti[z])
        ulti2[x].append(anio)
        z=0
        anio=2022
        x+=1
    else:
        z+=1
        anio+=1

print("\n=== Respuesta A4. Anualidad (variación enero->diciembre) ===")
h=0
while h < len(ulti2):
    print(f" - Año: {ulti2[h][3]}\n - Error Absoluto Enero-Diciembre: {ulti2[h][0]}")
    print(f" - Propagación de Error: {round(ulti2[h][1],5)}\n - Error Relativo Porcentual: {round(ulti2[h][2],3)}%\n")
    h+=1
print("Lo común de ambos años es que su error absoluto llega a ser igual o mayor que la propia diferencia entre ambos, provocando que" \
"el error relativo porcentual sea muy alto, invalidando la certeza del resultado (cancelación catastrófica).\n")

#=============================== Respuesta A5 ===============================
print("\n=== Respuesta A5. Mejor compra y mejor venta ===\n")

monto = 1_000_000
precio_mes_barato = min(listaOriginales)   #Mes más barato del período
precio_mes_caro = max(listaOriginales)     #Mes más caro del período
indice_barato = listaOriginales.index(precio_mes_barato)
indice_caro = listaOriginales.index(precio_mes_caro)
#mes_barato = 
#anio_barato =

#Rentabilidad
compra_barato = monto / precio_mes_barato    #Compramos en el mes más barato
vende_caro = compra_barato * precio_mes_caro #Vendemos en el mes más caro
ganancia = vende_caro-monto        
rentabilidad = (ganancia / monto)*100 #Porcentaje de rentabilidad

#Errores relativos y absolutos de ambos meses
error_relativo_barato = (listaErrores[indice_barato] / precio_mes_barato)*100
error_absoluto_barato = abs((precio_mes_barato - Arreglados_y_Significativos[indice_barato]))
error_relativo_caro = (listaErrores[indice_caro] / precio_mes_caro)*100
error_absoluto_caro = (precio_mes_caro - Arreglados_y_Significativos[indice_caro])
#Error relativo y absoluto de la venta
error_relativo_venta = error_relativo_barato + error_relativo_caro
error_absoluto_venta = (error_relativo_venta / 100) * vende_caro

error_absoluto_ganancia = error_absoluto_venta
error_absoluto_rentabilidad = (error_absoluto_ganancia / monto)*100

print(error_absoluto_rentabilidad)