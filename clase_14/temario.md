# Temario de la Clase 14: Evaluación de Modelos y Clasificación (60 minutos)

**Objetivo:** Comprender las métricas de evaluación para modelos de regresión numérica, aprender a modelar variables categóricas mediante algoritmos de clasificación (Regresión Logística y Árboles de Decisión) y dominar el diagnóstico de modelos de clasificación mediante matrices de confusión y métricas de exactitud, precisión y sensibilidad.

---

### 1. Métricas de Evaluación para Regresión (15 minutos)
* **Error Cuadrático Medio (MSE):** Medida de la magnitud de la desviación cuadrática promedio de las predicciones.
* **Coeficiente de Determinación ($R^2$):** Proporción de la varianza explicada por el modelo predictivo (Rango `[0, 1]`, donde 1 es un ajuste perfecto).

### 2. Algoritmos de Clasificación (15 minutos)
* **El Problema de Clasificación:** Predicción de clases mutuamente excluyentes (ej. Aprobado o Rechazado).
* **Regresión Logística:** Uso de la función sigmoide para predecir probabilidades entre 0 y 1.
* **Árboles de Decisión:** Clasificación no lineal basada en ramificaciones lógicas de decisión (ej. `if score_credito >= 650`).

### 3. Métricas de Evaluación para Clasificación (20 minutos)
* **Matriz de Confusión:** Tabla de doble entrada que contrasta las predicciones contra las etiquetas reales (Verdaderos Positivos, Falsos Positivos, Verdaderos Negativos, Falsos Negativos).
* **Métricas Clave:**
  - **Exactitud (Accuracy):** Proporción general de aciertos.
  - **Precisión (Precision):** Proporción de aciertos entre las predicciones positivas (evalúa el costo de un Falso Positivo).
  - **Sensibilidad (Recall / Sensitivity):** Proporción de positivos reales detectados por el modelo (evalúa el costo de un Falso Negativo).

### 4. Taller de Cierre (10 minutos)
* **Ejercicio práctico (Evaluación de Créditos Hipotecarios):** Cargar el dataset `credito_hipotecario.csv`. Separar en $X$ e $y$ (crédito aprobado). Dividir, escalar, instanciar y entrenar una Regresión Logística y un Árbol de Decisión. Calcular y contrastar la matriz de confusión y las métricas de Exactitud y Sensibilidad de ambos modelos.
* **Cierre:** Conexión hacia la Clase 15 (Taller práctico guiado del Proyecto Final aplicado de inicio a fin).
