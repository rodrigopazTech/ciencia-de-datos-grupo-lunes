# Temario de la Clase 7: Introducción a Pandas y Estructuras de Datos (60 minutos)

**Objetivo:** Comprender las estructuras de datos bidimensionales en Python utilizando Series y DataFrames de Pandas, aprender a importar conjuntos de datos reales desde archivos CSV/Excel, y realizar un diagnóstico inicial de la salud de los datos.

---

### 1. La Herramienta Reina del Científico de Datos: Pandas (15 minutos)
* **¿Qué es Pandas?:** Importancia de las estructuras tabulares en el análisis de datos.
* **Estructuras de Datos:**
  - **Series:** Arreglos unidimensionales con etiquetas de índice.
  - **DataFrames:** Tablas bidimensionales con filas indexadas y columnas etiquetadas (el equivalente a una hoja de cálculo).

### 2. Ingesta de Datos (Data Ingestion) (20 minutos)
* **Carga de Archivos:** Lectura de archivos CSV locales utilizando `pd.read_csv("recursos/ventas_ecommerce.csv")`.
* **Carga desde URLs:** Lectura directa de archivos CSV en la nube mediante URLs.

### 3. Diagnóstico de Salud de los Datos (15 minutos)
* **Inspección de Estructura:** Uso de métodos diagnósticos:
  - `.head(n)` y `.tail(n)`: previsualizar los primeros y últimos registros.
  - `.shape`: conocer las dimensiones del dataset (filas y columnas).
  - `.info()`: examinar tipos de datos de las columnas y conteo de valores no nulos.
  - `.describe()`: obtener estadísticas descriptivas rápidas de las columnas numéricas.

### 4. Taller de Cierre (10 minutos)
* **Ejercicio práctico (Explorador de Ventas):** Cargar el archivo de recursos `ventas_ecommerce.csv`, visualizar los primeros 10 registros, determinar las dimensiones del archivo e imprimir el resumen estructural (`.info()`) para identificar si hay columnas con valores nulos o tipos de datos incorrectos.
* **Cierre:** Conexión hacia la Clase 8 (Limpieza y filtrado de datos con Pandas).
