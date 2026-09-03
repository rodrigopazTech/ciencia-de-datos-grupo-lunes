# Clase 13: Preparación de Datos y Regresión Lineal con Scikit-Learn

**Duración sugerida:** 60 minutos  
**Modalidad:** práctica en Jupyter Lab  
**Objetivo:** que el alumnado aprenda a utilizar la librería **Scikit-Learn** para dividir un dataset con `train_test_split()`, normalizar datos empleando `StandardScaler()`, y entrenar y realizar predicciones numéricas con el algoritmo de **Regresión Lineal**.

---

### 🎨 Apoyo Visual para el Aprendizaje
* **Concepto:** Representación geométrica e intuitiva de la Regresión Lineal: una nube de puntos flotando sobre una cuadrícula azul, atravesada por una recta de color rosa brillante de la que se extienden pequeños resortes o tensores verticales hacia cada punto (representando los residuos o errores que el modelo busca minimizar).
* **Prompt para Generar Imagen con IA (Midjourney/DALL-E 3):**
  > *A 3D plot with floating scatter points in a dark grid space. A bright neon pink straight line passes through the points, with tiny glowing springs connecting each point to the line (representing residuals/errors). Futuristic science aesthetic, deep blues and hot pinks, highly visual mathematical concept.*

---

## 1. Preparación Científica de Datos en Machine Learning (20 min)

### Explicación para instructor

Para construir un modelo predictivo, no podemos entrenar y evaluar el algoritmo en el mismo conjunto de datos (eso sería equivalente a darle las preguntas y respuestas del examen al alumno antes de estudiar).
- **División de datos:**
  - **Entrenamiento (Train):** Datos con los que el modelo aprende los patrones (típicamente 80%).
  - **Prueba (Test):** Datos ocultos que usaremos para validar si el modelo realmente sabe generalizar o si solo memorizó (típicamente 20%).
- **Escalado de características:**
  - Los algoritmos de ML son sensibles a las diferentes escalas. Si los metros cuadrados de una propiedad van de `50` a `220` y las recámaras van de `1` a `4`, el modelo creerá que los metros cuadrados son 50 veces más importantes solo por su magnitud numérica.
  - Con `StandardScaler` normalizamos los datos para que tengan una media de `0` y una desviación estándar de `1`.

#### Texto para una celda Markdown del notebook

## Preparación de Datos (Preprocessing)

- `train_test_split` de `sklearn.model_selection` divide el dataset de forma aleatoria en entrenamiento y prueba.
- `StandardScaler` de `sklearn.preprocessing` escala las características numéricas de la matriz $X$.

#### Código para una celda de Jupyter

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Carga de datos de propiedades de CDMX
df_casas = pd.read_csv("recursos/propiedades_cdmx.csv")

# 1. Definir X (features numéricas) e y (target: precio)
X = df_casas[["Metros_Cuadrados", "Recamaras", "Banos", "Estacionamientos", "Antiguedad_Anos"]]
y = df_casas["Precio_Millones_MXN"]

# 2. División Entrenamiento/Prueba (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# 3. Escalar características
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Aprende la media/std del entrenamiento y transforma
X_test_scaled = scaler.transform(X_test)        # Transforma el test con los mismos parámetros aprendidos

print(f"Dimensiones de entrenamiento (X_train): {X_train.shape}")
print(f"Dimensiones de prueba (X_test): {X_test.shape}")
```

#### Salida esperada

```text
Dimensiones de entrenamiento (X_train): (120, 5)
Dimensiones de prueba (X_test): (30, 5)
```

---

## 2. El Algoritmo de Regresión Lineal (15 min)

### Explicación para instructor

Explica visualmente el concepto de **Regresión Lineal**:
- Consiste en ajustar una línea recta (o un plano multidimensional) a los puntos de datos de tal forma que la distancia promedio entre los puntos reales y la línea sea la menor posible (método de Mínimos Cuadrados Ordinarios).
- La ecuación lineal es $y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + ...$ donde:
  - $\beta_0$ es el intercepto (el precio base si todas las características fueran cero).
  - $\beta_1, \beta_2$ son los coeficientes o pesos que indican el impacto de cada característica (ej. cuánto sube el precio por cada metro cuadrado adicional).

---

## 3. Entrenamiento y Predicción con Scikit-Learn (15 min)

### Explicación para instructor

Demuestra el flujo estándar de modelado de Scikit-Learn. Este flujo es consistente para casi cualquier algoritmo de la librería (regresión, árboles, redes neuronales):
1. **Instanciar:** Importar y crear el objeto del modelo: `modelo = LinearRegression()`.
2. **Entrenar (`.fit()`):** Ajustar los parámetros del modelo pasándole los datos de entrenamiento escalados y la variable objetivo: `modelo.fit(X_train_scaled, y_train)`.
3. **Predecir (`.predict()`):** Aplicar el modelo entrenado sobre nuevos datos para obtener estimaciones: `predicciones = modelo.predict(X_test_scaled)`.

#### Texto para una celda Markdown del notebook

## Entrenamiento y Predicción con Scikit-Learn

El flujo básico de modelado consiste en:
1. `modelo = LinearRegression()` (Instanciar)
2. `modelo.fit(X_train_scaled, y_train)` (Entrenar)
3. `modelo.predict(X_test_scaled)` (Predecir)

#### Código para una celda de Jupyter

```python
from sklearn.linear_model import LinearRegression

