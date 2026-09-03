# Temario General del Curso: Ciencia de Datos con Python (16 Clases)

**Duración total:** 16 sesiones (60 minutos por sesión)  
**Metodología:** Práctica guiada orientada 100% a tareas reales de Ciencia de Datos (Ingesta, Limpieza, EDA, Feature Engineering, Machine Learning y Data Storytelling).

---

## 📌 Módulo 1: Fundamentos de Programación Orientada a Datos (Clases 1 a 4)

### Clase 1: Historia de la Ciencia de Datos y Panorama Profesional
* **🎯 Aplicación en Ciencia de Datos:** *Entendimiento del Rol, el Ciclo de Vida de los Datos (CRISP-DM) y el Valor de Negocio.*
* Historia de la Ciencia de Datos, panorama profesional e introducción al ecosistema de herramientas.
* El rol del Científico de Datos vs. Ingeniero de Software vs. Analista de BI.

### Clase 2: Fundamentos de Python I: Variables, Tipos de Datos y Listas Básicas
* **🎯 Aplicación en Ciencia de Datos:** *Estructuración y Almacenamiento Inicial de Datos.*
* Introducción a Python y Google Colab: celdas de código y de texto.
* Variables, tipado dinámico y tipos de datos elementales (`int`, `float`, `str`, `bool`).
* Operadores aritméticos y de texto (concatenación y repetición), y el puente hacia los datos con listas e índices.

### Clase 3: Fundamentos de Python II: Formateo de Texto, Slicing, Condicionales y Diccionarios
* **🎯 Aplicación en Ciencia de Datos:** *Manipulación de Texto y Toma de Decisiones con Datos.*
* Manipulación y formateo de texto moderno con `f-strings` (formatos decimales y saltos de línea).
* Métodos útiles de texto (`.upper()`, `.lower()`, `.strip()`, `.replace()`), interactividad con `input()` y casting.
* Selección de datos en listas mediante *slicing* e introducción a Diccionarios (`dict`).
* Lógica condicional con operadores de comparación, lógicos y estructuras `if/elif/else`.

### Clase 4: Fundamentos de Python III: Colecciones Estructuradas y Bucles
* **🎯 Aplicación en Ciencia de Datos:** *Estructuración y Recorrido Automatizado de Colecciones.*
* Uso de Diccionarios y sus métodos integrados (`.keys()`, `.values()`, `.items()`).
* Automatización con bucles `for` y `range()` (recorrido de listas y diccionarios).
* Comprensión de listas (*list comprehensions*) para crear y filtrar colecciones usando `not`.

---

## 📊 Módulo 2: Cómputo Numérico y Manipulación de Datos (Clases 5 a 9)

### Clase 5: Modularidad de Código y Entorno Local (Jupyter Lab)
* **🎯 Aplicación en Ciencia de Datos:** *Encapsulación de Lógica y Configuración del Entorno Profesional Local.*
* Modularidad de código con funciones (`def`, `return` vs `print`) e importación de módulos nativos (`import`, `as`).
* Configuración del entorno local: Anaconda Navigator y ejecución de Jupyter Lab.

### Clase 6: NumPy Fundamental y Análisis Estadístico Vectorizado
* **🎯 Aplicación en Ciencia de Datos:** *Filtrado Masivo y Caracterización Estadística de Datos Vectorizados.*
* Introducción a **NumPy**: creación de vectores y matrices multidimensionales (`np.array`).
* Comparativa de velocidad: rendimiento del cómputo vectorizado frente al bucle `for` tradicional.
* Indexación 2D, máscaras booleanas para filtrado lógico y métricas estadísticas descriptivas (`np.mean()`, `np.median()`, `np.std()`, `np.min()`, `np.max()`).

### Clase 7: Introducción a Pandas & Estructura de DataFrames
* **🎯 Aplicación en Ciencia de Datos:** *Ingesta de Datos (Data Ingestion) e Inspección Estructurada de Datasets.*
* La herramienta reina del Data Scientist: Series y DataFrames en **Pandas**.
* Carga de datos desde archivos reales (`pd.read_csv()`, `pd.read_excel()`).
* Diagnóstico inicial de salud de datos: `.head()`, `.info()`, `.describe()`, `.shape`.

### Clase 8: Limpieza y Filtrado de Datos con Pandas
* **🎯 Aplicación en Ciencia de Datos:** *Depuración de Datos (Data Cleaning) y Control de Calidad de la Información.*
* Tratamiento profesional de valores nulos o faltantes (`isna()`, `dropna()`, `fillna()`).
* Detección y eliminación de duplicados (`drop_duplicates()`) y corrección de tipos de datos (*casting*).
* Selección técnica y segmentación de datos con `.loc[]` e `.iloc[]`.

