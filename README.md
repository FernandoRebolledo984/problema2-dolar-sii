# Laboratorio: Propagación de Error en el Valor del Dólar

## Descripción del Proyecto
El objetivo principal es evaluar cómo el redondeo a 2 cifras significativas pueden afectar el análisis del precio del dólar en Chile a lo largo de los años. Utilizando el archivo mostrando datos mensuales del dólar observado (SII, 2022-2025), el proyecto analiza la propagación de errores absolutos y relativos, demostrando el fenómeno de cancelación catastrófica al operar con valores numéricamente cercanos.

---

## Estructura del Repositorio
* **`data/`**: Directorio para el dataset original (`dolar_observado_sii_2022_2025.csv`) y destino de la tabla generada (`tabla_errores.csv`).
* **`src/cargar_datos.py`**: Script base que importa los datos a trabajar desde el archivo CSV usando estructuras de `numpy`.
* **`src/punto_flotante.py`**: Script que evalúa la deriva de precisión (ciclo de ida y vuelta) y contrasta la pérdida de cifras significativas entre representaciones de 32 y 64 bits.
* **`src/anualidad.py`**: Script que calcula la variación de precios anual (enero a diciembre) y la rentabilidad entre el mes mínimo y máximo del conjunto de datos.
* **`src/errores.py`**: Script principal que analiza el error de representación, propaga el error en operaciones compuestas, exporta los resultados en un archivo CSV y genera también las gráficas.
* **`graficos/`**: Directorio de salida que almacena los cinco gráficos exigidos en formato PNG.
* **`requirements.txt`**: Listado de dependencias y librerías de Python necesarias para el entorno.

---

## Instrucciones de Ejecución
Para reproducir el análisis completo y generar los archivos de salida, sigue este orden en tu terminal:

1. **Asegurar dependencias**: Instala las dependencias ejecutando `pip install -r requirements.txt`.
2. **Conocer el límite de la máquina**: Ejecuta `python src/punto_flotante.py` para visualizar en consola los problemas de redondeo nativo de la computadora.
3. **Calcular rentabilidad**: Ejecuta `python src/anualidad.py` para obtener el análisis financiero y las conclusiones de los períodos.
4. **Generar tablas y gráficas**: Ejecuta `python src/errores.py`. Este paso final procesa la propagación de error, exporta automáticamente la tabla de datos y construye los 5 gráficos del laboratorio.