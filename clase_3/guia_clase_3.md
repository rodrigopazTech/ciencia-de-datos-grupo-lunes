# Clase 3: Manipulación de Texto, Condicionales y Diccionarios

**Duración sugerida:** 60 minutos  
**Modalidad:** práctica en Google Colab  
**Objetivo:** que el alumnado aplique `f-strings` para formatear cadenas de texto, extraiga subconjuntos de listas mediante *slicing*, evalúe decisiones lógicas utilizando estructuras `if/elif/else` y organice datos estructurados con diccionarios (`dict`).

> **Dinámica recomendada:** abre un notebook nuevo en Google Colab (o continúa en el mismo cuaderno). Para cada bloque, primero comparte la explicación para instructor, después crea una celda de texto con el resumen y, finalmente, escribe y ejecuta el código junto con el grupo. Invítalos a modificar los datos de prueba y reejecutar.

---

## 1. Manipulación de texto, formato y entrada de datos (12 min)

### 1.1 Formateo de texto moderno con `f-strings`

#### Explicación para instructor

En la primera sesión unimos textos usando la coma en `print()` o el operador `+`. Sin embargo, en Python existe una herramienta más limpia y profesional llamada **Formatted String Literals** o `f-strings`.

Por ejemplo, en la Clase 2 uníamos textos así:

```python
# Recordatorio Clase 2: concatenar con '+' (requiere convertir a str) o separando con comas
nombre = "Carlos"
edad = 25

print("Hola " + nombre + ", tienes " + str(edad) + " años.")  # Usando operador +
print("Hola", nombre, ", tienes", edad, "años.")              # Usando comas
```

Una `f-string` se crea colocando una letra `f` antes de las comillas iniciales. Dentro del texto, podemos incrustar cualquier variable o expresión entre llaves `{}`. Python evaluará lo que esté dentro de las llaves y lo convertirá en texto automáticamente.

Además, las `f-strings` permiten dar formato numérico rápidamente. Por ejemplo, `{promedio:.2f}` le indica a Python que muestre el número flotante recortado a 2 decimales. También podemos usar `\n` dentro de la cadena para dar un salto de línea. Esto es fundamental para generar reportes legibles al presentar análisis de datos.

#### Texto para una celda Markdown del notebook

## Formato de texto con f-strings

Las `f-strings` permiten insertar variables directamente dentro de un texto usando `f"..."` y colocando las variables entre llaves `{}`.

- `{variable:.2f}`: limita la exhibición de un decimal a 2 posiciones.
- `\n`: inserta un salto de línea.

#### Código para una celda de Colab

```python
nombre_usuario = "Carlos Gómez"
ingresos = 45000.856
score_credito = 720

# Formateo con f-strings
mensaje = f"Cliente: {nombre_usuario}\nScore: {score_credito}\nIngresos mensuales: ${ingresos:.2f}"
print(mensaje)
```

#### Salida esperada

```text
Cliente: Carlos Gómez
Score: 720
Ingresos mensuales: $45000.86
```

> **Pregunta para el grupo:** ¿qué sucede si cambias `:.2f` por `:.1f` en el código?

### 1.2 Métodos de texto y conversión de entrada (`input` y casting)

#### Explicación para instructor

Las cadenas de texto en Python poseen métodos integrados para limpiar y transformar texto:
- `.upper()`: convierte todo a mayúsculas.
- `.lower()`: convierte todo a minúsculas.
- `.strip()`: remueve espacios innecesarios al inicio y al final.
- `.replace(viejo, nuevo)`: reemplaza una subcadena por otra.

Adicionalmente, presentamos la función `input()`. Esta función detiene la ejecución para pedirle al usuario que ingrese un dato. Es crucial remarcar que **`input()` siempre devuelve un texto (`str`)**, sin importar si el usuario escribió números. Por ello, si requerimos operar matemáticamente con ese dato, debemos hacer una conversión explícita o *casting* usando `int()` o `float()`.

> [!CAUTION]
> **🚨 NOTA PARA EL INSTRUCTOR (NO LEER EN VOZ ALTA):**  
> Explica al grupo que en Ciencia de Datos no usaremos `input()` con frecuencia (porque procesaremos archivos masivos como CSVs o bases de datos), pero es vital comprender el concepto de conversión de tipos (*casting*).