### Clase 9: Transformación, Agregación y Uniones en Pandas
* **🎯 Aplicación en Ciencia de Datos:** *Ingeniería de Características (Feature Engineering) y Modelado Multitabla.*
* Creación de nuevas variables indicadoras y transformación mediante `.apply()`.
* Agrupación y resumen ejecutivo de datos por categorías con `.groupby()`.
* Integración y cruce de múltiples fuentes de datos con `.merge()` y `.concat()`.

---

## 📈 Módulo 3: Visualización de Datos y Análisis Exploratorio - EDA (Clases 10 y 11)

### Clase 10: Visualización de Datos I con Matplotlib
* **🎯 Aplicación en Ciencia de Datos:** *Diagnóstico Visual de Distribuciones y Comunicación de Métricas.*
* Principios de diseño visual de información y anatomía de un gráfico en Matplotlib.
* Creación de gráficos para tendencias (líneas), comparaciones (barras) y comportamiento (histogramas).
* Personalización técnica: títulos, ejes, leyendas y escalas visuales.

### Clase 11: Visualización Estadística con Seaborn y Análisis Exploratorio (EDA)
* **🎯 Aplicación en Ciencia de Datos:** *Análisis Exploratorio de Datos (EDA) y Detección de Patrones y Relaciones.*
* Gráficos estadísticos avanzados en Seaborn: dispersión (*scatter plot*), distribución por categorías (*box plot*) y mapas de calor (*heatmaps*).
* Análisis de correlación entre variables para descubrir factores clave.
* Ejecución completa de una metodología EDA en un dataset real.

---

## 🤖 Módulo 4: Estadística, Machine Learning y Proyecto Final (Clases 12 a 16)

### Clase 12: Estadística Descriptiva e Introducción a Machine Learning
* **🎯 Aplicación en Ciencia de Datos:** *Modelado Estadístico y Formulación de Problemas Predictivos.*
* Conexión entre medidas estadísticas (media, desviación, percentiles, covarianza) y algoritmos.
* Fundamentos de Machine Learning: Aprendizaje Supervisado vs. No Supervisado.
* Definición formal de variables predictoras ($X$) y variable objetivo ($y$).

### Clase 13: Preparación de Datos y Regresión Lineal con Scikit-Learn
* **🎯 Aplicación en Ciencia de Datos:** *Modelado Predictivo Numérico (Estimación de Precios, Costos o Ventas).*
* Uso de la librería líder en ML: **Scikit-Learn**.
* División científica del dataset: Entrenamiento y Prueba (`train_test_split`).
* Escalado de características (`StandardScaler`) y entrenamiento del modelo de Regresión Lineal (`.fit()`, `.predict()`).

### Clase 14: Evaluación de Modelos y Clasificación
* **🎯 Aplicación en Ciencia de Datos:** *Validación de Algoritmos, Métricas de Desempeño y Clasificación de Eventos.*
* Evaluación cuantitativa de predicciones: Error Cuadrático Medio ($MSE$) y Coeficiente $R^2$.
* Modelos de clasificación (ej. Regresión Logística / Árboles de Decisión) para predecir categorías o riesgos.
* Matriz de confusión y métricas clave (*Accuracy*, *Precision*, *Recall*).

### Clase 15: Proyecto Final Aplicado (Taller Práctico Guiado)
* **🎯 Aplicación en Ciencia de Datos:** *Construcción de una Solución de Ciencia de Datos de Extremo a Extremo (End-to-End).*
* Desarrollo guiado del proyecto integrador (ej. Predicción del precio de mercado de futbolistas o estimación de demanda).
* Pipeline completo: Ingesta de datos $\rightarrow$ Limpieza $\rightarrow$ EDA visual $\rightarrow$ Modelado predictivo con Scikit-Learn.

### Clase 16: Presentación de Proyectos, Conclusiones y Ruta Futura
* **🎯 Aplicación en Ciencia de Datos:** *Narrativa de Datos (Data Storytelling) y Toma de Decisiones de Negocio.*
* Presentación de resultados y recomendaciones de negocio por parte de los alumnos (*Storytelling* con datos).
* Retroalimentación técnica del instructor.
* Hoja de ruta para especialización futura: Machine Learning Avanzado, SQL para Big Data, PowerBI/Tableau.
