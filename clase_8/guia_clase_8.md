# Clase 8: Limpieza y Filtrado de Datos con Pandas

**Duración sugerida:** 60 minutos  
**Modalidad:** práctica en Jupyter Lab  
**Objetivo:** que el alumnado aprenda a depurar datos inconsistentes eliminando filas duplicadas, imputando valores nulos con `.fillna()` y seleccionando y filtrando filas y columnas utilizando `.loc[]` e `.iloc[]`.

---

### 🎨 Apoyo Visual para el Aprendizaje
* **Concepto:** Una aspiradora robótica succionando celdas que contienen filas duplicadas, un pincel digital rellenando celdas vacías (`NaN`) con valores por defecto e iluminándolas en verde, y una gran lupa de precisión que selecciona y aísla una sección específica de la tabla de base de datos (filtro `.loc`).
* **Prompt para Generar Imagen con IA (Midjourney/DALL-E 3):**
  > *A high-tech digital cleaning station for data. A robotic vacuum cleaner cleaning up duplicate icons, a glowing digital brush painting missing database cells (labeled 'NaN') with green values, and a large glowing magnifying glass isolating a specific row (labeled '.loc filter'). Futuristic vector infographic style, clean and bright.*

---

## 1. Tratamiento de Valores Faltantes (Nulos) (20 min)

### Explicación para instructor

En el análisis de datos del mundo real, los datasets casi nunca vienen perfectos.
- La ausencia de información se representa en Pandas como `NaN` (Not a Number) o `None`.
- Para saber cuántos valores nulos tiene cada columna, encadenamos `.isna().sum()`.
- Contamos con dos estrategias principales de limpieza:
  1. **Eliminar:** Si la columna con nulos es la variable crítica del análisis, eliminamos las filas afectadas con `.dropna()`.
  2. **Imputar (Rellenar):** Si no queremos perder registros útiles, rellenamos las celdas vacías con un valor constante o estadístico usando `.fillna()`.

#### Texto para una celda Markdown del notebook

## Tratamiento de Valores Nulos

- `df.isna().sum()` muestra el conteo de valores nulos por columna.
- `df.dropna()` elimina filas que contengan valores vacíos.
- `df.fillna(valor)` reemplaza las celdas vacías por el valor indicado.

#### Código para una celda de Jupyter

```python
import pandas as pd

df_ventas = pd.read_csv("recursos/ventas_ecommerce.csv")

# 1. Identificar nulos
print("--- Conteo de nulos por columna ---")
print(df_ventas.isna().sum())

# 2. Imputar nulos en la columna Metodo_Pago
# Usamos inplace=True para aplicar el cambio directamente al DataFrame original
df_ventas["Metodo_Pago"] = df_ventas["Metodo_Pago"].fillna("No Especificado")

# 3. Eliminar filas con nulos restantes (en la columna Estado)
df_limpio = df_ventas.dropna(subset=["Estado"])

print("\n--- Conteo de nulos después de la limpieza ---")
print(df_limpio.isna().sum())
```

#### Salida esperada

```text
--- Conteo de nulos por columna ---
ID_Pedido           0
Fecha               0
Ciudad              0
Categoria           0
Producto            0
Precio_Unitario     0
Cantidad            0
Metodo_Pago        10
Estado              8
dtype: int64

--- Conteo de nulos después de la limpieza ---
ID_Pedido          0
Fecha              0
Ciudad             0
Categoria          0
Producto           0
Precio_Unitario    0
Cantidad           0
Metodo_Pago        0
Estado             0
dtype: int64
```

---

## 2. Eliminar Duplicados (10 min)

### Explicación para instructor

Los duplicados ocurren por fallas en sistemas de guardado de datos o ingestas dobles.
- El método `.drop_duplicates()` elimina filas idénticas, dejando solo la primera aparición.
- Mostraremos la diferencia en las dimensiones (`.shape`) del DataFrame antes y después de quitar los registros duplicados que insertamos intencionalmente en el script de generación.

#### Texto para una celda Markdown del notebook

## Eliminar Registros Duplicados

- `.duplicated().sum()` cuenta cuántas filas repetidas existen en el dataset.
- `.drop_duplicates(inplace=True)` elimina las filas duplicadas.

#### Código para una celda de Jupyter

```python
print(f"Dimensiones originales antes de duplicados: {df_limpio.shape}")
print(f"Cantidad de filas duplicadas: {df_limpio.duplicated().sum()}")

# Eliminar duplicados
df_sin_duplicados = df_limpio.drop_duplicates()
print(f"Dimensiones finales sin duplicados: {df_sin_duplicados.shape}")
```

#### Salida esperada