# 1. Instanciar el modelo
modelo_reg = LinearRegression()

# 2. Entrenar con datos de entrenamiento escalados
modelo_reg.fit(X_train_scaled, y_train)

# 3. Generar predicciones sobre el conjunto de prueba
y_pred = modelo_reg.predict(X_test_scaled)

print("¡Modelo entrenado y predicciones generadas con éxito!")
print("\nPrimeras 5 predicciones del modelo vs. Valores reales:")
for i in range(5):
    print(f"Predicción: ${y_pred[i]:.2f} M | Real: ${y_test.values[i]:.2f} M")
```

#### Salida esperada

```text
¡Modelo entrenado y predicciones generadas con éxito!

Primeras 5 predicciones del modelo vs. Valores reales:
Predicción: $4.52 M | Real: $4.18 M
Predicción: $6.12 M | Real: $6.50 M
Predicción: $2.14 M | Real: $1.90 M
...
```

---

## 4. Taller de Cierre: Prediciendo el precio de tu casa (10 min)

### Explicación para instructor

Pide al grupo que abra una celda de código nueva y utilice el scaler y modelo entrenado para estimar el precio de una vivienda ficticia.

#### Actividad para el alumno

Deseas calcular el precio aproximado en el mercado de una propiedad en la Ciudad de México con las siguientes características:
- Metros cuadrados: `110`
- Recámaras: `3`
- Baños: `2`
- Estacionamientos: `1`
- Antigüedad en años: `8`

Escribe un código que:
1. Cree un DataFrame de una sola fila con estas características (las columnas deben tener los mismos nombres exactos que la matriz $X$).
2. Escale esta fila utilizando el scaler previamente entrenado (`scaler.transform()`).
3. Prediga su valor de mercado en millones de pesos utilizando `modelo_reg.predict()`.

#### Código para el notebook

```python
# 1. Crear el DataFrame de la nueva propiedad
nueva_casa = pd.DataFrame([{
    "Metros_Cuadrados": 110.0,
    "Recamaras": 3,
    "Banos": 2,
    "Estacionamientos": 1,
    "Antiguedad_Anos": 8
}])

# 2. Escalar usando el mismo scaler
nueva_casa_scaled = scaler.transform(nueva_casa)

# 3. Predecir e imprimir
precio_estimado = modelo_reg.predict(nueva_casa_scaled)[0]
print(f"--- Valuación Predictiva ---")
print(f"Precio estimado de venta: ${precio_estimado:.2f} Millones de pesos MXN")
```

#### Salida esperada

```text
--- Valuación Predictiva ---
Precio estimado de venta: $3.45 Millones de pesos MXN (el valor exacto dependerá de la aleatoriedad inicial)
```

---

## Cierre de la sesión (2 min)

Recapitula brevemente:
Hoy entrenamos nuestro primer modelo de inteligencia artificial. Aprendimos el flujo de preparación científica dividiendo datos en entrenamiento/prueba con `train_test_split()`, normalizamos magnitudes con `StandardScaler()` y entrenamos y aplicamos una **Regresión Lineal** en Scikit-Learn.

En la siguiente sesión (Clase 14) aprenderemos a evaluar numéricamente el error de nuestra regresión (MSE, R²) y conoceremos los algoritmos de clasificación (como Regresión Logística y Árboles de Decisión) para predecir variables categóricas.
