# Clase 10: Visualización de Datos I con Matplotlib

**Duración sugerida:** 60 minutos  
**Modalidad:** práctica en Jupyter Lab  
**Objetivo:** que el alumnado aprenda a representar gráficamente sus análisis construyendo gráficos de líneas (tendencias), barras (comparaciones) e histogramas (distribuciones) utilizando **Matplotlib**, aplicando estilos y etiquetas profesionales.

---

### 🎨 Apoyo Visual para el Aprendizaje
* **Concepto:** Un plano técnico o boceto arquitectónico de un gráfico donde cada una de las partes de la API de Matplotlib (`plt.title()`, `plt.xlabel()`, `plt.ylabel()`, `plt.grid()`, y `plt.legend()`) está indicada con flechas de planos de ingeniería.
* **Prompt para Generar Imagen con IA (Midjourney/DALL-E 3):**
  > *A blueprint-style 3D architectural drawing of a line graph. Labeled arrows point to various anatomical parts: 'plt.title()', 'plt.xlabel()', 'plt.ylabel()', 'plt.grid()', and 'plt.legend()'. Blueprint style with grid lines, technical drafting aesthetic, blue background with white lines, clean typography.*

---

## 1. Introducción a Matplotlib y Anatomía de un Gráfico (15 min)

### Explicación para instructor

Comunica al grupo que los seres humanos entendemos las imágenes mucho más rápido que las tablas numéricas. La visualización de datos es clave para contar historias (Data Storytelling).
- **Matplotlib** es la biblioteca abuela y motor de graficación en Python.
- Un gráfico en Matplotlib consta de:
  - `Figure`: el lienzo completo (la ventana o marco del gráfico).
  - `Axes`: el gráfico individual dibujado dentro del lienzo (con sus ejes X e Y).
- Por convención universal, importamos la interfaz de pyplot como `plt`: `import matplotlib.pyplot as plt`.

#### Texto para una celda Markdown del notebook

## Anatomía en Matplotlib

Matplotlib organiza sus gráficos mediante dos componentes principales:
- **Figure:** El lienzo completo donde se dibuja.
- **Axes:** El gráfico en sí, que contiene los ejes, marcas, líneas, etc.
Usamos la convención `import matplotlib.pyplot as plt`.

#### Código para una celda de Jupyter

```python
import pandas as pd
import matplotlib.pyplot as plt

df_ventas = pd.read_csv("recursos/ventas_ecommerce.csv").dropna()
df_ventas["Monto_Total"] = df_ventas["Precio_Unitario"] * df_ventas["Cantidad"]

# 1. Crear una figura básica vacía para entender la anatomía
fig, ax = plt.subplots(figsize=(6, 3))
ax.set_title("Lienzo de Ejemplo (Axes)")
plt.show()  # Muestra el gráfico en pantalla y limpia la memoria
```

#### Salida esperada

```text
(Se despliega un cuadro de gráfico vacío con título "Lienzo de Ejemplo (Axes)" y ejes de 0 a 1)
```

---

## 2. Creación de Gráficos Básicos (20 min)

### Explicación para instructor

Enseñaremos los tres gráficos indispensables para reportes descriptivos:
1. **Líneas (`plt.plot()`):** Para mostrar tendencias. Agruparemos las ventas acumuladas por fecha.
2. **Barras (`plt.bar()`):** Para comparar valores discretos. Mostraremos el total vendido por categoría.
3. **Histograma (`plt.hist()`):** Para ver cómo se distribuye una columna numérica. Mostraremos la distribución de los precios de los productos.

#### Texto para una celda Markdown del notebook

## Gráficos Fundamentales en Matplotlib

- `plt.plot(x, y)`: Gráfico de líneas (Tendencias).
- `plt.bar(x, y)`: Gráfico de barras (Comparaciones).
- `plt.hist(x, bins)`: Histograma (Distribución de frecuencias).

#### Código para una celda de Jupyter

```python
# Preparar datos
ventas_fecha = df_ventas.groupby("Fecha")["Monto_Total"].sum()
ventas_cat = df_ventas.groupby("Categoria")["Monto_Total"].sum()

# 1. Gráfico de Líneas (Tendencia de Ventas en el tiempo)
plt.figure(figsize=(10, 4))
plt.plot(ventas_fecha.index, ventas_fecha.values, color="royalblue", marker="o")
plt.title("Tendencia de Ventas Diarias")
plt.xticks(rotation=45)  # Rotar fechas para que no se encimen
plt.show()

# 2. Gráfico de Barras (Ventas por Categoría)
plt.figure(figsize=(8, 4))
plt.bar(ventas_cat.index, ventas_cat.values, color="teal")
plt.title("Ventas Totales por Categoría de Producto")
plt.show()

# 3. Histograma (Distribución de Precios)
plt.figure(figsize=(8, 4))
plt.hist(df_ventas["Precio_Unitario"], bins=15, color="coral", edgecolor="black")
plt.title("Distribución de Precios Unitarios de Productos")
plt.show()
```

