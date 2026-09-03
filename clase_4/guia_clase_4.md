# Clase 4: Colecciones Estructuradas y Bucles en Python

**Duración sugerida:** 60 minutos  
**Modalidad:** práctica en Google Colab  
**Objetivo:** que el alumnado domine el uso de Diccionarios (`dict`) para organizar datos estructurados, automatice tareas mediante bucles `for` (recorriendo listas y diccionarios) y aplique la Comprensión de Listas para filtrar y transformar colecciones.

---

### 🎨 Apoyo Visual para el Aprendizaje
* **Concepto:** Comparar una Lista (archivador con cajones numerados `0, 1, 2`) frente a un Diccionario (archivador con cajones etiquetados por nombre `nombre, precio, stock`). Mostrar un bucle `for` como una banda transportadora automatizada que toma y procesa un elemento a la vez.
* **Prompt para Generar Imagen con IA (Midjourney/DALL-E 3):**
  > *A clean, minimalist 3D infographic showing a comparison between a numbered filing cabinet (labeled 0, 1, 2) and a labeled filing cabinet (labeled 'name', 'price', 'stock'). In the background, a sleek automated conveyor belt system processing boxes of data one by one. Modern tech aesthetic, vibrant color palette (blues and oranges), isolated on a light gray background, clean UI style.*

---

## 1. Estructuras de datos: Diccionarios (`dict`) (20 min)

### 1.1 Crear y consultar un diccionario

#### Explicación para instructor

En las clases anteriores trabajamos con listas ordenadas por índice (`0`, `1`, `2`). Sin embargo, al representar un registro de datos (como la ficha de un cliente o un producto), resulta más claro acceder a la información por una **etiqueta o nombre descriptivo**.

Un **Diccionario** almacena datos en pares `llave: valor` (`key: value`).
- Se definen entre llaves `{}`.
- Cada llave se separa de su valor mediante dos puntos `:`.
- Para consultar un valor, usamos la llave entre corchetes: `diccionario["llave"]`.

> [!CAUTION]
> **🚨 NOTA PARA EL INSTRUCTOR (CONEXIÓN DATA SCIENCE - NO LEER EN VOZ ALTA):**  
> Enfatiza al grupo que un diccionario representa una **fila o registro individual** de una tabla de datos. En la Clase 7 verán que una tabla en Pandas (DataFrame) se compone de múltiples registros estructurados de esta forma.

#### Texto para una celda Markdown del notebook

## Diccionarios

Un diccionario almacena datos bajo pares `llave: valor` entre llaves `{}`.
Accedemos a los datos usando su llave: `diccionario["llave"]`.

#### Código para una celda de Colab

```python
# Crear un diccionario de un producto
producto = {
    "nombre": "Laptop Pro",
    "precio": 25000.0,
    "stock": 15
}

print("Diccionario completo:", producto)
print("Nombre:", producto["nombre"])
print("Precio:", producto["precio"])
```

#### Salida esperada

```text
Diccionario completo: {'nombre': 'Laptop Pro', 'precio': 25000.0, 'stock': 15}
Nombre: Laptop Pro
Precio: 25000.0
```

> **Pregunta para el grupo:** ¿qué sucede si intentas consultar una llave que no existe, como `producto["marca"]`? *(Respuesta: Python genera un error KeyErrors)*.

### 1.2 Modificar y consultar métodos de diccionarios

#### Explicación para instructor

Los diccionarios son mutables:
- **Modificar:** `diccionario["llave"] = nuevo_valor`
- **Agregar nueva llave:** si asignamos un valor a una llave que no existía, Python la crea.

Además, cuentan con tres métodos clave para análisis de datos:
- `.keys()`: devuelve todas las llaves.
- `.values()`: devuelve todos los valores.
- `.items()`: devuelve los pares `(llave, valor)` agrupados en tuplas (colección ordenada inmutable).

#### Texto para una celda Markdown del notebook

## Modificación y métodos de diccionarios

- Agregar/Modificar: `diccionario["llave"] = valor`
- `.keys()`: obtiene todas las llaves.
- `.values()`: obtiene todos los valores.
- `.items()`: obtiene los pares `(llave, valor)` en tuplas `(clave, valor)`.

#### Código para una celda de Colab

```python
producto = {"nombre": "Laptop Pro", "precio": 25000.0}

# Actualizar precio y agregar marca
producto["precio"] = 23500.0
producto["marca"] = "Dell"

print("Llaves:", list(producto.keys()))
print("Valores:", list(producto.values()))
print("Pares (llave, valor):", list(producto.items()))
```

#### Salida esperada

```text
Llaves: ['nombre', 'precio', 'marca']
Valores: ['Laptop Pro', 23500.0, 'Dell']
Pares (llave, valor): [('nombre', 'Laptop Pro'), ('precio', 23500.0), ('marca', 'Dell')]
```

---

## 2. Automatización con Bucles `for` y `range()` (25 min)

### 2.1 Bucle `for` en listas y `range()`

#### Explicación para instructor

El bucle `for` permite repetir instrucciones para cada elemento de una colección de manera automatizada.
- Sintaxis: `for elemento in coleccion:` seguido de una sangría de 4 espacios (indentación).
- Para repetir una tarea un número determinado de veces, usamos `range(inicio, fin, paso)`. El límite `fin` es exclusivo (no se incluye).

#### Texto para una celda Markdown del notebook

## Ciclo for y función range()

