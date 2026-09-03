# Temario de la Clase 15: Taller del Proyecto Final Aplicado (60 minutos)

**Objetivo:** Consolidar el conocimiento adquirido a lo largo de todo el curso mediante la ejecución guiada de un proyecto de ciencia de datos completo de inicio a fin (End-to-End), abarcando la ingesta de datos, limpieza, análisis exploratorio, modelado predictivo y comunicación de resultados.

---

### 1. Presentación del Reto Inmobiliario en CDMX (10 minutos)
* **El Problema del Negocio:** Necesidad de valuar propiedades de forma automática en la CDMX para un portal inmobiliario.
* **El Dataset:** Inspección inicial del archivo `propiedades_cdmx.csv` de recursos.

### 2. Pipeline de Ciencia de Datos: Ingesta, Limpieza y EDA (20 minutos)
* **Ingesta y Estructura:** Cargar el archivo CSV en Pandas e inspeccionar su salud preliminar.
* **Limpieza:** Tratamiento de posibles valores nulos o atípicos y codificación simple de variables categóricas (la alcaldía).
* **Análisis Exploratorio (EDA):** Diseñar visualizaciones estadísticas (Boxplots y Scatterplots con Seaborn) para identificar qué variables (m² u ubicación) impactan con mayor fuerza el valor de la vivienda.

### 3. Modelado Predictivo y Valuación del Error (20 minutos)
* **Modelado:** Separación en variables independientes ($X$) y objetivo ($y$). Partición científica de entrenamiento y prueba, normalización y ajuste de un modelo de Regresión Lineal en Scikit-Learn.
* **Evaluación:** Medición de precisión usando las métricas $R^2$ y Error Cuadrático Medio.

### 4. Taller de Cierre y Retroalimentación (10 minutos)
* **Puesta en Común:** Análisis crítico del modelo obtenido, interpretación de coeficientes de las variables (cuánto cuesta un metro cuadrado adicional según el modelo) e identificación de posibles mejoras técnicas para expandir el proyecto.
* **Cierre:** Conexión hacia la Clase 16 (Presentación de portafolio, conclusiones del curso y próximos pasos).