#### Salida esperada

```text
(Se despliegan secuencialmente tres gráficos bien definidos: líneas con marcas azules, barras color verde-azul y un histograma naranja con bordes negros)
```

---

## 3. Personalización y Diseño Profesional (15 min)

### Explicación para instructor

Un gráfico sin etiquetas ni títulos correctos no sirve para presentar un análisis.
Enseñaremos cómo personalizar los gráficos para que se vean listos para negocio:
- Configurar títulos y etiquetas claras (`plt.xlabel()`, `plt.ylabel()`).
- Agregar cuadrículas de fondo para facilitar la lectura visual (`plt.grid()`).
- Guardar la imagen final a disco con `plt.savefig()` antes de llamar a `plt.show()`.

#### Texto para una celda Markdown del notebook

## Personalización de Gráficos

Es vital incluir títulos descriptivos, etiquetas en los ejes y cuadrículas.
Guardamos la imagen con `plt.savefig("nombre_archivo.png", dpi=300)`.

#### Código para una celda de Jupyter

```python
plt.figure(figsize=(8, 4))
plt.bar(ventas_cat.index, ventas_cat.values, color="forestgreen")

# Personalización
plt.title("Reporte de Ventas por Categoría de Producto (Primer Semestre)", fontsize=14, fontweight="bold")
plt.xlabel("Categorías", fontsize=11)
plt.ylabel("Total Vendido ($ MXN)", fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.7)  # Cuadrícula solo horizontal

# Guardar la imagen a recursos
plt.savefig("recursos/ventas_por_categoria.png", dpi=100, bbox_inches="tight")
plt.show()
```

#### Salida esperada

```text
(Se despliega el gráfico de barras verdes, ahora con una cuadrícula punteada al fondo, títulos en negritas y etiquetas descriptivas)
```

---

## 4. Taller de Cierre: Comparador de Ventas por Ciudad (10 min)

### Explicación para instructor

Pide al grupo que abra una celda nueva y genere un gráfico comparativo de ventas por ciudad siguiendo las pautas de diseño profesional.

#### Actividad para el alumno

Utilizando el DataFrame `df_ventas`:
1. Agrupa las ventas calculando la suma de `Monto_Total` por la columna `Ciudad`.
2. Genera un gráfico de barras horizontales (usando `plt.barh()`) para comparar el desempeño de las ciudades.
3. Personaliza el gráfico:
   - Usa un color agradable (por ejemplo, `"darkorchid"`).
   - Añade títulos y etiquetas descriptivas.
   - Activa la cuadrícula en el eje X (`plt.grid(axis='x')`).
4. Guarda el gráfico en la carpeta de recursos como `ventas_por_ciudad.png`.

#### Código para el notebook

```python
# 1. Agrupación
ventas_ciudad = df_ventas.groupby("Ciudad")["Monto_Total"].sum().sort_values()

# 2. Creación del gráfico
plt.figure(figsize=(8, 4))
plt.barh(ventas_ciudad.index, ventas_ciudad.values, color="darkorchid")

# 3. Personalización
plt.title("Ventas Acumuladas por Ciudad", fontsize=13, fontweight="bold")
plt.xlabel("Ingresos Totales ($ MXN)", fontsize=10)
plt.ylabel("Ciudades", fontsize=10)
plt.grid(axis="x", linestyle=":", alpha=0.6)

# 4. Guardar y mostrar
plt.savefig("recursos/ventas_por_ciudad.png", dpi=100, bbox_inches="tight")
plt.show()
```

#### Salida esperada

```text
(Se despliega un gráfico de barras horizontales ordenadas de menor a mayor en color púrpura, con etiquetas de pesos en el eje X y nombres de las ciudades mexicanas en el eje Y)
```

---

## Cierre de la sesión (2 min)

Recapitula brevemente:
Hoy dominamos el motor de graficación **Matplotlib**. Aprendimos a crear y exportar gráficos de líneas, barras e histogramas, y comprendimos la importancia de la estética y la personalización mediante títulos, etiquetas y cuadrículas.

En la siguiente sesión (Clase 11) daremos el salto a **Seaborn**, una biblioteca de visualización basada en Matplotlib que simplifica la creación de gráficos estadísticos complejos, ejecutando nuestro primer Análisis Exploratorio de Datos (EDA) completo.
