# Clase 12: Estadística Descriptiva e Introducción a Machine Learning

**Duración sugerida:** 60 minutos  
**Modalidad:** teórica y conceptual, apoyada con scripts ilustrativos en Jupyter Lab  
**Objetivo:** que el alumnado comprenda la conexión de la estadística descriptiva (promedio, desviación estándar y sesgo) con los algoritmos predictivos, domine los conceptos de aprendizaje supervisado/no supervisado y sepa estructurar la matriz de características ($X$) y el vector objetivo ($y$) de un dataset para entrenamiento.

---

### 🎨 Apoyo Visual para el Aprendizaje
* **Concepto:** Comparativa del cambio de paradigma en la programación. Ruta 1 (Programación Clásica): Reglas manuales (engranes) y Datos de entrada generan Respuestas. Ruta 2 (Machine Learning): Datos de entrada e Historias de respuestas entran a un servidor informático, el cual genera automáticamente una llave brillante (las Reglas o Modelo predictivo).
* **Prompt para Generar Imagen con IA (Midjourney/DALL-E 3):**
  > *A comparative infographic. Top path: raw data and a manual cogwheel machine (labeled 'Rules') produce answers (labeled 'Classic Programming'). Bottom path: raw data and answers enter a computer server, which outputs a glowing key (labeled 'Rules/Model'). Sleek vector graphic, technical illustration style.*

---

## 1. Puentes Estadísticos hacia el Machine Learning (15 min)

### Explicación para instructor

Comienza la clase explicando que la inteligencia artificial no es "magia", sino estadística aplicada ejecutada a gran velocidad:
- En las clases de Pandas y visualización calculamos la media (`mean`) y desviación estándar (`std`).
- En Machine Learning, estos conceptos nos indican el comportamiento básico de los datos:
  - **Media vs. Mediana:** Si la media de ingresos es muy superior a la mediana, significa que hay un sesgo positivo provocado por unos pocos clientes de muy altos ingresos (valores atípicos u *outliers*).
  - **Desviación Estándar:** Mide la dispersión. Si un sensor de temperatura tiene una desviación alta, sus lecturas son inestables, lo cual dificulta la predicción de fallas.

#### Texto para una celda Markdown del notebook

## Estadística Descriptiva y Sesgo

Antes de entrenar un modelo, examinamos la dispersión y la simetría de los datos.
- **Outliers:** Valores extremos que inflan la media.
- **Desviación Estándar:** Cuantifica la variabilidad o incertidumbre de los datos.

#### Código para una celda de Jupyter

```python
import pandas as pd
import numpy as np

# Simular salarios de 10 personas comunes ($15k a $20k) y un millonario ($1,000,000)
salarios = [16000, 18000, 15500, 19000, 17500, 16500, 18500, 17000, 16000, 18000, 1000000]

df_salarios = pd.DataFrame(salarios, columns=["Salario_Mensual"])

print("Media de salarios:", df_salarios["Salario_Mensual"].mean())
print("Mediana de salarios:", df_salarios["Salario_Mensual"].median())
print("Desviación estándar:", df_salarios["Salario_Mensual"].std())
```

#### Salida esperada

```text
Media de salarios: 106500.0
Mediana de salarios: 17500.0
Desviación estándar: 296291.2418550439
```

> **Pregunta para reflexionar:** Si tuvieras que estimar el salario de un nuevo empleado promedio en esta empresa, ¿usarías la media o la mediana? *(Respuesta: La mediana, ya que la media está distorsionada por el outlier).*

---

## 2. Paradigmas del Aprendizaje Automático (20 min)

### Explicación para instructor

Explica el cambio de paradigma de programación clásica a Machine Learning:
- **Programación tradicional:** Escribimos reglas condicionales rígidas (`if ingresos > 25000: aprobar`). Si las reglas cambian, debemos reescribir el código a mano.
- **Machine Learning:** Alimentamos al algoritmo con datos y respuestas históricas (ej. perfiles de clientes pasados y si pagaron o no). El algoritmo aprende las reglas óptimas automáticamente y genera un *modelo* predictivo.

Diferencia los dos tipos de aprendizaje:
1. **Supervisado:** Contamos con datos etiquetados (tenemos la variable a predecir, la respuesta histórica).
   - **Regresión:** Queremos predecir un número continuo (ej. precio de una casa, demanda de producto, ventas del mes).
   - **Clasificación:** Queremos predecir una categoría o etiqueta (ej. si una transacción es fraude o no, si un correo es spam o no).
