# Temario de la Clase 3: Manipulación de Texto, Condicionales y Diccionarios (60 minutos)

**Objetivo:** Dominar la manipulación y formateo de texto, profundizar en la extracción de listas mediante *slicing*, tomar decisiones lógicas en el código utilizando estructuras condicionales (`if/elif/else`), y comprender el uso de Diccionarios como estructuras fundamentales para representar registros de datos.

---

### 1. Manipulación de Texto y Formato con `f-strings` (12 minutos)
* **Format String Literals (`f-strings`):** Uso de la sintaxis `f"..."` para incrustar variables directamente dentro de cadenas de texto.
* **Formato numérico dentro de `f-strings`:** Limitación de decimales (ej. `{promedio:.2f}`) y uso de caracteres de escape como saltos de línea (`\n`).
* **Métodos útiles de texto (`str`):** Transformación de cadenas con `.lower()`, `.upper()`, `.strip()` y `.replace()`.
* **Entrada de datos (`input()`) y Casting:** Solicitud de información al usuario y conversión de tipo explícita (`int()`, `float()`).

### 2. Extracción Avanzada en Listas: *Slicing* y Métodos (13 minutos)
* **Slicing de listas:** Sintaxis `lista[inicio:fin]` y `lista[inicio:fin:paso]`. Explicación del límite superior no inclusivo.
* **Operador de pertenencia (`in`):** Verificación de si un elemento existe dentro de una lista (`"Ana" in alumnos`).
* **Métodos adicionales:** Eliminación de elementos con `.pop()` y `.remove()`, y ordenamiento de colecciones con `.sort()`.

### 3. Control de Flujo: Tomando Decisiones con Condicionales (18 minutos)
* **Operadores de comparación:** Evaluación de relaciones (`==`, `!=`, `>`, `<`, `>=`, `<=`).
* **Operadores lógicos:** Combinación de condiciones usando `and`, `or` y `not`.
* **Estructura condicional (`if`, `elif`, `else`):** Control del flujo de ejecución según reglas de negocio o filtros de datos.
* **Conexión con Data Science:** Filtrado de registros y clasificación de datos según criterios.

### 4. Estructuras de Datos II: Diccionarios (`dict`) (12 minutos)
* **Concepto de Diccionario:** Estructura de datos basada en la lógica **llave: valor** (`key: value`).
* **Acceso y modificación:** Consulta mediante llaves (`diccionario["llave"]`), modificación de valores existentes y adición de nuevas llaves.
* **Métodos integrados esenciales:** Extracción exclusiva de llaves (`.keys()`), valores (`.values()`) y pares en tuplas (`.items()`).
* **Conexión con Data Science:** Presentación del diccionario como la representación de una fila/registro individual dentro de una tabla de datos (DataFrame).

### 5. Ejercicio Integrador de Cierre y Cierre (5 minutos)
* **Ejercicio práctico:** Evaluación de un perfil de cliente o estudiante guardado en un diccionario, aplicando condicionales `if/elif/else` y mostrando un reporte automatizado formateado con `f-strings`.
* **Cierre:** Recapitulación de lo aprendido y vista previa de la Clase 4 (Bucles `for`/`while`, *List Comprehensions*, Funciones `def` y Módulos).
