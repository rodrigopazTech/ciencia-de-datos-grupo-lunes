# Temario de la Clase 9: Transformación, Agregación y Uniones en Pandas (60 minutos)

**Objetivo:** Desarrollar habilidades avanzadas de modelado y manipulación de datos en Pandas, aprendiendo a crear columnas derivadas mediante `.apply()`, agrupar y consolidar información categorizada con `.groupby()` y unificar múltiples conjuntos de datos utilizando `.merge()` y `.concat()`.

---

### 1. Ingeniería de Características (Feature Engineering) y `.apply()` (20 minutos)
* **Creación de Columnas:** Sumar, restar y multiplicar columnas directas (ej. multiplicar `Precio_Unitario` por `Cantidad` para calcular el `Total`).
* **Transformación Personalizada:** Uso de `.apply()` para aplicar funciones lógicas o matemáticas complejas a cada celda de una columna (ej. clasificar compras en categorías de volumen "Alto" o "Bajo").

### 2. Agrupación y Resumen Ejecutivo: `.groupby()` (20 minutos)
* **Agrupación por Categorías:** Uso de `.groupby()` para segmentar el dataset según variables categóricas (ej. ventas totales por `Ciudad` o por `Categoria`).
* **Funciones de Agregación:** Aplicación de funciones de resumen como `.sum()`, `.mean()`, `.count()` y `.agg()` para obtener reportes consolidados del negocio.

### 3. Integración de Múltiples Fuentes: Uniones (10 minutos)
* **Concatenación (`pd.concat()`):** Unir tablas de datos de forma vertical (añadir filas) o de forma horizontal (añadir columnas).
* **Fusión (`pd.merge()`):** Realizar cruces relacionales de tablas utilizando claves comunes (el equivalente a un JOIN en SQL).

### 4. Taller de Cierre (10 minutos)
* **Ejercicio práctico (Reporte de Negocio):** Tomar el dataset depurado de ventas, calcular la columna de ingresos totales (`Total_Venta`), agrupar la información por `Categoria` para obtener la suma de ingresos y la cantidad promedio vendida, y finalmente cruzar este reporte con una tabla pequeña de metas de venta utilizando `.merge()` para evaluar el desempeño.
* **Cierre:** Conexión hacia la Clase 10 (Visualización de datos e inicio de Matplotlib).
