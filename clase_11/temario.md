# Temario de la Clase 11: Visualización Estadística con Seaborn y Análisis Exploratorio (60 minutos)

**Objetivo:** Aprender a utilizar la biblioteca Seaborn para simplificar gráficos estadísticos avanzados, comprender el concepto de correlación numérica y ejecutar un Análisis Exploratorio de Datos (EDA) completo y estructurado sobre un dataset real.

---

### 1. Seaborn: Gráficos Estadísticos Simplificados (15 minutos)
* **¿Qué es Seaborn?:** Ventajas de Seaborn frente a Matplotlib (integración directa con DataFrames y paletas estilizadas por defecto).
* **Importación:** Sintaxis estándar `import seaborn as sns`.
* **Gráficos Estadísticos:**
  - **Relación (`sns.scatterplot()`):** Dispersión para evaluar relaciones entre dos variables numéricas.
  - **Distribución de Grupos (`sns.boxplot()`):** Diagramas de caja y bigotes para comparar distribuciones entre variables categóricas (identificación visual de valores atípicos o *outliers*).

### 2. Correlaciones Numéricas y Mapas de Calor (15 minutos)
* **Correlación de Pearson:** Comprensión matemática y lógica del rango `[-1, 1]` en relaciones lineales.
* **Cálculo de Matriz de Correlación:** Uso de `.corr(numeric_only=True)` en Pandas.
* **Visualización de Correlación (`sns.heatmap()`):** Representación visual de matrices de correlación utilizando mapas de calor de Seaborn.

### 3. El Método del Científico de Datos: EDA Completo (15 minutos)
* **Ciclo de vida del EDA:** Inspeccionar tipos de datos, limpiar inconsistencias, analizar distribuciones, detectar correlaciones y formular hipótesis del negocio a través de visualizaciones.

### 4. Taller de Cierre (15 minutos)
* **Ejercicio práctico (EDA de Negocio):** Tomar el dataset de e-commerce y realizar un EDA guiado: analizar el boxplot de precios por categoría, graficar la relación entre precio unitario y cantidad vendida, calcular y mostrar el mapa de calor de correlaciones del negocio y documentar verbalmente tres hallazgos clave de valor.
* **Cierre:** Conexión hacia la Clase 12 (Estadística descriptiva formal e introducción teórica a los algoritmos de Machine Learning).
