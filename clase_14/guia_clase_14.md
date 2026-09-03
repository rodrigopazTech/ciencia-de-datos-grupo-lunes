# Clase 14: Evaluación de Modelos y Clasificación

**Duración sugerida:** 60 minutos  
**Modalidad:** práctica en Jupyter Lab  
**Objetivo:** que el alumnado aprenda a evaluar modelos numéricos mediante MSE y $R^2$, domine el entrenamiento de algoritmos de clasificación (Regresión Logística y Árboles de Decisión) utilizando **Scikit-Learn** e interprete una matriz de confusión para calcular exactitud, precisión y recall.

---

### 🎨 Apoyo Visual para el Aprendizaje
* **Concepto:** Tablero de tiro al blanco dividido en una matriz de 2x2 (Matriz de Confusión): los aciertos exactos en el centro del blanco (Verdaderos Positivos y Negativos en verde) y los tiros fallidos en zonas erróneas (Falsos Positivos y Negativos en rojo).
* **Prompt para Generar Imagen con IA (Midjourney/DALL-E 3):**
  > *A 3D target board divided into a 2x2 grid representing a Confusion Matrix. The top-left and bottom-right targets are hit perfectly with arrows (green, labeled 'True positive/negative'). The other two targets have arrows hitting outside or missing (red, labeled 'False positive/negative'). Clear educational layout, isometric view.*

---

## 1. Evaluación de Modelos de Regresión (15 min)

### Explicación para instructor

En la clase anterior entrenamos una regresión lineal para predecir precios. Ahora necesitamos medir numéricamente qué tan bien funciona:
- **Error Cuadrático Medio (MSE):** Promedio de los errores al cuadrado. Penaliza con mayor fuerza las desviaciones grandes.
- **R-cuadrado ($R^2$):** Indica qué porcentaje de la variabilidad del precio logra explicar nuestro modelo. Un valor de `0.80` significa que explicamos el 80% de la variabilidad del mercado inmobiliario.

#### Texto para una celda Markdown del notebook

## Métricas de Evaluación para Regresión

Evaluamos la precisión de las estimaciones numéricas mediante:
- **MSE (Mean Squared Error):** Magnitud de los errores cuadráticos.
- **$R^2$ (R-cuadrado):** Porcentaje de varianza explicada (cercano a 1 es ideal).

#### Código para una celda de Jupyter (reutilizando variables de la regresión anterior de forma conceptual)

```python
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

# Simular valores reales y predicciones para fines ilustrativos
reales = np.array([3.4, 4.5, 2.1, 5.0, 1.8])
predicciones = np.array([3.2, 4.7, 2.3, 4.8, 1.9])

# Calcular métricas
mse = mean_squared_error(reales, predicciones)
r2 = r2_score(reales, predicciones)

print(f"Error Cuadrático Medio (MSE): {mse:.4f}")
print(f"Coeficiente de Determinación (R2): {r2:.4f}")
```

#### Salida esperada

```text
Error Cuadrático Medio (MSE): 0.0340
Coeficiente de Determinación (R2): 0.9769
```

---

## 2. Modelos de Clasificación y Evaluación Cualitativa (35 min)

### Explicación para instructor

Presenta el problema de la **Clasificación**: la variable objetivo ya no es un precio continuo, sino una etiqueta binaria (ej. `1` para aprobado, `0` para rechazado).
- **Regresión Logística:** Modela la probabilidad de pertenencia a una clase.
- **Árboles de Decisión:** Hacen preguntas jerárquicas lógicas para clasificar registros.

Explica la **Matriz de Confusión**:
- **Verdadero Positivo (VP):** El cliente pagaba y el modelo dijo que pagaría.
- **Falso Positivo (FP):** El cliente no pagaba y el modelo dijo que sí pagaría (error costoso para el banco).
- **Verdadero Negativo (VN):** El cliente no pagaba y el modelo dijo que no pagaría.
- **Falso Negativo (FN):** El cliente pagaba y el modelo dijo que no pagaría.

Introduce las métricas:
- **Accuracy (Exactitud):** Total de aciertos del modelo.
- **Precision (Precisión):** ¿De todos los que predije como aprobados, cuántos realmente lo eran? (Evita Falsos Positivos).
- **Recall (Sensibilidad):** ¿De todos los clientes que realmente merecían aprobación, a cuántos logré detectar? (Evita Falsos Negativos).

