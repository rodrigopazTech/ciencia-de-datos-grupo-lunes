# Temario de la Clase 8: Limpieza y Filtrado de Datos con Pandas (60 minutos)

**Objetivo:** Desarrollar habilidades para depurar y filtrar datasets utilizando Pandas, aprendiendo a identificar y tratar valores nulos, eliminar registros duplicados y seleccionar subconjuntos de datos mediante localización por etiquetas (`.loc`) e índices (`.iloc`).

---

### 1. Tratamiento de Valores Faltantes (Nulos) (20 minutos)
* **Detección de Nulos:** Uso de `.isna()` y `.isnull()` combinados con `.sum()` para contar nulos por columna.
* **Estrategias de Depuración:**
  - **Eliminación:** Uso de `.dropna()` para descartar filas con valores vacíos.
  - **Imputación:** Uso de `.fillna()` para reemplazar valores nulos por un valor predeterminado (por ejemplo, "No especificado" o el promedio de una columna).

### 2. Duplicados y Corrección de Tipos (10 minutos)
* **Registros Duplicados:** Detección de duplicados con `.duplicated()` y eliminación de filas repetidas mediante `.drop_duplicates()`.
* **Casting (Conversión de tipos):** Corrección de tipos de columnas usando `.astype()`.

### 3. Selección y Segmentación de Datos con `.loc[]` e `.iloc[]` (20 minutos)
* **Localización por Etiquetas (`.loc[]`):** Selección de filas y columnas basándose en sus nombres y etiquetas.
* **Localización por Índices (`.iloc[]`):** Selección de filas y columnas basándose en sus posiciones numéricas enteras.
* **Filtrado Condicional:** Selección de filas que cumplan condiciones específicas (ej. ventas completadas en una ciudad particular).

### 4. Taller de Cierre (10 minutos)
* **Ejercicio práctico (Depuración de Ventas):** Tomar el dataset `ventas_ecommerce.csv` que contiene nulos y duplicados. Eliminar las filas duplicadas, imputar los valores faltantes en `Metodo_Pago` con "No especificado", y filtrar únicamente las ventas completadas realizadas en "Ciudad de México" que superen los $5,000 MXN usando `.loc`.
* **Cierre:** Conexión hacia la Clase 9 (Operaciones avanzadas con Pandas: agrupaciones, agregaciones y uniones).
