# Temario de la Clase 6: NumPy Fundamental y Análisis Estadístico Vectorizado (60 minutos)

**Objetivo:** Introducir la biblioteca líder del cómputo numérico, NumPy, comprendiendo el rendimiento de las operaciones vectorizadas frente a los bucles tradicionales, y aprender a realizar filtrados lógicos y cálculos estadísticos sobre matrices multidimensionales.

---

### 1. Introducción a NumPy y Vectores (15 minutos)
* **¿Qué es NumPy?:** Importancia de las estructuras homogéneas y rápidas en Ciencia de Datos.
* **Creación de Arreglos (Arrays):** Creación de vectores y matrices a partir de listas con `np.array()`.
* **Propiedades de un Array:** Inspección de forma (`.shape`) y dimensiones (`.ndim`).

### 2. Cómputo Vectorizado y Rendimiento (15 minutos)
* **Operaciones Vectorizadas:** Suma, multiplicación y cálculos matemáticos directos sobre arrays sin usar bucles.
* **Demostración Práctica de Velocidad:** Comparativa de rendimiento entre un bucle `for` de Python clásico frente a una operación vectorizada en NumPy procesando grandes cantidades de registros.

### 3. Indexación 2D y Filtrado mediante Máscaras Booleanas (20 minutos)
* **Acceso Multidimensional:** Indexación de filas y columnas en matrices de 2 dimensiones.
* **Máscaras Booleanas (Boolean Indexing):** Filtrado masivo de datos que cumplen con criterios condicionales (ej. seleccionar todos los valores mayores a un umbral).
* **Métricas Estadísticas:** Cálculo de medidas descriptivas instantáneas sobre grandes conjuntos de datos usando `np.mean()`, `np.median()`, `np.std()`, `np.min()` y `np.max()`.

### 4. Taller de Cierre (10 minutos)
* **Ejercicio práctico:** Tomar una matriz de mediciones de temperatura de varios sensores, aislar las lecturas de un sensor específico mediante indexación, filtrar lecturas erróneas (valores fuera de rango) con máscaras booleanas y calcular el promedio y desviación estándar de los datos limpios.
* **Cierre:** Conexión hacia la Clase 7 (Carga y análisis tabular con la librería Pandas).
