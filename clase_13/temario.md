# Temario de la Clase 13: Preparación de Datos y Regresión Lineal con Scikit-Learn (60 minutos)

**Objetivo:** Comprender y aplicar el flujo de modelado predictivo de regresión numérica utilizando Scikit-Learn, aprendiendo a realizar la división científica del dataset en conjuntos de entrenamiento y prueba, escalar características numéricas y entrenar y aplicar un modelo de Regresión Lineal.

---

### 1. Preparación Científica de Datos en Machine Learning (20 minutos)
* **La Librería Scikit-Learn:** Introducción al estándar de la industria en Python (`sklearn`).
* **División del Dataset (`train_test_split`):** Por qué dividimos los datos en entrenamiento (Train, 80%) para que el modelo aprenda, y prueba (Test, 20%) para evaluarlo de forma imparcial.
* **Escalado de Características (`StandardScaler`):** Normalización de variables numéricas para que tengan media 0 y varianza 1, evitando que variables con escalas grandes (como los metros cuadrados) dominen a variables pequeñas (como el número de recámaras).

### 2. Algoritmo de Regresión Lineal (15 minutos)
* **Concepto de Regresión Lineal:** La ecuación de la línea ($y = mx + b$). Búsqueda de los coeficientes óptimos que minimizan la distancia (error) a los puntos reales.

### 3. Entrenamiento y Predicción con Scikit-Learn (15 minutos)
* **El Flujo Estándar de Scikit-Learn:**
  - Instanciar el modelo: `modelo = LinearRegression()`.
  - Entrenar el modelo: `modelo.fit(X_train, y_train)`.
  - Predecir nuevos valores: `y_pred = modelo.predict(X_test)`.

### 4. Taller de Cierre (10 minutos)
* **Ejercicio práctico (Predicción de Viviendas CDMX):** Cargar el dataset `propiedades_cdmx.csv`. Separar las columnas en $X$ e $y$ (precio). Realizar la división entrenamiento/prueba, aplicar el escalado de datos, entrenar una regresión lineal con Scikit-Learn y realizar una predicción sobre una vivienda nueva ficticia en la Ciudad de México.
* **Cierre:** Conexión hacia la Clase 14 (Evaluación cuantitativa del modelo mediante métricas y modelado de clasificación).
