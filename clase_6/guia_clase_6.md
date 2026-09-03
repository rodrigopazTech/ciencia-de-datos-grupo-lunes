# Clase 6: NumPy Fundamental y Análisis Estadístico Vectorizado

**Duración sugerida:** 60 minutos  
**Modalidad:** práctica en Jupyter Lab (o Google Colab)  
**Objetivo:** que el alumnado aprenda a utilizar la librería **NumPy** para crear arrays de una y dos dimensiones, entienda la velocidad de la vectorización frente a los bucles tradicionales, domine el filtrado booleano y realice análisis estadístico descriptivo sobre conjuntos de datos.

---

### 🎨 Apoyo Visual para el Aprendizaje
* **Concepto:** Comparativa del rendimiento del bucle `for` tradicional (un cartero que visita casas a pie una por una) frente a la computación vectorizada en NumPy (una flotilla de vehículos de entrega que arrancan todos al mismo tiempo en paralelo).
* **Prompt para Generar Imagen con IA (Midjourney/DALL-E 3):**
  > *A conceptual 3D comparison illustration. On the left side, a single slow letter carrier walking along a line of houses one by one (labeled 'Python For-Loop'). On the right side, a modern fleet of delivery trucks launching simultaneously in parallel (labeled 'NumPy Vectorization'). Dynamic motion blur, clean vector art style, contrast colors, infographic layout.*

---

## 1. Introducción a NumPy y Vectores (15 min)

### Explicación para instructor

**NumPy** (Numerical Python) es la biblioteca fundamental para el cálculo científico en Python:
- En Ciencia de Datos los conjuntos de datos son numéricos y masivos. Las listas tradicionales de Python son lentas porque permiten mezclar tipos de datos y requieren memoria extra para rastrearlos.
- Los **arrays de NumPy** (`np.array`) son colecciones homogéneas (todos los elementos deben tener exactamente el mismo tipo de dato, ej. flotantes) que se almacenan de manera contigua en memoria, haciéndolos miles de veces más rápidos.
- Para usar NumPy, por convención universal lo importamos usando el alias `np`: `import numpy as np`.

#### Texto para una celda Markdown del notebook

## Introducción a NumPy

NumPy es la librería líder para procesamiento numérico en Python.
- Los arrays de NumPy (`np.array`) son más rápidos y eficientes que las listas porque almacenan datos del mismo tipo en memoria contigua.
- Usamos `.shape` para ver la forma (filas, columnas) y `.ndim` para saber el número de dimensiones.

#### Código para una celda de Jupyter

```python
import numpy as np

# 1. Crear un vector (array de 1 dimensión) a partir de una lista
edades_lista = [20, 25, 30, 35]
edades_array = np.array(edades_lista)

print("Vector de edades:", edades_array)
print("Tipo de objeto:", type(edades_array))
print("Forma (shape):", edades_array.shape)
print("Dimensiones (ndim):", edades_array.ndim)
```

#### Salida esperada

```text
Vector de edades: [20 25 30 35]
Tipo de objeto: <class 'numpy.ndarray'>
Forma (shape): (4,)
Dimensiones (ndim): 1
```

---

## 2. Cómputo Vectorizado y Rendimiento (15 min)

### Explicación para instructor

La gran ventaja de NumPy es la **vectorización**: la capacidad de realizar operaciones aritméticas sobre todo el array de forma instantánea sin escribir un bucle `for` línea por línea.
Para demostrar esta ventaja de velocidad, realizamos un experimento de rendimiento:
- Generamos una lista y un array con 1 millón de registros.
- Sumamos un valor usando un bucle `for` tradicional contra la suma directa en NumPy.

#### Texto para una celda Markdown del notebook

## Cómputo Vectorizado

En NumPy podemos operar sobre colecciones enteras instantáneamente (ej. `array * 2`) sin usar bucles `for`. A esto se le conoce como **vectorización**.

#### Código para una celda de Jupyter