#### Texto para una celda Markdown del notebook

## Algoritmos de Clasificación y Diagnóstico

- `LogisticRegression` y `DecisionTreeClassifier` clasifican variables categóricas.
- `confusion_matrix` crea la matriz de diagnóstico de aciertos y errores.
- `classification_report` calcula la exactitud, precisión y recall.

#### Código para una celda de Jupyter

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report

# Carga de datos de créditos hipotecarios
df_creditos = pd.read_csv("recursos/credito_hipotecario.csv")

# 1. Separar datos
X = df_creditos[["Ingresos_Mensuales", "Edad", "Score_Credito", "Deudas_Mensuales"]]
y = df_creditos["Credito_Aprobado"]

# 2. Dividir y Escalar
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Entrenar Regresión Logística
modelo_log = LogisticRegression()
modelo_log.fit(X_train_scaled, y_train)
y_pred = modelo_log.predict(X_test_scaled)

# 4. Evaluación diagnóstica
print("--- Matriz de Confusión ---")
print(confusion_matrix(y_test, y_pred))

print("\n--- Reporte de Clasificación ---")
print(classification_report(y_test, y_pred))
```

#### Salida esperada (los valores exactos dependerán de la generación aleatoria)

```text
--- Matriz de Confusión ---
[[22  3]
 [ 2 23]]

--- Reporte de Clasificación ---
              precision    recall  f1-score   support

           0       0.92      0.88      0.90        25
           1       0.88      0.92      0.90        25

    accuracy                           0.90        50
   macro avg       0.90      0.90      0.90        50
weighted avg       0.90      0.90      0.90        50
```

---

## 3. Taller de Cierre: Comparando Algoritmos (10 min)

### Explicación para instructor

Pide al grupo que entrene un Árbol de Decisión sobre el mismo conjunto de datos y compare su rendimiento frente a la Regresión Logística.

#### Actividad para el alumno

Entrena un **Árbol de Decisión** utilizando Scikit-Learn sobre los mismos datos escalados de créditos hipotecarios:
1. Importa `DecisionTreeClassifier` desde `sklearn.tree`.
2. Instancia el modelo (`modelo_tree = DecisionTreeClassifier(max_depth=3, random_state=42)`).
3. Entrénalo con los datos escalados y predice sobre el conjunto de prueba.
4. Muestra su matriz de confusión y su reporte de clasificación para contrastar cuál algoritmo clasifica mejor a los clientes riesgosos.

#### Código para el notebook

```python
from sklearn.tree import DecisionTreeClassifier

# 1. Instanciar y Entrenar
modelo_tree = DecisionTreeClassifier(max_depth=3, random_state=42)
modelo_tree.fit(X_train_scaled, y_train)

# 2. Predecir
y_pred_tree = modelo_tree.predict(X_test_scaled)

# 3. Mostrar reportes
print("--- Matriz de Confusión (Árbol de Decisión) ---")
print(confusion_matrix(y_test, y_pred_tree))

print("\n--- Reporte de Clasificación (Árbol de Decisión) ---")
print(classification_report(y_test, y_pred_tree))
```

#### Salida esperada

```text
--- Matriz de Confusión (Árbol de Decisión) ---
[[21  4]
 [ 3 22]]

--- Reporte de Clasificación (Árbol de Decisión) ---
(Reporte mostrando una exactitud ligeramente diferente, ej. 86% vs. 90%)
```

---

## Cierre de la sesión (2 min)

Recapitula brevemente:
Hoy aprendimos a evaluar rigurosamente nuestros modelos de inteligencia artificial. Comprendimos el uso de MSE y $R^2$ para regresión y dominamos la clasificación mediante Regresión Logística y Árboles de Decisión, interpretando las métricas de exactitud, precisión y recall en la toma de decisiones.

En la siguiente sesión (Clase 15) ejecutaremos el **Proyecto Final del Curso**, un taller práctico e integrador de inicio a fin donde cargaremos, limpiaremos, exploraremos y modelaremos predictivamente un conjunto de datos inmobiliarios en la CDMX.
