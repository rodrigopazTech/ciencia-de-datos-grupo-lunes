# Clase 7: Introducción a Pandas & Estructura de DataFrames

**Duración sugerida:** 60 minutos  
**Modalidad:** práctica en Jupyter Lab  
**Objetivo:** que el alumnado comprenda la diferencia entre Series y DataFrames, aprenda a cargar un archivo CSV local empleando **Pandas** y realice un diagnóstico preliminar del dataset con `.head()`, `.shape`, `.info()` y `.describe()`.

---

### 🎨 Apoyo Visual para el Aprendizaje
* **Concepto:** Una Serie representada como una tira vertical de película de una sola columna, y el DataFrame como una hoja de cálculo completa flotante con etiquetas claras que marcan el "Index" (filas en el eje vertical) y las "Columns" (nombres de las columnas en el eje horizontal).
* **Prompt para Generar Imagen con IA (Midjourney/DALL-E 3):**
  > *A professional 3D infographic of a data table (DataFrame) floating in a digital space. Highlight a single vertical column (labeled 'Series') glowing in orange. Clearly show labeled axes: a vertical index (labeled 'Row Index') and horizontal headers (labeled 'Column Names'). Clean corporate design, high contrast, blue and white palette, isolated background.*

---

## 1. La herramienta reina del Científico de Datos: Pandas (15 min)

### Explicación para instructor

En la ciencia de datos, la gran mayoría de la información se organiza de forma tabular (en filas y columnas, como hojas de Excel o tablas de SQL).
- Aunque NumPy es muy rápido para operaciones matemáticas vectorizadas, no maneja bien columnas con diferentes tipos de datos (como una columna con texto y otra con números) ni etiquetas descriptivas de columnas.
- **Pandas** resuelve esto introduciendo dos estructuras fundamentales:
  - **Series:** una columna individual de datos con un índice.
  - **DataFrame:** una tabla de dos dimensiones con filas y columnas indexadas.
- Importamos Pandas usando la convención: `import pandas as pd`.

#### Texto para una celda Markdown del notebook

## Series y DataFrames en Pandas

Pandas es la biblioteca principal de Python para manipulación y análisis de datos.
- **Series:** Arreglo unidimensional con etiquetas (una sola columna).
- **DataFrame:** Estructura bidimensional de filas y columnas (una tabla).

#### Código para una celda de Jupyter

```python
import pandas as pd

# 1. Crear una Serie
temperaturas = pd.Series([22.5, 23.0, 24.5], index=["Lunes", "Martes", "Miércoles"])
print("--- Serie de Pandas ---")
print(temperaturas)

# 2. Crear un DataFrame manual
datos = {
    "Producto": ["Cafetera", "Laptop", "Teclado"],
    "Precio": [1500, 22000, 850]
}
df_manual = pd.DataFrame(datos)
print("\n--- DataFrame Manual ---")
print(df_manual)
```

#### Salida esperada

```text
--- Serie de Pandas ---
Lunes        22.5
Martes       23.0
Miércoles    24.5
dtype: float64

--- DataFrame Manual ---
   Producto  Precio
0  Cafetera    1500
1    Laptop   22000
2   Teclado     850
```

---

## 2. Ingesta de Datos (Data Ingestion) (20 min)

### Explicación para instructor

En el mundo real, los datos no se escriben manualmente en el código; se leen desde archivos externos.
- La función `pd.read_csv()` permite importar un archivo delimitado por comas (CSV) de forma instantánea convirtiéndolo en un DataFrame de Pandas.
- Mostraremos cómo leer el archivo local `ventas_ecommerce.csv` que preparamos en nuestra carpeta de recursos.
- También mostraremos cómo se podría leer directamente desde una URL pública (ej. GitHub Raw) en la nube, lo cual es muy útil para cuadernos compartidos.

#### Texto para una celda Markdown del notebook

## Carga de Archivos de Datos (Ingesta)

Cargamos archivos locales en formato CSV usando `pd.read_csv("ruta_del_archivo")`.

#### Código para una celda de Jupyter

```python
# Carga del dataset local de recursos
ruta_archivo = "recursos/ventas_ecommerce.csv"
df_ventas = pd.read_csv(ruta_archivo)

print("¡Dataset cargado con éxito!")
print("Tipo de objeto generado:", type(df_ventas))
```

#### Salida esperada

```text
¡Dataset cargado con éxito!
Tipo de objeto generado: <class 'pandas.core.frame.DataFrame'>
```

---

## 3. Diagnóstico de Salud de los Datos (15 min)

### Explicación para instructor

Una vez cargada la tabla, antes de realizar cualquier análisis o cálculo, el Científico de Datos debe realizar un diagnóstico de "salud" de la información:
- `.head(n)`: muestra las primeras `n` filas (por defecto 5). Es el primer vistazo de los datos.
- `.shape`: tupla que devuelve `(filas, columnas)`. Permite saber el volumen de información.
- `.info()`: muestra el resumen del esquema de la tabla (nombres de columnas, tipos de datos como `int64`, `float64` u `object` para texto, y si existen valores nulos/vacíos).
- `.describe()`: devuelve métricas estadísticas básicas (media, desviación estándar, mínimos, máximos) de las columnas numéricas.