```python
# 1. Operaciones aritméticas simples
precios = np.array([100, 200, 300])
precios_con_iva = precios * 1.16
print("Precios con IVA:", precios_con_iva)

# 2. Experimento de velocidad (Demostración de rendimiento)
millon_lista = list(range(1000000))
millon_array = np.array(millon_lista)

import time

# Medir tiempo con bucle for de Python
t_inicio = time.time()
resultado_for = [x + 10 for x in millon_lista]
t_for = time.time() - t_inicio

# Medir tiempo con vectorización de NumPy
t_inicio = time.time()
resultado_np = millon_array + 10
t_np = time.time() - t_inicio

print(f"\nTiempo con bucle 'for': {t_for:.5f} segundos")
print(f"Tiempo con NumPy vectorizado: {t_np:.5f} segundos")
print(f"¡NumPy es aproximadamente {t_for / t_np:.1f} veces más rápido!")
```

#### Salida esperada (los tiempos exactos pueden variar según el procesador)

```text
Precios con IVA: [116. 232. 348.]

Tiempo con bucle 'for': 0.08240 segundos
Tiempo con NumPy vectorizado: 0.00115 segundos
¡NumPy es aproximadamente 71.7 veces más rápido!
```

---

## 3. Indexación 2D, Máscaras Booleanas y Estadística (20 min)

### Explicación para instructor

Explica la indexación multidimensional:
- Las matrices de 2 dimensiones tienen filas y columnas: `matriz[fila, columna]`. Al igual que en las listas, se empieza en cero.
- La **máscara booleana (Boolean Indexing)** consiste en crear una condición lógica sobre un array (ej. `array > 50`), lo cual genera un array de booleanos (`True/False`). Al pasar esa condición dentro de los corchetes del array `array[condicion]`, NumPy filtra y extrae únicamente los valores que cumplen con la condición.
- NumPy cuenta con funciones optimizadas para obtener estadísticas de forma instantánea.

#### Texto para una celda Markdown del notebook

## Matrices, Filtrado Booleano y Estadística

- Indexación 2D: `matriz[fila, columna]`.
- Máscaras booleanas: Filtramos elementos aplicando condiciones directas, por ejemplo: `array[array > valor]`.
- Estadísticas descriptivas: `np.mean()`, `np.median()`, `np.std()`, `np.min()`, `np.max()`.

#### Código para una celda de Jupyter

```python
# 1. Crear una matriz de 2 filas y 3 columnas (ventas de 2 tiendas en 3 días)
ventas = np.array([
    [120, 150, 90],
    [200, 80, 250]
])

print("Matriz de ventas:\n", ventas)
print("Venta de la tienda 1, día 2 (fila 0, col 1):", ventas[0, 1])

# 2. Filtrado Booleano
ventas_altas = ventas[ventas > 100]
print("\nVentas mayores a 100:", ventas_altas)

# 3. Métricas Estadísticas
print("\n--- Estadísticas del Conjunto de Datos ---")
print("Promedio general de ventas:", np.mean(ventas))
print("Mediana de ventas:", np.median(ventas))
print("Desviación estándar:", np.std(ventas))
print("Máxima venta registrada:", np.max(ventas))
```

#### Salida esperada

```text
Matriz de ventas:
 [[120 150  90]
 [200  80 250]]
Venta de la tienda 1, día 2 (fila 0, col 1): 150

Ventas mayores a 100: [120 150 200 250]

--- Estadísticas del Conjunto de Datos ---
Promedio general de ventas: 148.33333333333334
Mediana de ventas: 135.0
Desviación estándar: 60.11562932289196
Máxima venta registrada: 250
```

