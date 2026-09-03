# Clase 9: Transformación, Agregación y Uniones en Pandas

**Duración sugerida:** 60 minutos  
**Modalidad:** práctica en Jupyter Lab  
**Objetivo:** que el alumnado aprenda a crear columnas calculadas básicas y transformaciones complejas con `.apply()`, a resumir datos agrupándolos con `.groupby()` y a combinar múltiples tablas mediante uniones relacionales (`.merge()`).

---

### 🎨 Apoyo Visual para el Aprendizaje
* **Concepto:** La operación `.groupby` como metáfora física: canicas de diferentes colores mezcladas (rojas, azules y amarillas) caen a través de un embudo, se separan automáticamente en tres tubos distintos según su color y caen en recipientes individuales con básculas digitales que calculan el promedio de su peso.
* **Prompt para Generar Imagen con IA (Midjourney/DALL-E 3):**
  > *A 3D physical metaphor of a database groupby operation. Mixed colorful marbles (red, blue, yellow) flow down a funnel, sort automatically into three distinct tubes, and fall into cups with digital scales showing averages. Bright colors, clean design, educational illustration.*

---

## 1. Ingeniería de Características y Transformación con `.apply()` (20 min)

### Explicación para instructor

En ciencia de datos, a menudo necesitamos crear nuevas columnas a partir de las existentes. Esto se conoce como **Feature Engineering**:
- Las operaciones aritméticas básicas entre columnas se realizan de forma directa y vectorizada.
- Sin embargo, para aplicar transformaciones que involucren lógica condicional (como clasificar un producto según su precio), usamos el método `.apply()`.
- `.apply(funcion)` recorre cada valor de la columna y le aplica la función indicada, devolviendo la columna resultante.

#### Texto para una celda Markdown del notebook

## Transformación de columnas y Feature Engineering

- Operaciones directas: `df["Nueva"] = df["Col1"] * df["Col2"]`
- Transformación personalizada: `df["Columna"].apply(funcion_personalizada)`

#### Código para una celda de Jupyter

```python
import pandas as pd

df_ventas = pd.read_csv("recursos/ventas_ecommerce.csv").dropna()

# 1. Operación directa: Calcular el monto total de cada pedido
df_ventas["Monto_Total"] = df_ventas["Precio_Unitario"] * df_ventas["Cantidad"]
print("--- DataFrame con Monto_Total ---")
display(df_ventas[["Producto", "Precio_Unitario", "Cantidad", "Monto_Total"]].head(3))

# 2. Transformación con .apply(): Clasificar pedido en "Alto Valor" o "Bajo Valor"
def clasificar_monto(monto):
    if monto >= 5000:
        return "Alto Valor"
    else:
        return "Bajo Valor"

df_ventas["Segmento_Pedido"] = df_ventas["Monto_Total"].apply(clasificar_monto)

print("\n--- DataFrame Segmentado ---")
display(df_ventas[["Producto", "Monto_Total", "Segmento_Pedido"]].head(3))
```

#### Salida esperada

```text
--- DataFrame con Monto_Total ---
            Producto  Precio_Unitario  Cantidad  Monto_Total
0   Silla Ergonómica             4176         1         4176
1   Muñeco de Acción              453         1          453
2    Termo Deportivo              347         1          347

--- DataFrame Segmentado ---
            Producto  Monto_Total Segmento_Pedido
0   Silla Ergonómica         4176      Bajo Valor
1   Muñeco de Acción          453      Bajo Valor
2    Termo Deportivo          347      Bajo Valor
```

---

## 2. Agrupación y Resumen Ejecutivo: `.groupby()` (20 min)

### Explicación para instructor

Una tabla con cientos de filas es difícil de analizar a simple vista.
- La agrupación mediante `.groupby()` divide los datos en grupos basados en los valores de una columna categórica (ej. ciudades o categorías).
- Tras agrupar, aplicamos una **función de agregación** (como `.sum()` para totales, `.mean()` para promedios, o `.count()` para cantidad de pedidos) para colapsar los grupos en un resumen numérico.

#### Texto para una celda Markdown del notebook

## Agrupación de Datos (groupby)

- `df.groupby("Columna_Categoria")["Columna_Metrica"].sum()` calcula la suma de la métrica para cada categoría.
- Otras funciones comunes: `.mean()`, `.count()`, `.min()`, `.max()`.

#### Código para una celda de Jupyter