2. **No Supervisado:** No hay etiquetas. Buscamos patrones de similitud (ej. segmentar clientes en grupos homogéneos para marketing).

---

## 3. Representación de Datos en ML: Matriz $X$ y Vector $y$ (15 min)

### Explicación para instructor

Para que una librería de Machine Learning en Python (como Scikit-Learn) pueda procesar y entrenar un modelo, debemos separar los datos en dos estructuras estrictas:
1. **Características ($X$):** Las variables que usaremos para realizar la predicción. Se representa con la letra $X$ en mayúscula porque es una matriz bidimensional (varias filas y columnas).
2. **Variable Objetivo ($y$):** La variable que deseamos predecir. Se representa con la letra $y$ en minúscula porque es un vector de una sola dimensión (una sola columna).

Por ejemplo, si queremos predecir el **Precio** de una casa basándonos en sus **Metros Cuadrados** y **Recámaras**:
- $X$: Las columnas `["Metros_Cuadrados", "Recamaras"]`.
- $y$: La columna `Precio`.

#### Texto para una celda Markdown del notebook

## Anatomía de los Datos en Machine Learning

Antes de entrenar un modelo predictivo, dividimos nuestro dataset en:
- **$X$ (Matriz de Características / Features):** Variables predictoras independientes (columnas descriptoras).
- **$y$ (Vector Objetivo / Target):** La columna con la variable dependiente que queremos estimar.

#### Código para una celda de Jupyter

```python
# Simulando un dataset de propiedades
datos_casas = {
    "Metros_Cuadrados": [80, 120, 150],
    "Recamaras": [2, 3, 3],
    "Antiguedad": [5, 10, 2],
    "Precio_Millones": [2.1, 3.5, 4.8]
}
df_casas = pd.DataFrame(datos_casas)

# 1. Separar en X (Features) e y (Target)
X = df_casas[["Metros_Cuadrados", "Recamaras", "Antiguedad"]]
y = df_casas["Precio_Millones"]

print("--- Matriz de Características X (Features) ---")
display(X)

print("\n--- Vector Objetivo y (Target) ---")
print(y)
```

#### Salida esperada

```text
--- Matriz de Características X (Features) ---
   Metros_Cuadrados  Recamaras  Antiguedad
0                80          2           5
1               120          3          10
2               150          3           2

--- Vector Objetivo y (Target) ---
0    2.1
1    3.5
2    4.8
Name: Precio_Millones, dtype: float64
```

---

## 4. Taller de Cierre: Diseño de Modelado (10 min)

### Explicación para instructor

Pide al grupo que abra una celda de texto y realice una modelación mental de un problema de negocios sobre su dataset de e-commerce.

#### Actividad para el alumno

Analiza la estructura del dataset de e-commerce `df_ventas` y plantea dos problemas de Machine Learning que resuelvan necesidades de negocio reales:
1. **Caso 1 (Regresión):** Deseas estimar cuántos artículos (`Cantidad`) comprará un cliente. ¿Cuál sería la variable objetivo ($y$) y qué columnas usarías como características ($X$)?
2. **Caso 2 (Clasificación):** Deseas predecir si un pedido será cancelado (`Estado == "Cancelado"`). ¿Cuál sería la variable objetivo ($y$) y qué columnas usarías como características ($X$)?

Redacta tu propuesta en una celda de texto de forma estructurada.

#### Ejemplo de solución (para el instructor)

```text
Caso 1: Regresión (Cantidad a comprar)
- Variable objetivo (y): Cantidad (es una variable numérica continua).
- Características (X): Precio_Unitario, Categoria, Ciudad, Metodo_Pago.

Caso 2: Clasificación (Cancelación de pedido)
- Variable objetivo (y): Estado (representa categorías discretas: Completado, Pendiente, Cancelado).
- Características (X): Precio_Unitario, Cantidad, Categoria, Ciudad, Metodo_Pago.
```

---

## Cierre de la sesión (2 min)

Recapitula brevemente:
Hoy sentamos las bases de la inteligencia artificial. Conectamos la estadística descriptiva con el modelado, entendimos el cambio de paradigma al Machine Learning y aprendimos a separar nuestros conjuntos de datos en características ($X$) y variable objetivo ($y$).

En la siguiente sesión (Clase 13) programaremos nuestro primer algoritmo predictivo de regresión utilizando la librería estándar **Scikit-Learn** para predecir precios de propiedades locales.
