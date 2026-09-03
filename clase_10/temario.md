# Temario de la Clase 10: Visualización de Datos I con Matplotlib (60 minutos)

**Objetivo:** Comprender la importancia del diseño visual de la información y dominar la creación y personalización de gráficos de líneas, barras e histogramas en Python utilizando Matplotlib.

---

### 1. Principios de Visualización y Anatomía de un Gráfico (15 minutos)
* **Importancia de la Visualización:** Cómo el cerebro procesa la información visual frente a las tablas numéricas.
* **Anatomía en Matplotlib:** Comprensión de los componentes de un gráfico (Figure, Axes, Title, Labels, Legend, Grid y Ticks).
* **Importación:** Sintaxis estándar `import matplotlib.pyplot as plt`.

### 2. Creación de Gráficos Básicos (20 minutos)
* **Gráfico de Tendencia (Líneas):** Uso de `plt.plot()` para mostrar comportamientos a lo largo del tiempo (ej. ventas por fecha).
* **Gráfico de Comparación (Barras):** Uso de `plt.bar()` o `plt.barh()` para comparar métricas entre categorías (ej. ventas por ciudad).
* **Gráfico de Distribución (Histograma):** Uso de `plt.hist()` para visualizar la frecuencia y distribución de variables numéricas continuas (ej. distribución de precios unitarios).

### 3. Personalización y Diseño Profesional (15 minutos)
* **Formato y Estilo:** Configurar títulos descriptivos (`plt.title()`), etiquetas en ejes (`plt.xlabel()`, `plt.ylabel()`), cuadrículas (`plt.grid()`), y colores personalizados.
* **Guardar Gráficos:** Exportar gráficos a imágenes en el disco usando `plt.savefig()`.

### 4. Taller de Cierre (10 minutos)
* **Ejercicio práctico (Análisis Visual de Ventas):** Tomar el dataset de ventas, agrupar las ventas por `Ciudad` y generar un gráfico de barras verticales personalizado. Incluir etiquetas en los ejes, título descriptivo, cuadrícula de fondo, colores estilizados y guardar el gráfico como archivo de imagen `ventas_por_ciudad.png` en recursos.
* **Cierre:** Conexión hacia la Clase 11 (Visualización avanzada con Seaborn y Análisis Exploratorio de Datos - EDA).