#### Texto para una celda Markdown del notebook

## Métodos de texto y conversión de datos

- `.upper()` y `.lower()` cambian mayúsculas/minúsculas.
- `.strip()` quita espacios extras en los bordes.
- `.replace()` sustituye texto.
- `input()` recibe datos como `str`. Usamos `int()` o `float()` para convertirlos a números (*casting*).

#### Código para una celda de Colab

```python
# 1. Métodos de limpieza de texto
producto = "  Laptop Pro 15  "
producto_limpio = producto.strip().upper()
print("Producto limpio en mayúsculas:", f"'{producto_limpio}'")

# 2. Entrada de datos interactiva en Colab con input() y casting (conversión)
edad_ingresada = input("Por favor ingresa tu edad: ")  # Colab desplegará una caja de texto interactiva
edad_numero = int(edad_ingresada)                     # Convertimos de texto (str) a entero (int)

print(f"Texto ingresado: '{edad_ingresada}' | Tipo: {type(edad_ingresada)}")
print(f"Número convertido: {edad_numero} | Tipo: {type(edad_numero)}")
print(f"En 5 años tendrás: {edad_numero + 5} años")
```

#### Salida esperada

```text
Producto limpio en mayúsculas: 'LAPTOP PRO 15'
Por favor ingresa tu edad: 25
Texto ingresado: '25' | Tipo: <class 'str'>
Número convertido: 25 | Tipo: <class 'int'>
En 5 años tendrás: 30 años
```

---

## 2. Extracción avanzada en listas: Slicing y Métodos útiles (13 min)

### 2.1 Extracción de sublistas (Slicing)

#### Explicación para instructor

En la Clase 2 aprendimos a extraer un solo elemento mediante su índice (por ejemplo `lista[0]`). En Ciencia de Datos constantemente necesitamos seleccionar un **rango o subconjunto** de datos (por ejemplo, los primeros 3 registros o una muestra intermedia).

A esta técnica se le llama **Slicing** (rebanado). La sintaxis utiliza dos puntos: `lista[inicio:fin]`.
- `inicio`: el índice donde comienza la extracción (inclusivo).
- `fin`: el índice donde se detiene la extracción (**exclusivo**, es decir, no incluye ese índice).

Si omitimos el `inicio` (`lista[:3]`), Python asume desde el principio. Si omitimos el `fin` (`lista[2:]`), asume hasta el final de la lista. También se puede incluir un tercer parámetro para dar pasos (`lista[inicio:fin:paso]`).

#### Texto para una celda Markdown del notebook

## Slicing de listas

Extrae una porción de una lista usando `lista[inicio:fin]`.

- El valor de `inicio` se incluye.
- El valor de `fin` **NO** se incluye.
- `lista[:3]`: desde el inicio hasta el índice 2.
- `lista[2:]`: desde el índice 2 hasta el final.

#### Código para una celda de Colab

```python
ventas_semana = [100, 150, 200, 80, 250, 300, 190]

# Extraer los primeros 3 días
primeros_dias = ventas_semana[0:3]

# Extraer los últimos 2 días usando índices negativos
ultimos_dias = ventas_semana[-2:]

# Extraer días intermedios (del índice 2 al 4)
dias_centrales = ventas_semana[2:5]

print("Ventas completas:", ventas_semana)
print("Primeros 3 días (0:3):", primeros_dias)
print("Últimos 2 días (-2:):", ultimos_dias)
print("Días centrales (2:5):", dias_centrales)
```

#### Salida esperada

```text
Ventas completas: [100, 150, 200, 80, 250, 300, 190]
Primeros 3 días (0:3): [100, 150, 200]
Últimos 2 días (-2:): [300, 190]
Días centrales (2:5): [200, 80, 250]
```

> **Punto a remarcar:** Nota que `ventas_semana[0:3]` toma los elementos en las posiciones 0, 1 y 2. El 3 queda fuera.

### 2.2 Verificación de pertenencia y ordenamiento

#### Explicación para instructor

Además de extraer valores, con frecuencia necesitamos saber si un dato específico está dentro de una colección antes de procesarlo. Para esto usamos el operador de pertenencia `in`, el cual devuelve `True` o `False`.