> [!NOTE]
> **Métricas Estadísticas Básicas:**
> - **Promedio / Media (`np.mean`):** Es la suma de todos los valores dividida por el número total de datos. Nos da el valor típico o tendencia central de los datos. 
>   * *¿Para qué sirve?* Como referencia rápida del rendimiento general, aunque es sensible a valores extremos (atípicos).
> - **Mediana (`np.median`):** Es el valor que se ubica exactamente en el medio cuando ordenamos los datos de menor a mayor.
>   * *¿Para qué sirve?* Para encontrar el centro real del conjunto de datos. A diferencia del promedio, no se ve afectada por valores extremadamente grandes o pequeños.
> - **Desviación Estándar (`np.std`):** Mide cuánto se alejan (se dispersan) los datos con respecto al promedio.
>   * *¿Para qué sirve?* Para entender la variabilidad o el riesgo. Una desviación alta significa que los datos varían mucho entre sí; una desviación baja indica que la mayoría de los datos son similares al promedio.
> - **Máxima (`np.max`):** Encuentra el valor más alto del conjunto de datos.
>   * *¿Para qué sirve?* Para identificar picos de rendimiento o límites superiores (en este caso, la venta más alta lograda).

---

## 4. Taller de Cierre: Análisis de Lecturas de Sensores (10 min)

### Explicación para instructor

Pide al grupo que abra una celda nueva y resuelva el problema de depuración estadística de datos vectorizados.

#### Actividad para el alumno

Tenemos una matriz que contiene las lecturas de temperatura de tres sensores de temperatura a lo largo de 4 días. Cada fila representa un sensor.
Las lecturas registradas como menores o iguales a `0` grados representan fallas del sensor y deben ser excluidas del análisis.
Escribe un programa que:
1. Cree la matriz de datos con los valores provistos.
2. Aísle las lecturas del tercer sensor (fila con índice 2).
3. Utilice una **máscara booleana** para filtrar las lecturas válidas (temperaturas mayores a 0) en la lectura total de la matriz.
4. Calcule y muestre el promedio y la desviación estándar de las lecturas válidas de la matriz.

#### Código para el notebook

```python
import numpy as np

# Matriz: 3 sensores (filas) x 4 días (columnas)
lecturas = np.array([
    [22.5, 23.0, -99.0, 21.9],  # Sensor 1 (-99.0 representa error)
    [24.1, 23.8, 25.0, 24.3],   # Sensor 2
    [20.5, -99.0, 21.0, 22.0]   # Sensor 3
])

print("Lecturas de la matriz:\n", lecturas)

# 1. Aislar sensor 3 (índice 2)
sensor_3 = lecturas[2]
print("\nLecturas del Sensor 3:", sensor_3)

# 2. Filtrar lecturas válidas (mayores a 0) de toda la matriz
lecturas_validas = lecturas[lecturas > 0]
print("\nLecturas válidas filtered (excluyendo errores):", lecturas_validas)

# 3. Métricas de datos limpios
promedio_limpio = np.mean(lecturas_validas)
desviacion_limpia = np.std(lecturas_validas)

print(f"\nPromedio de lecturas válidas: {promedio_limpio:.2f} °C")
print(f"Desviación estándar de lecturas válidas: {desviacion_limpia:.2f} °C")
```

#### Salida esperada

```text
Lecturas de la matriz:
 [[ 22.5  23.  -99.   21.9]
 [ 24.1  23.8  25.   24.3]
 [ 20.5 -99.   21.   22. ]]

Lecturas del Sensor 3: [ 20.5 -99.   21.   22. ]

Lecturas válidas filtered (excluyendo errores): [22.5 23.  21.9 24.1 23.8 25.  24.3 20.5 21.  22. ]

Promedio de lecturas válidas: 22.81 °C
Desviación estándar de lecturas válidas: 1.45 °C
```

---

## Cierre de la sesión (2 min)

Recapitula brevemente:
Hoy aprendimos las bases de **NumPy**, descubriendo por qué sus arrays contiguos en memoria aceleran los cálculos en Ciencia de Datos. Trabajamos con cómputo vectorizado de alto rendimiento, filtramos matrices usando indexación y **máscaras booleanas**, y obtuvimos estadísticas descriptivas en milisegundos.

En la siguiente sesión (Clase 7) daremos el salto a la herramienta reina del análisis de datos en Python: **Pandas**, aprendiendo a importar y diagnosticar archivos CSV y Excel en tablas estructuradas de tipo DataFrame.
