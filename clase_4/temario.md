# Temario de la Clase 4: Colecciones Estructuradas y Bucles en Python (60 minutos)

**Objetivo:** Dominar el almacenamiento estructurado en Diccionarios (pares llave: valor), aprender a iterar sobre colecciones mediante bucles `for` y `range()`, y utilizar la Comprensión de Listas (*List Comprehensions*) para transformaciones y filtros rápidos.

---

### 1. Estructuras de Datos: Diccionarios (`dict`) (20 minutos)
* **Concepto y estructura:** Almacenamiento basado en la lógica **llave: valor** (`key: value`).
* **Acceso y modificación:** Consultas por llave (`diccionario["llave"]`), actualización de valores y adición de llaves nuevas.
* **Métodos principales:** Extracción selectiva de llaves (`.keys()`), valores (`.values()`) y pares como tuplas inmutables (`.items()`).
* **Conexión Data Science:** Explicar cómo un diccionario representa una fila o registro individual de una tabla.

### 2. Automatización con Bucles `for` y `range()` (25 minutos)
* **El bucle `for`:** Concepto de repetición y sintaxis. Importancia de la indentación (sangría).
* **Iteración sobre listas:** Uso de la función de rango `range(inicio, fin, paso)`.
* **Iteración sobre diccionarios:** Uso de `.items()` para recorrer llaves y valores simultáneamente (`for llave, valor in diccionario.items():`).

### 3. Comprensión de Listas (*List Comprehensions*) (10 minutos)
* **Sintaxis compacta:** Crear y filtrar listas en una sola línea de código: `[expresion for elemento in lista if condicion]`.
* **Operador `not`:** Filtros inversos (nivelación de la sesión anterior).
* **Comparativa:** Contraste frente a la sintaxis tradicional de inicializar lista vacía, recorrer y usar `.append()`.

### 4. Taller de Cierre (5 minutos)
* **Ejercicio práctico (Reporte de ventas):** Procesar un diccionario con el historial de compras de varios clientes. Iterar sobre ellos con un bucle `for`, calcular descuentos y aplicar un filtro mediante *list comprehensions* para mostrar solo los clientes VIP con reporte formateado.
* **Cierre:** Conexión pedagógica hacia la Clase 5 (Modularidad de código con funciones y setups locales).
