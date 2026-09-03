# Clase 15: Taller del Proyecto Final Aplicado

**Duración sugerida:** 60 minutos  
**Modalidad:** práctica e integradora en Jupyter Lab  
**Objetivo:** que el alumnado integre todas las habilidades adquiridas en el curso (Pandas, Matplotlib, Seaborn y Scikit-Learn) desarrollando un proyecto completo de fin a fin: ingesta de datos de viviendas de CDMX, limpieza, análisis visual, modelado y predicción del precio del mercado.

---

### 🎨 Apoyo Visual para el Aprendizaje
* **Concepto:** Mapa de ruta de un pipeline de datos en 3D isométrico: el flujo de datos arranca con el skyline de la CDMX, pasa por una lavadora digital (limpieza de datos), se conecta a un tablero con gráficas (EDA), y termina alimentando a una calculadora digital que muestra el precio de mercado final de una vivienda.
* **Prompt para Generar Imagen con IA (Midjourney/DALL-E 3):**
  > *A beautiful 3D isometric roadmap showing a data pipeline. A pipeline starts from a CDMX city skyline, passes through a washing machine (labeled 'Data Cleaning'), then through a visual dashboard with charts (labeled 'EDA'), and finally feeds into a digital calculator showing property valuations. Professional, sleek, modern layout.*

---

## 1. Planteamiento del Reto e Ingesta de Datos (10 min)

### Explicación para instructor

Hoy es el taller del **Proyecto Final**. Los alumnos dejarán de ver temas nuevos y aplicarán de forma secuencial todo lo aprendido.
- **Contexto de negocio:** Actuamos como consultores de datos para una plataforma de tecnología inmobiliaria (PropTech) que busca automatizar las valuaciones de casas y departamentos en la CDMX para agilizar sus ofertas.
- El archivo de datos a analizar es `propiedades_cdmx.csv` ubicado en la carpeta de recursos.

#### Texto para una celda Markdown del notebook

# Proyecto Final: Valuador Predictivo de Propiedades CDMX

Desarrollamos el pipeline completo de ciencia de datos:
1. Ingesta de Datos (Pandas)
2. Limpieza e Inspección
3. Análisis Exploratorio Visual (Seaborn y Matplotlib)
4. Modelado Predictivo (Scikit-Learn)
5. Evaluación del Modelo

#### Código para una celda de Jupyter

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Ingesta
df_casas = pd.read_csv("recursos/propiedades_cdmx.csv")
print("Dimensiones del dataset:", df_casas.shape)
display(df_casas.head(3))
```

#### Salida esperada

```text
Dimensiones del dataset: (150, 7)
   Alcaldia  Metros_Cuadrados  Recamaras  Banos  Estacionamientos  Antiguedad_Anos  Precio_Millones_MXN
0  Cuauhtémoc              84.5          2      1                 1               15                 2.85
1  Miguel Hidalgo             120.0          3      2                 2                5                 6.20
...
```

---

## 2. Limpieza y Análisis Exploratorio de Datos (EDA) (20 min)

### Explicación para instructor

Insta a los alumnos a revisar la salud de la tabla y a realizar análisis gráficos:
- Revisar nulos (`.isna().sum()`).
- Mostrar la distribución de precios (`sns.histplot` o `sns.boxplot`).
- Graficar la relación entre Metros Cuadrados y Precio con un Scatterplot, coloreando por Alcaldía. Esto mostrará visualmente cómo la ubicación influye en el valor del metro cuadrado.

#### Texto para una celda Markdown del notebook

## Paso 2: Limpieza y Visualización (EDA)

Evaluamos nulos y graficamos la distribución y relaciones de las viviendas.

#### Código para una celda de Jupyter

```python
# 1. Validación de nulos
print("Valores nulos en el dataset:")
print(df_casas.isna().sum())

# 2. Distribución de precios por Alcaldía
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 5))
sns.boxplot(data=df_casas, x="Alcaldia", y="Precio_Millones_MXN", palette="Set3")
plt.title("Distribución de Precios de Propiedades por Alcaldía de CDMX", fontsize=12)
plt.show()