El bucle `for` recorre elemento por elemento una colección.
`range(inicio, fin)` genera una secuencia numérica (el límite `fin` no se incluye).

#### Código para una celda de Colab

```python
# 1. Recorrer una lista de precios
precios = [100, 250, 400]
print("--- Recorriendo lista de precios ---")
for p in precios:
    print(f"Precio con IVA (16%): ${p * 1.16:.2f}")

# 2. Secuencia con range
print("\n--- Secuencia con range(1, 4) ---")
for i in range(1, 4):
    print(f"Iteración número: {i}")
```

#### Salida esperada

```text
--- Recorriendo lista de precios ---
Precio con IVA (16%): $116.00
Precio con IVA (16%): $290.00
Precio con IVA (16%): $464.00

--- Secuencia con range(1, 4) ---
Iteración número: 1
Iteración número: 2
Iteración número: 3
```

### 2.2 Recorrer diccionarios con `.items()`

#### Explicación para instructor

Para iterar sobre un diccionario, el método más limpio y potente es `.items()`. Esto nos permite desempacar dos variables simultáneamente en cada vuelta del ciclo: una para la llave (clave) y otra para el valor.

#### Texto para una celda Markdown del notebook

## Recorrer diccionarios con for

Usamos `.items()` para extraer la llave y el valor simultáneamente en cada vuelta del ciclo.

#### Código para una celda de Colab

```python
cliente = {
    "nombre": "Ana López",
    "compras": 5,
    "total_gastado": 1250.50
}

print("--- Ficha de cliente ---")
for llave, valor in cliente.items():
    print(f"{llave.upper()}: {valor}")
```

#### Salida esperada

```text
--- Ficha de cliente ---
NOMBRE: Ana López
COMPRAS: 5
TOTAL_GASTADO: 1250.5
```

---

## 3. Comprensión de listas (*List Comprehensions*) (10 min)

### Explicación para instructor

La **comprensión de listas** es una sintaxis concisa y optimizada de Python para crear una lista nueva a partir de una existente en una sola línea de código, reduciendo la necesidad de inicializar listas vacías y usar `.append()`.
- Sintaxis: `[expresion for elemento in lista if condicion]`.
- Podemos usar el operador `not` para filtros inversos (ej. seleccionar elementos que *no* cumplen cierta condición).

#### Texto para una celda Markdown del notebook

## Comprensión de listas (List Comprehensions)

Crea y filtra listas en una sola línea de código.
Sintaxis básica: `[nueva_expresion for elemento in lista if condicion]`

#### Código para una celda de Colab

```python
ventas = [50, 120, 80, 200, 45]

# 1. Filtrar ventas mayores a 100 y aplicarles 10% de descuento
ventas_altas_descuento = [v * 0.90 for v in ventas if v > 100]

# 2. Filtrar ventas que NO sean menores o iguales a 50 (usando 'not')
ventas_no_bajas = [v for v in ventas if not v <= 50]

print("Ventas originales:", ventas)
print("Ventas > 100 con descuento:", ventas_altas_descuento)
print("Ventas no bajas (not <= 50):", ventas_no_bajas)
```

#### Salida esperada

```text
Ventas originales: [50, 120, 80, 200, 45]
Ventas > 100 con descuento: [108.0, 180.0]
Ventas no bajas (not <= 50): [120, 80, 200]
```

---

## 4. Taller de Cierre: Reporte de Ventas (5 min)

### Explicación para instructor

Pide al grupo que abra una celda de código y procese un conjunto de registros de clientes usando diccionarios y comprensión de listas.

#### Texto para una celda Markdown del notebook

## Ejercicio Integrador: Clientes VIP

Tenemos un diccionario donde las llaves son nombres de clientes y sus valores son el total de sus compras.
Escribe un bloque de código que:
1. Recorra el diccionario usando `.items()` e imprima la ficha de compras de cada cliente.
2. Utilice una **comprensión de listas** para extraer los nombres de los clientes que gastaron más de $1000.
3. Imprima la lista resultante de clientes VIP.

#### Código para una celda de Colab

```python
historial_compras = {
    "Carlos": 450.0,
    "Sofía": 1200.5,
    "Mateo": 890.0,
    "Valeria": 1500.0
}

# 1. Recorrer el historial
print("--- Historial de Compras ---")
for cliente, total in historial_compras.items():
    print(f"Cliente: {cliente} | Total gastado: ${total:.2f}")

# 2. Filtrar VIPs con List Comprehension
vips = [cliente for cliente, total in historial_compras.items() if total > 1000]
print("\nClientes VIP (compras > $1000):", vips)
```

#### Salida esperada

```text
--- Historial de Compras ---
Cliente: Carlos | Total gastado: $450.00
Cliente: Sofía | Total gastado: $1200.50
Cliente: Mateo | Total gastado: $890.00
Cliente: Valeria | Total gastado: $1500.00

Clientes VIP (compras > $1000): ['Sofía', 'Valeria']
```

---

## Cierre de la sesión (2 min)

Recapitula brevemente:
Hoy dominamos el uso de los **Diccionarios** para representar filas de datos y estructurar información llave:valor. Aprendimos a iterar automáticamente con el bucle `for` y a usar las **List Comprehensions** para generar listas filtradas de manera elegante.

En la siguiente sesión (Clase 5) cerraremos el bloque de fundamentos de programación aprendiendo a crear **Funciones** reutilizables, importar **Módulos nativos** y configurar el entorno local profesional de **Jupyter Lab** mediante Anaconda.