También revisaremos dos métodos prácticos:
- `.sort()`: ordena los elementos de la lista de menor a mayor (o alfabéticamente) modificando la lista original. Se puede usar `.sort(reverse=True)` para orden descendente.
- `.pop()`: elimina y devuelve el último elemento de la lista (o el elemento en el índice indicado).

#### Texto para una celda Markdown del notebook

## Operaciones útiles en listas

- `valor in lista`: verifica si el valor existe en la lista (`True`/`False`).
- `lista.sort()`: ordena la lista de forma ascendente.
- `lista.pop()`: elimina y retorna el último elemento.

#### Código para una celda de Colab

```python
regiones = ["Norte", "Sur", "Centro", "Este"]

# Verificar si una región existe
print("¿Existe 'Sur' en regiones?:", "Sur" in regiones)
print("¿Existe 'Oeste' en regiones?:", "Oeste" in regiones)

# Ordenar lista
precios = [45.5, 12.0, 99.9, 23.4]
precios.sort()
print("Precios ordenados de menor a mayor:", precios)

# Eliminar el último precio
precio_removido = precios.pop()
print("Precio eliminado:", precio_removido)
print("Lista resultante de precios:", precios)
```

#### Salida esperada

```text
¿Existe 'Sur' en regiones?: True
¿Existe 'Oeste' en regiones?: False
Precios ordenados de menor a mayor: [12.0, 23.4, 45.5, 99.9]
Precio eliminado: 99.9
Lista resultante de precios: [12.0, 23.4, 45.5]
```

---

## 3. Tomando decisiones: Condicionales y Lógica (18 min)

### 3.1 Operadores de comparación y operadores lógicos

#### Explicación para instructor

Para que un programa tome decisiones autónomas, necesita comparar datos. Las comparaciones producen siempre un resultado booleano (`True` o `False`).

Los operadores de comparación son:
- `==`: igual a (no confundir con `=` que asigna variables).
- `!=`: diferente de.
- `>`, `<`, `>=`, `<=`: mayor, menor, mayor o igual, menor o igual.

Cuando requerimos evaluar múltiples criterios a la vez, usamos operadores lógicos:
- `and`: es `True` solo si **ambas** condiciones se cumplen.
- `or`: es `True` si **al menos una** condición se cumple.
- `not`: invierte el valor booleano (`not True` es `False`).

#### Texto para una celda Markdown del notebook

## Comparaciones y Lógica

- Comparadores: `==`, `!=`, `>`, `<`, `>=`, `<=`.
- Operadores lógicos:
  - `and`: verdadero si se cumplen ambas condiciones.
  - `or`: verdadero si se cumple al menos una condición.
  - `not`: invierte la condición.

#### Código para una celda de Colab

```python
temperatura = 28.5
humedad = 65

hace_calor = temperatura > 25
húmedo = humedad >= 60

print("¿Hace calor?:", hace_calor)
print("¿Hace calor Y está húmedo?:", hace_calor and húmedo)
print("¿Hace calor O la humedad es baja?:", hace_calor or humedad < 50)
```

#### Salida esperada

```text
¿Hace calor?: True
¿Hace calor Y está húmedo?: True
¿Hace calor O la humedad es baja?: True
```

### 3.2 Estructuras condicionales (`if`, `elif`, `else`)

#### Explicación para instructor

Un bloque condicional ejecuta distintas instrucciones según el resultado de una prueba lógica. 

En Python, la sintaxis utiliza la **sangría o indentación** (4 espacios o un tabulador). Todo lo que esté indentado debajo del `if`, `elif` o `else` pertenece a ese bloque.

- `if`: evalúa la primera condición. Si es `True`, ejecuta su bloque y omite los demás.
- `elif` (abreviación de *else if*): evalúa una condición secundaria si las anteriores fueron falsas. Se pueden poner varios `elif`.
- `else`: ejecuta su bloque si ninguna de las condiciones anteriores fue verdadera.

> [!CAUTION]
> **🚨 NOTA PARA EL INSTRUCTOR (CONEXIÓN DATA SCIENCE - NO LEER EN VOZ ALTA):**  
> Relaciona este concepto con el análisis de datos: por ejemplo, al clasificar automáticamente a un cliente como "Riesgo Alto", "Riesgo Medio" o "Riesgo Bajo" según sus métricas.

#### Texto para una celda Markdown del notebook

## Estructura condicional if / elif / else

Evalúa condiciones en orden de arriba a abajo. Se debe respetar la **indentación** (sangría) dentro de cada bloque.