```python
# 1. Total vendido por Categoría de producto
ventas_por_categoria = df_ventas.groupby("Categoria")["Monto_Total"].sum()
print("--- Ventas Totales por Categoría ($ MXN) ---")
print(ventas_por_categoria)

# 2. Cantidad de pedidos y promedio de venta por Ciudad
print("\n--- Reporte Ejecutivo por Ciudad ---")
reporte_ciudad = df_ventas.groupby("Ciudad")["Monto_Total"].agg(["count", "mean", "sum"])
display(reporte_ciudad)
```

#### Salida esperada

```text
--- Ventas Totales por Categoría ($ MXN) ---
Categoria
Deportes        11964
Electrónica    381442
Hogar          121331
Juguetes        13788
Ropa            11425
Name: Monto_Total, dtype: int64

--- Reporte Ejecutivo por Ciudad ---
(Tabla con columnas count, mean y sum de Monto_Total agrupado por Ciudad)
```

---

## 3. Integración de Múltiples Fuentes: Uniones (10 min)

### Explicación para instructor

En las empresas, los datos están repartidos en diferentes archivos.
- `pd.concat([df1, df2])`: apila o concatena tablas que comparten las mismas columnas.
- `pd.merge(df_izq, df_der, on="clave")`: realiza una unión relacional (JOIN) basándose en una columna en común.

#### Texto para una celda Markdown del notebook

## Uniones y Combinación de Tablas

- `pd.concat([tabla1, tabla2])` une verticalmente tablas con las mismas columnas.
- `pd.merge(tabla1, tabla2, on="llave_comun")` une relacionalmente tablas utilizando una columna clave.

#### Código para una celda de Jupyter

```python
# Crear tabla de catálogo de comisiones para el canal de venta
comisiones_data = {
    "Categoria": ["Electrónica", "Ropa", "Hogar", "Juguetes", "Deportes"],
    "Comision_Porcentaje": [0.05, 0.08, 0.06, 0.10, 0.08]
}
df_comisiones = pd.DataFrame(comisiones_data)

# Cruzar las ventas con el catálogo de comisiones
df_completo = pd.merge(df_ventas, df_comisiones, on="Categoria")

print("--- DataFrame Fusionado (Merge) ---")
display(df_completo[["ID_Pedido", "Categoria", "Monto_Total", "Comision_Porcentaje"]].head(3))
```

#### Salida esperada

```text
--- DataFrame Fusionado (Merge) ---
  ID_Pedido    Categoria  Monto_Total  Comision_Porcentaje
0  PED_1000        Hogar         4176                 0.06
1  PED_1006        Hogar          650                 0.06
2  PED_1008        Hogar         4268                 0.06
```

---

## 4. Taller de Cierre: Reporte de Desempeño y Metas (10 min)

### Explicación para instructor

Pide al grupo que abra una celda y resuelva un problema donde deba calcular la comisión de cada venta y agrupar para ver el total de comisiones a pagar por categoría.

#### Actividad para el alumno

Utilizando el DataFrame fusionado `df_completo`:
1. Crea una columna calculada llamada `Comision_Cobrada` multiplicando `Monto_Total` por la columna `Comision_Porcentaje`.
2. Agrupa la tabla por `Categoria` y calcula el **total** de comisiones cobradas en cada una de ellas.
3. Imprime el resultado ordenado de mayor a menor utilizando `.sort_values(ascending=False)`.

#### Código para el notebook

```python
# 1. Calcular comisión por fila
df_completo["Comision_Cobrada"] = df_completo["Monto_Total"] * df_completo["Comision_Porcentaje"]

# 2. Agrupar y calcular total de comisión por categoría
comisiones_categoria = df_completo.groupby("Categoria")["Comision_Cobrada"].sum()

# 3. Ordenar e imprimir
print("--- Comisiones Totales a Pagar por Categoría ---")
print(comisiones_categoria.sort_values(ascending=False))
```

#### Salida esperada

```text
--- Comisiones Totales a Pagar por Categoría ---
Categoria
Electrónica    19072.10
Hogar           7279.86
Juguetes        1378.80
Deportes         957.12
Ropa             914.00
Name: Comision_Cobrada, dtype: float64
```

---

## Cierre de la sesión (2 min)

Recapitula brevemente:
Hoy cerramos nuestro bloque de manipulación de datos con Pandas. Aprendimos a crear variables calculadas vectorialmente y lógicas con `.apply()`, consolidamos reportes con `.groupby()` y unificamos tablas externas mediante `.merge()`.

En la siguiente sesión (Clase 10) entraremos al Módulo 3 para aprender a comunicar visualmente estos resultados, diseñando gráficos interactivos y profesionales con la librería **Matplotlib**.
