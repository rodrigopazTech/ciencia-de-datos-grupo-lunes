# Clase de cierre: Del dato al hallazgo

**Duración sugerida:** 60 minutos  
**Modalidad:** práctica guiada en Jupyter Lab  
**Dataset:** `../clase_11/recursos/ventas_ecommerce.csv`  
**Nivel alcanzado:** Python básico, Pandas, limpieza, transformación, agrupación y visualización con Matplotlib.

## Objetivo

Integrar lo aprendido hasta la clase anterior en un análisis breve de ventas: cargar y revisar datos, limpiar registros, crear una métrica, resumirla por categoría y fecha, construir visualizaciones y comunicar hallazgos de negocio.

> Esta sesión cierra el bloque trabajado por el grupo. No introduce Machine Learning, Seaborn ni conceptos nuevos; se concentra en practicar y explicar el flujo completo.

## Resultado esperado

Al finalizar, cada participante tendrá:

1. Un DataFrame limpio y documentado.
2. Una columna `monto_total`.
3. Un gráfico de líneas de ventas por fecha.
4. Un gráfico de barras de ventas por categoría, con un color por categoría.
5. Un histograma de precios unitarios.
6. Tres conclusiones escritas y una limitación del análisis.

---

## 1. Apertura y mapa del flujo (5 min)

Pregunta al grupo:

- ¿Qué diferencia hay entre una fila duplicada y un valor nulo?
- ¿Cuándo usaríamos un gráfico de líneas, uno de barras y un histograma?
- ¿Qué información necesitamos antes de interpretar una gráfica?

Presenta el flujo de trabajo:

```text
CSV -> inspección -> limpieza -> transformación -> agrupación -> visualización -> conclusión
```

Recalca que una visualización no sustituye la revisión de la calidad de los datos.

---

## 2. Carga e inspección inicial (10 min)

### Código para ejecutar

```python
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

plt.rcParams["font.size"] = 11

ruta_csv = Path("../clase_11/recursos/ventas_ecommerce.csv")
if not ruta_csv.exists():
    raise FileNotFoundError(f"No se encontró el archivo: {ruta_csv}")

df_original = pd.read_csv(ruta_csv)

print(f"Filas y columnas: {df_original.shape}")
display(df_original.head())
display(df_original.dtypes)
```

### Conversación guiada

Pide que identifiquen:

- Qué columnas son numéricas, de texto y de fecha.
- Qué columna representa una venta individual.
- Qué variables pueden utilizarse para agrupar.

---

## 3. Limpieza y creación de una métrica (15 min)

### Código para ejecutar

```python
print("Valores faltantes por columna:")
display(df_original.isna().sum())

print(f"Filas duplicadas: {df_original.duplicated().sum()}")

# Para este ejercicio, conservamos únicamente filas completas y no duplicadas.
df_ventas = (
    df_original
    .dropna()
    .drop_duplicates()
    .copy()
)

df_ventas["Fecha"] = pd.to_datetime(df_ventas["Fecha"], format="%Y-%m-%d")
df_ventas["monto_total"] = (
    df_ventas["Precio_Unitario"] * df_ventas["Cantidad"]
)

print(f"Filas originales: {len(df_original)}")
print(f"Filas listas para analizar: {len(df_ventas)}")
display(
    df_ventas[
        ["Fecha", "Categoria", "Precio_Unitario", "Cantidad", "monto_total"]
    ].head()
)
```

### Puntos para explicar

- `dropna()` evita que los registros incompletos distorsionen el ejercicio.
- `drop_duplicates()` evita contar dos veces una misma fila.
- `copy()` crea un DataFrame independiente para trabajar con seguridad.
- `monto_total` es una variable derivada: precio unitario por cantidad.
- El número final de filas debe calcularse con `len(df_ventas)`, no memorizarse.

---

## 4. Resúmenes y visualizaciones (20 min)

### 4.1 Ventas por fecha: gráfico de líneas