```python
if condicion_1:
    # Código si condicion_1 es True
elif condicion_2:
    # Código si condicion_2 es True
else:
    # Código si ninguna condición fue True
```

#### Código para una celda de Colab

```python
score_credito = 680

if score_credito >= 750:
    nivel_riesgo = "Bajo"
    aprobado = True
elif score_credito >= 650:
    nivel_riesgo = "Medio"
    aprobado = True
else:
    nivel_riesgo = "Alto"
    aprobado = False

print(f"Resultado de evaluación:")
print(f"Score: {score_credito} | Riesgo: {nivel_riesgo} | Crédito aprobado: {aprobado}")
```

#### Salida esperada

```text
Resultado de evaluación:
Score: 680 | Riesgo: Medio | Crédito aprobado: True
```

> **Error común a prevenir:** Olvidar los dos puntos `:` al final de la línea del `if`/`elif`/`else` o perder la indentación en el código interno.

---

## 4. Estructuras de datos II: Diccionarios (12 min)

### 4.1 Crear y consultar un diccionario

#### Explicación para instructor

En la Clase 2 vimos las listas, donde los elementos se organizan por posición numérica (`0`, `1`, `2`). Pero cuando representamos información compleja (como la ficha de un paciente, las propiedades de un producto o una fila de una base de datos), es más claro acceder a los valores por un **nombre descriptivo o etiqueta**.

Un **Diccionario** guarda pares de datos bajo la estructura `llave: valor` (`key: value`).
- Se definen entre llaves `{}`.
- Cada llave está separada de su valor por dos puntos `:`.
- Los pares se separan por comas `,`.

Para acceder a un valor, escribimos el nombre del diccionario y la llave entre corchetes: `diccionario["llave"]`.

#### Texto para una celda Markdown del notebook

## Diccionarios

Un diccionario almacena datos asociados en pares `llave: valor` dentro de llaves `{}`.

Para consultar un valor usamos su llave entre corchetes: `diccionario["llave"]`.

#### Código para una celda de Colab

```python
# Crear un diccionario con datos de un empleado
empleado = {
    "nombre": "Elena Torres",
    "departamento": "Análisis de Datos",
    "edad": 31,
    "salario": 38500.0,
    "activo": True
}

print("Diccionario completo:", empleado)
print("Nombre del empleado:", empleado["nombre"])
print("Departamento:", empleado["departamento"])
```

#### Salida esperada

```text
Diccionario completo: {'nombre': 'Elena Torres', 'departamento': 'Análisis de Datos', 'edad': 31, 'salario': 38500.0, 'activo': True}
Nombre del empleado: Elena Torres
Departamento: Análisis de Datos
```

### 4.2 Modificación y métodos de diccionarios

#### Explicación para instructor

Los diccionarios son mutables. Podemos:
- Modificar un valor existente: `diccionario["llave"] = nuevo_valor`.
- Agregar una nueva llave: si asignamos un valor a una llave que no existía, Python la crea automáticamente.

Además, poseen tres métodos fundamentales para inspeccionar sus datos:
- `.keys()`: obtiene todas las llaves.
- `.values()`: obtiene todos los valores.
- `.items()`: obtiene los pares `(llave, valor)` como tuplas. *(Una **tupla** es una colección ordenada entre paréntesis `(a, b)` similar a una lista, pero **inmutable**, lo que significa que sus elementos no se pueden modificar tras crearse).*

> [!CAUTION]
> **🚨 NOTA PARA EL INSTRUCTOR (CONEXIÓN DATA SCIENCE - NO LEER EN VOZ ALTA):**  
> Enfatiza que un diccionario representa una fila o registro individual de una tabla. Cuando usemos la librería Pandas en la Clase 7, verán que un DataFrame es básicamente un conjunto de diccionarios alineados en columnas.

#### Texto para una celda Markdown del notebook

## Modificación y métodos de diccionarios

- Agregar/Modificar: `diccionario["llave"] = valor`
- `.keys()`: devuelve las llaves del diccionario.
- `.values()`: devuelve los valores del diccionario.
- `.items()`: devuelve los pares `(llave, valor)`.

#### Código para una celda de Colab