```text
Dimensiones originales antes de duplicados: (197, 9)
Cantidad de filas duplicadas: 5
Dimensiones finales sin duplicados: (192, 9)
```

---

## 3. Selección y Filtrado con `.loc[]` e `.iloc[]` (20 min)

### Explicación para instructor

Pandas provee dos indexadores fundamentales para extraer subconjuntos de datos de forma profesional:
- `.loc[filas, columnas]`: busca por **nombre o etiqueta**.
- `.iloc[filas, columnas]`: busca por **posición numérica entera** (indexación por posición).

También enseñaremos cómo hacer **filtrado condicional** (máscaras lógicas) pasando una condición directamente entre corchetes, lo cual es equivalente a la indexación booleana de NumPy.

#### Texto para una celda Markdown del notebook

## Segmentación y Selección de Datos

- `df.loc[filas_etiquetas, columnas_nombres]` selecciona por nombre de etiqueta.
- `df.iloc[filas_posiciones, columnas_posiciones]` selecciona por posición numérica.
- `df[df["Columna"] == "Valor"]` filtra las filas que cumplen la condición.

#### Código para una celda de Jupyter

```python
# 1. Uso de .iloc: Seleccionar las primeras 3 filas y las primeras 4 columnas
print("--- Selección por posición (.iloc) ---")
display(df_sin_duplicados.iloc[0:3, 0:4])

# 2. Uso de .loc: Seleccionar filas específicas y las columnas ID_Pedido y Producto
print("\n--- Selección por etiquetas (.loc) ---")
display(df_sin_duplicados.loc[0:2, ["ID_Pedido", "Producto"]])

# 3. Filtrado condicional: Ventas realizadas en Monterrey
print("\n--- Ventas en Monterrey ---")
ventas_mty = df_sin_duplicados[df_sin_duplicados["Ciudad"] == "Monterrey"]
display(ventas_mty.head(3))
```

#### Salida esperada

```text
--- Selección por posición (.iloc) ---
(Tabla con filas de índice 0 a 2 y columnas ID_Pedido, Fecha, Ciudad, Categoria)

--- Selección por etiquetas (.loc) ---
(Tabla con columnas ID_Pedido y Producto para filas indexadas como 0, 1 y 2)

--- Ventas en Monterrey ---
(Tabla filtrada mostrando únicamente ventas de la ciudad de Monterrey)
```

---

## 4. Taller de Cierre: Filtro de Clientes y Ventas Altas (10 min)

### Explicación para instructor

Pide al grupo que abra una celda y resuelva un problema integrador de depuración y filtrado de datos e-commerce.

#### Actividad para el alumno

Utilizando el DataFrame `df_sin_duplicados` que acabamos de limpiar de nulos y duplicados:
1. Crea un filtro condicional utilizando `.loc` para extraer todas las filas donde la columna `Categoria` sea `"Electrónica"` **Y** el `Precio_Unitario` sea mayor o igual a `10000`.
2. Muestra únicamente las columnas `ID_Pedido`, `Producto` y `Precio_Unitario` del subconjunto filtrado.
3. Imprime cuántos registros cumplen con esta condición usando la propiedad `.shape`.

#### Código para el notebook

```python
# Aplicar filtros lógicos combinados (usando el operador '&' para el AND de Pandas)
filtro_electronica_cara = df_sin_duplicados.loc[
    (df_sin_duplicados["Categoria"] == "Electrónica") & (df_sin_duplicados["Precio_Unitario"] >= 10000),
    ["ID_Pedido", "Producto", "Precio_Unitario"]
]

print("--- Electrónica de Alta Gama ---")
display(filtro_electronica_cara)
print(f"Registros encontrados: {filtro_electronica_cara.shape[0]}")
```

#### Salida esperada

```text
--- Electrónica de Alta Gama ---
     ID_Pedido      Producto  Precio_Unitario
7     PED_1007  Smartphone X            11425
11    PED_1011    Laptop Pro            21971
18    PED_1018    Laptop Pro            21867
...
Registros encontrados: 32 (el número exacto dependerá de la generación aleatoria)
```

---

## Cierre de la sesión (2 min)

Recapitula de forma rápida:
Hoy limpiamos de forma completa nuestro dataset de ventas. Aprendimos a rellenar celdas vacías con `.fillna()`, a eliminar registros nulos con `.dropna()`, a limpiar duplicados con `.drop_duplicates()` y a segmentar y filtrar de forma condicional con `.loc[]` y `.iloc[]`.

En la siguiente sesión (Clase 9) completaremos nuestro dominio de la manipulación de tablas aprendiendo a crear columnas derivadas mediante transformaciones, agrupar datos por categorías con `.groupby()` y unir múltiples tablas del negocio.