# 3. Dispersión: Metros Cuadrados vs. Precio por Alcaldía
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df_casas, x="Metros_Cuadrados", y="Precio_Millones_MXN", hue="Alcaldia", s=70)
plt.title("Relación entre Metros Cuadrados y Precio de Venta", fontsize=12)
plt.show()
```

#### Salida esperada

```text
Valores nulos en el dataset:
Alcaldia               0
Metros_Cuadrados       0
...
(Se despliegan dos gráficos: un boxplot que muestra precios mayores en alcaldías premium como Miguel Hidalgo y un gráfico de dispersión con una marcada tendencia positiva ascendente)
```

---

## 3. Preparación y Modelado Predictivo (20 min)

### Explicación para instructor

Guía al grupo en el modelado.
*Nota de nivelación:* Dado que la columna `Alcaldia` es de tipo texto, explicaremos brevemente que no se puede pasar a una regresión lineal matemática de Scikit-Learn directamente. Para simplificar el proyecto de hoy y mantenerlo amigable al nivel introductorio, entrenaremos el modelo utilizando únicamente las características puramente numéricas: `["Metros_Cuadrados", "Recamaras", "Banos", "Estacionamientos", "Antiguedad_Anos"]`.

#### Texto para una celda Markdown del notebook

## Paso 3: Modelado de Regresión con Scikit-Learn

Dividimos, normalizamos con StandardScaler y entrenamos el modelo de Regresión Lineal.

#### Código para una celda de Jupyter

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Definir X (features numéricas) e y
features = ["Metros_Cuadrados", "Recamaras", "Banos", "Estacionamientos", "Antiguedad_Anos"]
X = df_casas[features]
y = df_casas["Precio_Millones_MXN"]

# 2. Partición Científica (80% Train, 20% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# 3. Escalado
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Ajustar modelo
modelo_validador = LinearRegression()
modelo_validador.fit(X_train_scaled, y_train)

# 5. Generar predicciones
y_pred = modelo_validador.predict(X_test_scaled)

# 6. Evaluación de error
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print(f"Precisión del Valuador (R2 Coeficiente): {r2:.4f}")
print(f"Error Cuadrático Medio (MSE): {mse:.4f}")
```

#### Salida esperada

```text
Precisión del Valuador (R2 Coeficiente): 0.8845 (aproximadamente)
Error Cuadrático Medio (MSE): 0.1852 (aproximadamente)
```

---

## 4. Taller de Cierre: Valuación del Negocio (10 min)

### Explicación para instructor

Pide al grupo que debata sobre la utilidad de este valuador para una inmobiliaria.
Hagan los siguientes cálculos interpretativos:
- Muestren los coeficientes asociados a cada variable (`modelo_validador.coef_`).
- Expliquen que la característica de Metros Cuadrados tiene el peso más alto en la predicción.

#### Código para una celda de Jupyter

```python
# Mostrar la importancia de cada característica numérica según los coeficientes
importancia = pd.DataFrame({
    "Característica": features,
    "Coeficiente_Importancia": modelo_validador.coef_
})

print("--- Importancia de Variables en la Valuación ---")
print(importancia.sort_values(by="Coeficiente_Importancia", ascending=False))
```

#### Salida esperada

```text
--- Importancia de Variables en la Valuación ---
     Característica  Coeficiente_Importancia
0  Metros_Cuadrados                  1.350124
2             Banos                  0.280145
3  Estacionamientos                  0.210452
1         Recamaras                  0.150421
4   Antiguedad_Anos                 -0.120542
```

---

## Cierre de la sesión (2 min)

Recapitula brevemente:
¡Muchas felicidades a todo el grupo! Desarrollaron un proyecto de ciencia de datos completo e integrado. Importamos, limpiamos, exploramos visualmente correlaciones complejas y construimos un algoritmo con una precisión que ronda el 88% para valuar propiedades de forma automática en la CDMX.

En la última sesión (Clase 16) realizaremos la presentación de conclusiones de sus análisis, revisaremos mejores prácticas para armar su portafolio profesional en GitHub y delinearemos la ruta de aprendizaje recomendada para continuar su formación.
