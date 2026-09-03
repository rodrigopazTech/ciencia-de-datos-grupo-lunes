# Clase 11: Visualización Estadística con Seaborn y Análisis Exploratorio (EDA)

**Duración sugerida:** 60 minutos  
**Modalidad:** práctica en Jupyter Lab  
**Objetivo:** que el alumnado aprenda a utilizar la librería **Seaborn** para simplificar visualizaciones complejas (diagramas de dispersión, boxplots y mapas de calor), entienda e interprete la correlación numérica de Pearson y ejecute un Análisis Exploratorio de Datos (EDA) estructurado de inicio a fin.

---

### 🎨 Apoyo Visual para el Aprendizaje
* **Concepto:** Un diagrama tridimensional y educativo de un gráfico Boxplot diseccionado en el que se señala de forma clara la caja central que representa el "50% de los Datos", la línea gruesa de la "Mediana", los bigotes de los extremos y los valores atípicos representados como estrellas o esferas rojas alejadas etiquetadas como "Outliers".
* **Prompt para Generar Imagen con IA (Midjourney/DALL-E 3):**
  > *An educational 3D render explaining a Boxplot chart. The central box represents the '50% of Data', a bold central line represents the 'Median', the whiskers show the range, and outliers are depicted as glowing red dots floating far away labeled 'Outliers'. Bright educational theme, soft lighting, gray background.*

---

## 1. Seaborn: Gráficos Estadísticos Simplificados (15 min)

### Explicación para instructor

**Seaborn** es una biblioteca de visualización basada en Matplotlib que está diseñada específicamente para integrarse de forma nativa con los DataFrames de Pandas.
- A diferencia de Matplotlib, donde a veces hay que escribir muchas líneas de código para dar estilo o separar datos por colores, Seaborn lo hace de forma automática mediante el argumento `hue` (que colorea los elementos según una variable categórica).
- Importamos Seaborn usando: `import seaborn as sns`.
- Veremos dos gráficos clave:
  1. **Scatterplot (`sns.scatterplot()`):** Gráfico de dispersión para ver la relación entre dos números.
  2. **Boxplot (`sns.boxplot()`):** Diagrama de caja para comparar la distribución de precios o ventas entre categorías de productos. Permite ver la mediana, los cuartiles y los valores atípicos (*outliers*).

#### Texto para una celda Markdown del notebook

## Visualización Estadística con Seaborn

Seaborn facilita la creación de gráficos avanzados integrándose directamente con DataFrames:
- `sns.scatterplot(data, x, y, hue)`: Dispersión con codificación de colores.
- `sns.boxplot(data, x, y)`: Comparación de distribuciones (cajas y bigotes).

#### Código para una celda de Jupyter

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carga de datos
df_ventas = pd.read_csv("recursos/ventas_ecommerce.csv").dropna()
df_ventas["Monto_Total"] = df_ventas["Precio_Unitario"] * df_ventas["Cantidad"]

# Definir estilo visual de Seaborn por defecto
sns.set_theme(style="whitegrid")

# 1. Boxplot: Distribución de Precios Unitarios por Categoría
plt.figure(figsize=(10, 5))
sns.boxplot(data=df_ventas, x="Categoria", y="Precio_Unitario", palette="Set2")
plt.title("Distribución de Precios Unitarios por Categoría de Producto")
plt.show()

# 2. Scatterplot: Relación entre Precio Unitario y Cantidad vendida
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df_ventas, x="Precio_Unitario", y="Cantidad", hue="Categoria", s=80)
plt.title("Relación entre Precio Unitario y Cantidad de Productos")
plt.show()
```

#### Salida esperada

```text
(Se despliegan dos gráficos de alta calidad estética: un boxplot con paleta pastel Set2 mostrando rangos de precio por categoría y un gráfico de dispersión con puntos coloreados por categoría)
```

---

## 2. Correlaciones Numéricas y Mapas de Calor (15 min)

### Explicación para instructor

Explica qué es la **correlación de Pearson**:
- Es una medida estadística que indica la fuerza y la dirección de la relación lineal entre dos variables numéricas.
- Toma valores entre `-1` y `1`:
  - `1`: Relación lineal positiva perfecta (si una variable sube, la otra sube proporcionalmente).
  - `-1`: Relación lineal negativa perfecta (si una variable sube, la otra baja).
  - `0`: No existe relación lineal.
- Pandas permite calcular de forma rápida la matriz de correlación numérica con `.corr()`.
- Seaborn permite dibujar esta matriz mediante un mapa de calor (`sns.heatmap()`), facilitando la detección de relaciones visuales de forma inmediata.

#### Texto para una celda Markdown del notebook

## Correlación y Mapa de Calor (Heatmap)

- La correlación mide el grado de relación entre dos variables numéricas en un rango de `-1` a `1`.
- `df.corr(numeric_only=True)` calcula las correlaciones en Pandas.
- `sns.heatmap(matriz_corr, annot=True)` dibuja el mapa de calor con los valores numéricos correspondientes.

#### Código para una celda de Jupyter

```python
# 1. Calcular la matriz de correlación
matriz_corr = df_ventas[["Precio_Unitario", "Cantidad", "Monto_Total"]].corr()
print("--- Matriz de Correlación Numérica ---")
print(matriz_corr)

