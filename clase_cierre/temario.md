# Temario de la clase de cierre: Del dato al hallazgo

**Duración:** 60 minutos

## Objetivo

Integrar los contenidos trabajados hasta la clase anterior mediante un análisis exploratorio guiado del dataset de ventas e-commerce.

## Contenidos

### 1. Repaso del flujo de análisis (5 minutos)

- Inspección, limpieza, transformación, agrupación, visualización y comunicación.
- Elección del gráfico según la pregunta:
  - líneas para tendencias;
  - barras para comparar categorías;
  - histogramas para distribuciones.

### 2. Carga e inspección con Pandas (10 minutos)

- `Path` y validación de la ruta.
- `pd.read_csv()`.
- `.shape`, `.head()` y `.dtypes`.
- Identificación de variables numéricas, categóricas y de fecha.

### 3. Limpieza y transformación (15 minutos)

- Conteo de valores faltantes con `.isna().sum()`.
- Conteo y eliminación de duplicados.
- Conversión de fechas con `pd.to_datetime()`.
- Creación de `monto_total` mediante operaciones entre columnas.

### 4. Agrupación y visualización con Matplotlib (20 minutos)

- `.groupby()` y `.sum()`.
- Ventas por fecha con gráfico de líneas.
- Ventas por categoría con gráfico de barras y colores distintivos.
- Distribución de precios con histograma y `bins`.
- Títulos, ejes, cuadrícula, rotación y `tight_layout()`.

### 5. Mini-reporte y comunicación de hallazgos (8 minutos)

- Identificación del pico de ventas.
- Categoría con mayor monto acumulado.
- Interpretación de la distribución de precios.
- Distinción entre evidencia, interpretación y limitaciones.

### 6. Cierre (2 minutos)

- Repaso del flujo completo.
- Reflexión sobre el análisis reproducible y basado en evidencia.

## Producto final de la sesión

Un análisis reproducible con:

- DataFrame limpio;
- columna calculada `monto_total`;
- gráfico de líneas;
- gráfico de barras con colores por categoría;
- histograma;
- tres hallazgos y una limitación documentados.
