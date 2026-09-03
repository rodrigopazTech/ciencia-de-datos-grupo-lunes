# Temario de la Clase 12: Estadística Descriptiva e Introducción a Machine Learning (60 minutos)

**Objetivo:** Establecer las bases estadísticas descriptivas necesarias para el modelado de datos, comprender el propósito del Machine Learning y diferenciar sus principales paradigmas (Supervisado y No Supervisado), así como identificar la variable objetivo ($y$) y las características independientes ($X$).

---

### 1. Puentes Estadísticos hacia el Machine Learning (15 minutos)
* **Medidas de Tendencia Central:** Comprensión profunda de la media, mediana y moda en el contexto de distribuciones sesgadas.
* **Medidas de Dispersión:** Varianza y Desviación Estándar. Cómo cuantifican el riesgo, error o variabilidad en los datos.
* **Outliers (Valores Atípicos):** Impacto de los valores atípicos en las estadísticas resumen.

### 2. Fundamentos de Machine Learning (20 minutos)
* **¿Qué es Machine Learning?:** El cambio de paradigma de la programación tradicional (Reglas + Datos $\rightarrow$ Respuestas) al Machine Learning (Datos + Respuestas $\rightarrow$ Reglas).
* **Paradigmas del Aprendizaje Automático:**
  - **Aprendizaje Supervisado:** El algoritmo aprende a partir de datos etiquetados (cuenta con respuestas históricas).
    - *Regresión:* Predicción de valores numéricos continuos (ej. estimación de ingresos o precios).
    - *Clasificación:* Predicción de categorías o etiquetas discretas (ej. aprobado/rechazado, sano/enfermo).
  - **Aprendizaje No Supervisado:** El algoritmo busca patrones ocultos en datos sin etiquetar (ej. segmentación de clientes o Clustering).

### 3. Representación de Datos en ML: Matriz $X$ y Vector $y$ (15 minutos)
* **Features ($X$):** Las variables independientes o características descriptoras (matriz bidimensional).
* **Target ($y$):** La variable dependiente o etiqueta que deseamos predecir (vector unidimensional).

### 4. Taller de Cierre (10 minutos)
* **Ejercicio práctico (Anatomía del Modelado):** Tomar la estructura del dataset de e-commerce y plantear dos problemas de Machine Learning que resuelvan necesidades de negocio reales: uno de Regresión (estimar montos de compra) y uno de Clasificación (predecir si una compra será cancelada), aislando en celdas de texto cuáles serían las características ($X$) y cuál sería la variable objetivo ($y$) para cada caso.
* **Cierre:** Conexión hacia la Clase 13 (Modelado predictivo numérico con Regresión Lineal en Scikit-Learn).