# 2. Dibujar el mapa de calor
plt.figure(figsize=(6, 4))
sns.heatmap(matriz_corr, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f")
plt.title("Mapa de Calor de Correlaciones")
plt.show()
```

#### Salida esperada

```text
--- Matriz de Correlación Numérica ---
                 Precio_Unitario  Cantidad  Monto_Total
Precio_Unitario         1.000000 -0.063251     0.972348
Cantidad               -0.063251  1.000000     0.112341
Monto_Total             0.972348  0.112341     1.000000

(Se despliega un mapa de calor coloreado de azul a rojo. Muestra una fuerte correlación positiva de 0.97 entre Precio_Unitario y Monto_Total, y una correlación casi nula de -0.06 entre Precio_Unitario y Cantidad)
```

---

## 3. El Método del Científico de Datos: EDA Completo (15 min)

### Explicación para instructor

Explica al grupo que el **EDA** (Exploratory Data Analysis) es la fase fundamental del flujo de trabajo en la que un Científico de Datos interroga al dataset usando Pandas y gráficos para:
1. Validar la estructura y calidad de los datos (nulos, tipos de datos).
2. Comprender la distribución de las variables individuales.
3. Buscar patrones, relaciones y correlaciones lógicas o de negocio.
4. Identificar anomalías o valores atípicos que requieran ser tratados antes de entrenar un modelo predictivo de Machine Learning.

Presenta el EDA como el diagnóstico médico de un dataset antes de formular el tratamiento.

---

## 4. Taller de Cierre: EDA Exprés de Ventas (15 min)

### Explicación para instructor

Pide al grupo que abra una celda de código y ejecute los tres pasos clásicos del EDA sobre las variables del dataset.

#### Actividad para el alumno

Ejecuta el siguiente bloque de código para culminar tu Análisis Exploratorio del dataset de e-commerce:
1. Genera un gráfico de boxplot utilizando Seaborn para comparar el `Monto_Total` de las ventas en cada una de las diferentes `Ciudades` mexicanas.
2. Analiza visualmente si existen ciudades con ventas que destaquen o muestren distribuciones de ingresos significativamente diferentes.
3. Documenta en una celda de texto un hallazgo rápido de valor obtenido de tus visualizaciones (ej. si la correlación entre variables tiene sentido de negocio o si una categoría de productos domina los ingresos).

#### Código para el notebook

```python
# 1. Crear el boxplot por ciudades
plt.figure(figsize=(10, 5))
sns.boxplot(data=df_ventas, x="Ciudad", y="Monto_Total", palette="Pastel1")
plt.title("Distribución de Montos de Venta por Ciudad", fontsize=13, fontweight="bold")
plt.xlabel("Ciudades", fontsize=11)
plt.ylabel("Monto de Venta ($ MXN)", fontsize=11)
plt.show()
```

#### Salida esperada

```text
(Se despliega el gráfico de caja comparativo de montos de venta por ciudad. Las distribuciones se verán similares debido a la generación aleatoria homogénea, pero es excelente para consolidar la sintaxis de boxplot)
```

---

## Cierre de la sesión (2 min)

Recapitula brevemente:
Hoy dominamos la graficación avanzada usando **Seaborn**. Aprendimos a construir diagramas de caja, gráficos de dispersión y mapas de calor de correlación. Cerramos el módulo de visualización y análisis unificando todo en un Análisis Exploratorio de Datos (EDA) completo.

En la siguiente sesión (Clase 12) iniciaremos el último módulo del curso, conectando las métricas estadísticas descriptivas del EDA con la teoría y fundamentos lógicos de la inteligencia artificial y el **Machine Learning**.