#### Texto para una celda Markdown del notebook

## Diagnóstico Inicial de Datos

Utilizamos herramientas básicas para explorar el DataFrame:
- `.head()` y `.tail()` para previsualizar filas.
- `.shape` para el tamaño.
- `.info()` para tipos de datos y valores no nulos.
- `.describe()` para estadísticas rápidas.

#### Código para una celda de Jupyter

```python
# 1. Previsualizar las primeras 3 filas
print("--- Primeras 3 filas ---")
display(df_ventas.head(3))  # 'display' da formato de tabla en Jupyter

# 2. Conocer dimensiones
print(f"\nDimensiones (filas, columnas): {df_ventas.shape}")

# 3. Resumen estructural
print("\n--- Resumen Estructural info() ---")
df_ventas.info()

# 4. Estadísticas rápidas
print("\n--- Resumen Estadístico describe() ---")
display(df_ventas.describe())
```

#### Salida esperada (la salida de info mostrará tipos y no nulos)

```text
--- Primeras 3 filas ---
  ID_Pedido       Fecha             Ciudad    Categoria     Producto  Precio_Unitario  Cantidad        Metodo_Pago      Estado
0  PED_1000  2026-01-01   Ciudad de México     Hogar   Silla Ergonómica            4176         1  Tarjeta de Crédito  Completado
1  PED_1001  2026-01-01   Guadalajara      Juguetes   Muñeco de Acción             453         1              PayPal  Completado
2  PED_1002  2026-01-02   Monterrey       Deportes   Termo Deportivo             347         1            Efectivo  Completado

Dimensiones (filas, columnas): (205, 9)

--- Resumen Estructural info() ---
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 205 entries, 0 to 204
Data columns (total 9 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   ID_Pedido        205 non-null    object
 1   Fecha            205 non-null    object
 2   Ciudad           205 non-null    object
 3   Categoria        205 non-null    object
 4   Producto         205 non-null    object
 5   Precio_Unitario  205 non-null    int64 
 6   Cantidad         205 non-null    int64 
 7   Metodo_Pago      195 non-null    object
 8   Estado           197 non-null    object
dtypes: int64(2), object(7)
memory usage: 14.5+ KB

--- Resumen Estadístico describe() ---
(Tabla con count, mean, std, min, 25%, 50%, 75%, max para Precio_Unitario y Cantidad)
```

---

## 4. Taller de Cierre: Explorador de Diagnóstico (10 min)

### Explicación para instructor

Pide al grupo que abra una celda nueva y haga un diagnóstico de las columnas con problemas.
*Guía didáctica:* Haz notar a la clase que las columnas `Metodo_Pago` y `Estado` tienen menos de `205` registros no nulos. Esto revela que hay datos faltantes (nulos) que deberán limpiarse en la próxima clase.

#### Actividad para el alumno

Utilizando el DataFrame `df_ventas` cargado:
1. Muestra las últimas 5 filas del dataset usando `.tail()`.
2. Imprime de forma clara la cantidad de filas y la cantidad de columnas del dataset por separado, usando desempaquetado de tuplas de `.shape`.
3. Observando la salida de `.info()`, identifica qué columnas tienen valores nulos (conteo menor al total de filas) y escríbelas en una celda de texto.

#### Código para el notebook

```python
# 1. Previsualizar las últimas 5 filas
print("--- Últimos 5 registros ---")
display(df_ventas.tail(5))

# 2. Desempaquetado de dimensiones
filas, columnas = df_ventas.shape
print(f"\nEl dataset contiene {filas} filas y {columnas} columnas.")
```

#### Salida esperada

```text
--- Últimos 5 registros ---
    ID_Pedido       Fecha       Ciudad    Categoria           Producto  Precio_Unitario  Cantidad        Metodo_Pago      Estado
200  PED_1995  2026-06-29       Puebla     Deportes    Tapete de Yoga              519         1  Tarjeta de Crédito   Completado
201  PED_1996  2026-06-29  Guadalajara  Electrónica      Smartphone X            11942         1      Transferencia    Completado
202  PED_1997  2026-06-30    Monterrey     Deportes   Termo Deportivo              351         1            PayPal     Cancelado
203  PED_1998  2026-06-30    Monterrey        Hogar  Silla Ergonómica             4184         1            PayPal     Completado
204  PED_1999  2026-06-30       Puebla        Hogar   Aspiradora Robot             5579         1  Tarjeta de Crédito   Completado

El dataset contiene 205 filas y 9 columnas.
```

---

## Cierre de la sesión (2 min)

Recapitula brevemente:
Hoy aprendimos a estructurar datos tabulares usando **Series** y **DataFrames** en Pandas. Cargamos nuestro primer archivo CSV de e-commerce real y aprendimos a realizar un diagnóstico preliminar del volumen de registros y la calidad de las columnas mediante `.info()` y `.describe()`.

En la siguiente sesión (Clase 8) aprenderemos a resolver los problemas de salud encontrados, limpiando los valores nulos, eliminando duplicados e indexando y filtrando filas de interés mediante condicionales avanzados.