```python
empleado = {
    "nombre": "Elena Torres",
    "departamento": "Análisis de Datos",
    "salario": 38500.0
}

# Modificar valor existente
empleado["salario"] = 42000.0

# Agregar una nueva llave
empleado["ciudad"] = "Guadalajara"

print("Diccionario actualizado:", empleado)
print("Llaves disponibles:", list(empleado.keys()))
print("Valores almacenados:", list(empleado.values()))
```

#### Salida esperada

```text
Diccionario actualizado: {'nombre': 'Elena Torres', 'departamento': 'Análisis de Datos', 'salario': 42000.0, 'ciudad': 'Guadalajara'}
Llaves disponibles: ['nombre', 'departamento', 'salario', 'ciudad']
Valores almacenados: ['Elena Torres', 'Análisis de Datos', 42000.0, 'Guadalajara']
```

---

## 5. Ejercicio integrador de cierre (5 min)

### Explicación para instructor

Este ejercicio reúne los conceptos clave de la sesión: formateo con `f-strings`, extracción y evaluación de datos en un diccionario, y lógica condicional con `if/elif/else`.

> [!CAUTION]
> **🚨 DINÁMICA PARA EL INSTRUCTOR (NO LEER EN VOZ ALTA):**  
> Permite que el grupo intente primero resolverlo por su cuenta durante 3 a 5 minutos, o bien guíalos construyendo el código paso a paso según el nivel del grupo.

### Texto para una celda Markdown del notebook

## Ejercicio integrador: Evaluación de inventario de producto

Dado un diccionario con la información de un producto en bodega:
1. Muestra un resumen del producto formateado con `f-strings`.
2. Determina el estado del stock mediante condicionales:
   - Si el stock es menor a 10: "Stock Crítico".
   - Si el stock está entre 10 y 30: "Stock Moderado".
   - Si el stock es mayor a 30: "Stock Óptimo".
3. Muestra el estado asignado.

### Código para una celda de Colab

```python
producto = {
    "sku": "PROD-9082",
    "nombre": "Monitor 27 Pulgadas",
    "precio": 4500.50,
    "stock": 8
}

# 1. Reporte formateado
print(f"--- REVISIÓN DE INVENTARIO ---")
print(f"Producto: {producto['nombre']} ({producto['sku']})")
print(f"Precio unitario: ${producto['precio']:.2f}")

# 2. Evaluación lógica de stock
if producto["stock"] < 10:
    estado_stock = "CRÍTICO - Requerir reabastecimiento urgente"
elif producto["stock"] <= 30:
    estado_stock = "MODERADO - Cantidad aceptable"
else:
    estado_stock = "ÓPTIMO - Inventario suficiente"

# 3. Impresión del estado
print(f"Unidades disponibles: {producto['stock']}")
print(f"Estado de inventario: {estado_stock}")
```

### Salida esperada

```text
--- REVISIÓN DE INVENTARIO ---
Producto: Monitor 27 Pulgadas (PROD-9082)
Precio unitario: $4500.50
Unidades disponibles: 8
Estado de inventario: CRÍTICO - Requerir reabastecimiento urgente
```

---

## Cierre de la sesión (5 min)

### Explicación para instructor

Recapitula brevemente:
Hoy aprendimos a manipular cadenas y formatearlas con `f-strings`, extrajimos subconjuntos de datos de listas con *slicing*, construimos lógica condicional con `if/elif/else` para la toma de decisiones, y organizamos registros de información estructurados con diccionarios (`dict`).

En la siguiente sesión (Clase 4) cerraremos los fundamentos de Python aprendiendo a automatizar tareas con bucles (`for` y `while`), simplificar código con *list comprehensions*, empaquetar soluciones en **funciones (`def`)** e importar librerías nativas.

### Texto para una celda Markdown del notebook

## Lo que aprendimos en la Clase 3

- Formatear texto y números con `f-strings` e incrustar variables.
- Usar métodos de texto (`.upper()`, `.strip()`, `.replace()`) y convertir tipos de datos (`int()`, `float()`).
- Extraer rangos de listas mediante *slicing* (`lista[inicio:fin]`).
- Construir estructuras de decisión con `if`, `elif` y `else` usando operadores lógicos.
- Almacenar y modificar registros estructurados `llave: valor` con diccionarios.

En la Clase 4 aprenderemos a automatizar tareas repetitivas con bucles y crear nuestras propias funciones reutilizables.