```python
ventas_por_fecha = (
    df_ventas
    .groupby("Fecha")["monto_total"]
    .sum()
    .sort_index()
)

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(
    ventas_por_fecha.index,
    ventas_por_fecha.values,
    color="royalblue",
    marker="o",
    linewidth=1.5,
)
ax.set_title("Monto total de ventas por fecha")
ax.set_xlabel("Fecha")
ax.set_ylabel("Monto total (MXN)")
ax.grid(axis="y", alpha=0.3)
ax.tick_params(axis="x", rotation=45)
fig.tight_layout()
plt.show()
```

Solicita que localicen el día con mayor venta:

```python
fecha_maxima = ventas_por_fecha.idxmax()
monto_maximo = ventas_por_fecha.max()
print(f"Mayor venta: {fecha_maxima:%Y-%m-%d} con ${monto_maximo:,.2f} MXN")
```

### 4.2 Ventas por categoría: gráfico de barras

```python
ventas_por_categoria = (
    df_ventas
    .groupby("Categoria")["monto_total"]
    .sum()
    .sort_values(ascending=False)
)

colores = {
    categoria: color
    for categoria, color in zip(
        ventas_por_categoria.index,
        ["teal", "darkorange", "seagreen", "mediumpurple", "crimson"],
    )
}

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(
    ventas_por_categoria.index,
    ventas_por_categoria.values,
    color=[colores[categoria] for categoria in ventas_por_categoria.index],
)
ax.set_title("Monto total de ventas por categoría")
ax.set_xlabel("Categoría")
ax.set_ylabel("Monto total (MXN)")
ax.grid(axis="y", linestyle="--", alpha=0.4)
fig.tight_layout()
plt.show()
```

Explica que el diccionario relaciona cada categoría con un color, mientras que la lista `color=` conserva el mismo orden de las categorías y sus montos.

### 4.3 Distribución de precios: histograma

```python
fig, ax = plt.subplots(figsize=(8, 4))
ax.hist(
    df_ventas["Precio_Unitario"],
    bins=12,
    color="coral",
    edgecolor="black",
)
ax.set_title("Distribución de precios unitarios")
ax.set_xlabel("Precio unitario (MXN)")
ax.set_ylabel("Frecuencia")
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()
plt.show()
```

Aclara que el histograma agrupa valores numéricos en intervalos (`bins`); no compara categorías.

---

## 5. Reto final: mini-reporte de ventas (8 min)

Pide al grupo completar un reporte que responda:

1. ¿Qué categoría acumuló el mayor monto total?
2. ¿Qué fecha tuvo el pico de ventas?
3. ¿Los precios unitarios están concentrados en un intervalo o hay valores muy dispersos?
4. ¿Qué decisión de negocio podría apoyarse en estos resultados?
5. ¿Qué no podemos afirmar con este dataset?

### Plantilla de respuesta

```python
categoria_maxima = ventas_por_categoria.idxmax()
monto_categoria_maxima = ventas_por_categoria.max()

print(
    f"La categoría con mayor monto fue {categoria_maxima}, "
    f"con ${monto_categoria_maxima:,.2f} MXN."
)
print("Hallazgo sobre la fecha pico: ______________________________")
print("Hallazgo sobre la distribución de precios: __________________")
print("Decisión de negocio posible: ________________________________")
print("Limitación del análisis: ____________________________________")
```

### Solución orientativa para revisar en grupo

La respuesta debe mencionar valores observables en las tablas o gráficos, no solo describir colores o formas. También debe reconocer que el análisis muestra asociaciones y acumulados históricos; por sí solo no demuestra causalidad, rentabilidad futura ni comportamiento de clientes.

---

## 6. Cierre y reflexión (2 min)

Recapitula el flujo:

```text
Inspeccionar -> limpiar -> transformar -> agrupar -> visualizar -> comunicar
```

Mensaje final:

> La herramienta importante no es memorizar una función aislada, sino aprender a formular preguntas, revisar la calidad de los datos y respaldar cada conclusión con evidencia.

Como actividad opcional, cada participante puede guardar los gráficos con `fig.savefig(...)` y entregar una captura o un breve reporte con sus tres hallazgos.
