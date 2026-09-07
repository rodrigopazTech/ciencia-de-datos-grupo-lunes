# 🎯 Plan de Clase: Continuación Clase 8 (Limpieza, Filtrado Avanzado & Preparación a Pandas 9)

**Grupo:** Jueves - Ciencia de Datos (`26-1 Ciencia de Datos`)  
**Fecha:** Próximo Jueves  
**Duración:** 60 minutos  
**Objetivo de la Sesión:** Completar la **Clase 8 del temario oficial** (tratamiento de valores nulos, eliminación de duplicados y filtrado condicional avanzado con `.loc[]` e `.iloc[]`) para dejar al grupo 100% listo para iniciar la Clase 9 (*groupby*, transformaciones y uniones).

---

## ⏱️ Estructura y Cronograma de la Clase (60 Min)

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 1. Recapitulación Breve (5 min)                                        │
│    - Repaso de la diferencia entre .loc[] (etiquetas) e .iloc[] (números)│
├─────────────────────────────────────────────────────────────────────────┤
│ 2. Bloque 1: Tratamiento de Valores Nulos (15 min)                      │
│    - Conteo (.isna().sum()), Eliminación (.dropna()) e Imputación       │
│      (.fillna())                                                        │
├─────────────────────────────────────────────────────────────────────────┤
│ 3. Bloque 2: Eliminación de Duplicados (10 min)                         │
│    - Detección (.duplicated().sum()) y Limpieza (.drop_duplicates())    │
├─────────────────────────────────────────────────────────────────────────┤
│ 4. Bloque 3: Filtrado Condicional Complejo con .loc[] (20 min)          │
│    - Condiciones compuestas (&, |) y selección de columnas específicas   │
├─────────────────────────────────────────────────────────────────────────┤
│ 5. Taller Práctico de Cierre & Puente a Clase 9 (10 min)                │
│    - Ejercicio integrador y vista previa de .groupby()                 │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 📝 Guión y Guía Paso a Paso para el Instructor

### 1. Recapitulación (5 min)
* **Mensaje clave:** *"En la clase pasada aprendimos a crear DataFrames y a movernos por ellos usando `.loc` (por nombre de fila/columna) e `.iloc` (por posición numéricas). Hoy completaremos la limpieza profesional de datos reales para poder analizarlos la siguiente semana."*

---

### 2. Bloque 1: Tratamiento de Valores Nulos (15 min)

#### Explicación:
* Los datos reales vienen con huecos (`NaN` o `None`).
* Estrategias:
  1. **Diagnóstico:** `df.isna().sum()` muestra cuántos nulos hay por columna.
  2. **Imputación:** Rellenar celdas vacías con un valor por defecto o promedio mediante `df["Columna"].fillna(valor)`.
  3. **Eliminación:** Eliminar filas donde la información faltante es crítica mediante `df.dropna(subset=["Columna"])`.

#### Código para el Jupyter Notebook:
```python
import pandas as pd

# Cargar dataset de ventas e-commerce
df_ventas = pd.read_csv("recursos/ventas_ecommerce.csv")

# 1. Diagnóstico de nulos
print("--- Diagnóstico de valores nulos ---")
print(df_ventas.isna().sum())

# 2. Imputación (Rellenar método de pago vacíos con 'No Especificado')
df_ventas["Metodo_Pago"] = df_ventas["Metodo_Pago"].fillna("No Especificado")

# 3. Eliminación de filas con Estado nulo
df_limpio = df_ventas.dropna(subset=["Estado"])

print("\n--- Nulos después de la limpieza ---")
print(df_limpio.isna().sum())
```

---

### 3. Bloque 2: Eliminación de Duplicados (10 min)

#### Explicación:
* Las ingestas de bases de datos o sistemas de punto de venta a menudo duplican registros por errores de red.
* `.duplicated().sum()` nos dice cuántas filas son exactamente iguales.
* `.drop_duplicates(inplace=True)` elimina los registros repetidos dejando solo una copia.

#### Código para el Jupyter Notebook:
```python
print(f"Dimensiones iniciales del dataset: {df_limpio.shape}")
print(f"Número de filas duplicadas: {df_limpio.duplicated().sum()}")

# Eliminar filas duplicadas
df_sin_duplicados = df_limpio.drop_duplicates()
print(f"Dimensiones finales sin duplicados: {df_sin_duplicados.shape}")
```

---

### 4. Bloque 3: Filtrado Condicional Complejo con `.loc[]` (20 min)

#### Explicación:
* Para responder preguntas de negocio como *"¿Cuáles son las ventas de Electrónica mayores a $10,000 en Monterrey?"*, combinamos filtros lógicos con `.loc[]`.
* **Regla importante en Pandas:**
  * Usar `&` para el operador **AND** (ambas condiciones deben cumplirse).
  * Usar `|` para el operador **OR** (al menos una condición).
  * Encerrar siempre cada condición entre paréntesis `(condicion1) & (condicion2)`.

#### Código para el Jupyter Notebook:
```python
# Filtrar Electrónica con Precio >= 10,000 mostrando sólo ciertas columnas
filtro_alta_gama = df_sin_duplicados.loc[
    (df_sin_duplicados["Categoria"] == "Electrónica") & (df_sin_duplicados["Precio_Unitario"] >= 10000),
    ["ID_Pedido", "Producto", "Precio_Unitario", "Ciudad"]
]

print("--- Productos de Electrónica de Alta Gama ---")
display(filtro_alta_gama.head())
print(f"Total de registros encontrados: {len(filtro_alta_gama)}")
```

---

### 5. Ejercicio Práctico de Cierre para Alumnos (10 min)

**Consigna para los alumnos:**
1. Filtrar del dataset `df_sin_duplicados` todas las ventas cuyo estado sea `"Completado"` **Y** el `Metodo_Pago` sea `"Tarjeta de Crédito"` o `"PayPal"`.
2. Mostrar únicamente las columnas `ID_Pedido`, `Ciudad`, `Producto` y `Precio_Unitario`.
3. Imprimir el total de ventas completadas con esos métodos de pago.

#### Solución para el Instructor:
```python
ventas_exitosas = df_sin_duplicados.loc[
    (df_sin_duplicados["Estado"] == "Completado") & 
    ((df_sin_duplicados["Metodo_Pago"] == "Tarjeta de Crédito") | (df_sin_duplicados["Metodo_Pago"] == "PayPal")),
    ["ID_Pedido", "Ciudad", "Producto", "Precio_Unitario"]
]
display(ventas_exitosas.head())
```
