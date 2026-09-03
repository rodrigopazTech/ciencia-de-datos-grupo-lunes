# Clase 2: Fundamentos de Python para Ciencia de Datos

**Duración sugerida:** 60 minutos  
**Modalidad:** práctica en Google Colab  
**Objetivo:** que el alumnado escriba, ejecute y lea código básico en Python; use variables y tipos de datos, aplique operadores y manipule una lista sencilla.

> **Dinámica recomendada:** abre un notebook nuevo en Google Colab. Para cada bloque, primero comparte la explicación para instructor, después crea una celda de texto con el resumen y, finalmente, escribe y ejecuta el código junto con el grupo. Invítalos a cambiar valores y volver a ejecutar.

---

## 1. Introducción a Python y Google Colab (10 min)

### Explicación para instructor

Python es un lenguaje de programación: una forma de escribir instrucciones para que una computadora resuelva tareas. Se caracteriza por una sintaxis legible; muchas instrucciones se parecen a frases sencillas y no requieren demasiados símbolos.

En ciencia de datos se usa para limpiar información, calcular medidas, crear gráficas, entrenar modelos y automatizar tareas. Más adelante trabajaremos con librerías como NumPy y pandas, pero primero necesitamos entender cómo Python representa y transforma información.

Google Colab es un cuaderno interactivo que se ejecuta en el navegador. un notebook combina dos tipos de celdas: las celdas de texto documentan ideas y las celdas de código ejecutan Python. Esto resulta útil para análisis de datos porque permite conservar juntos la explicación, el procedimiento y el resultado.

Aclara que el código se ejecuta de arriba hacia abajo. Si una celda usa una variable creada en otra, primero debe ejecutarse la celda donde esa variable fue definida.

### Texto para una celda Markdown del notebook

## Python y Google Colab

Python es un lenguaje muy usado en ciencia de datos por ser legible y contar con muchas librerías. En Colab trabajamos con:

- Celdas de **texto** para explicar.
- Celdas de **código** para ejecutar Python.

Ejecuta una celda con el botón ▶ o con `Shift + Enter`.

### Código para una celda de Colab

```python
print("¡Hola! Hoy comenzamos a programar con Python.")
print("Python también nos ayudará a analizar datos.")
```

### Salida esperada

```text
¡Hola! Hoy comenzamos a programar con Python.
Python también nos ayudará a analizar datos.
```

> **Pregunta para el grupo:** ¿qué cambiaría si reemplazamos el texto entre comillas por su nombre?

---

## 2. Variables y tipos de datos (20 min)

### 2.1 Variables: nombres para guardar información

#### Explicación para instructor

Una variable es un nombre que usamos para guardar un valor y poder reutilizarlo. En vez de escribir un número muchas veces, le damos un nombre descriptivo. El signo `=` asigna el valor de la derecha al nombre de la izquierda; no significa una igualdad matemática.

Python tiene tipado dinámico: no hace falta anunciar previamente si una variable guardará un número o texto. Python identifica el tipo según el valor asignado. Una misma variable puede recibir un valor nuevo, aunque conviene mantener nombres claros y un uso coherente.

Enfatiza las buenas prácticas: nombres en minúsculas, palabras separadas con guion bajo (`snake_case`), sin espacios ni acentos y que describan el contenido. Por ejemplo, `numero_alumnos` comunica mejor que `x`.

#### Texto para una celda Markdown del notebook

## Variables

Una variable guarda información bajo un nombre. Usamos `=` para asignar un valor.

Usa nombres descriptivos en `snake_case`, por ejemplo: `numero_alumnos`.

### Código para una celda de Colab

```python
nombre_curso = "Introducción a Ciencia de Datos"
numero_alumnos = 25

print(nombre_curso)
print("Alumnos inscritos:", numero_alumnos)
```

### Salida esperada

```text
Introducción a Ciencia de Datos
Alumnos inscritos: 25
```

> **Práctica rápida:** pide que cambien el nombre del curso y el número de alumnos por datos ficticios propios.

### 2.2 Tipos elementales de datos

#### Explicación para instructor

Los valores tienen tipos. Los cuatro básicos de esta sesión son:

- `int`: números enteros, como cantidad de alumnos o edad.
- `float`: números con decimales, como una temperatura o un promedio. En Python se usa punto, no coma: `8.5`.
- `str`: texto o cadena de caracteres; siempre va entre comillas simples o dobles.
- `bool`: valores lógicos: `True` o `False`. La primera letra va en mayúscula.

La función `type()` permite consultar el tipo de un valor. Esto será importante al trabajar con datos reales: una columna que parece numérica puede haber sido leída como texto y requerir una conversión.

#### Texto para una celda Markdown del notebook

## Tipos de datos

- `int`: entero, por ejemplo `25`.
- `float`: decimal, por ejemplo `8.5`.
- `str`: texto entre comillas, por ejemplo `"Ana"`.
- `bool`: valor lógico: `True` o `False`.

Usamos `type()` para conocer el tipo de un valor.

### Código para una celda de Colab

```python
edad = 21
promedio = 9.4
nombre = "Mariana"
curso_activo = True

print("edad:", edad, "| tipo:", type(edad))
print("promedio:", promedio, "| tipo:", type(promedio))
print("nombre:", nombre, "| tipo:", type(nombre))
print("curso_activo:", curso_activo, "| tipo:", type(curso_activo))
```

### Salida esperada

```text
edad: 21 | tipo: <class 'int'>
promedio: 9.4 | tipo: <class 'float'>
nombre: Mariana | tipo: <class 'str'>
curso_activo: True | tipo: <class 'bool'>
```

> **Punto a remarcar:** `"21"` se ve como un número, pero al llevar comillas es texto (`str`).

### 2.3 Mostrar resultados con `print()`

#### Explicación para instructor

`print()` muestra información en la salida de la celda. Es la primera herramienta para observar qué está haciendo un programa. Puede recibir varios valores separados por comas; Python los mostrará con espacios entre ellos.

Para una introducción conviene usar `print()` de forma explícita, aunque Colab también muestra automáticamente el último valor de una celda. Así el resultado es más claro para quien está aprendiendo.

#### Texto para una celda Markdown del notebook

## Mostrar información

La función `print()` muestra valores y mensajes en la salida de una celda.

### Código para una celda de Colab

```python
ciudad = "Ciudad de México"
temperatura = 24.5

print("Ciudad:", ciudad)
print("Temperatura registrada:", temperatura, "°C")
```

### Salida esperada

```text
Ciudad: Ciudad de México
Temperatura registrada: 24.5 °C
```

---

## 3. Operadores básicos (10 min)

### 3.1 Operadores aritméticos

#### Explicación para instructor

Los operadores permiten transformar valores. Con números, Python ofrece las operaciones conocidas: suma (`+`), resta (`-`) y multiplicación (`*`). También incluye:

- `/`: división normal; produce un resultado decimal.
- `//`: división entera; conserva solo la parte entera del cociente.
- `%`: módulo o residuo; indica lo que sobra tras una división.
- `**`: potencia.

Relaciona los ejemplos con datos: dividir el total de registros entre grupos, obtener un promedio o verificar si una cantidad es par mediante el residuo.

#### Texto para una celda Markdown del notebook

## Operadores aritméticos

Python puede sumar, restar, multiplicar, dividir y calcular potencias.

`/` conserva decimales, `//` obtiene la parte entera y `%` obtiene el residuo.

### Código para una celda de Colab

```python
total_respuestas = 25
equipos = 4

print("Suma:", 8 + 3)
print("Resta:", 8 - 3)
print("Multiplicación:", 8 * 3)
print("División:", total_respuestas / equipos)
print("División entera:", total_respuestas // equipos)
print("Residuo:", total_respuestas % equipos)
print("Potencia:", 2 ** 3)
```

### Salida esperada

```text
Suma: 11
Resta: 5
Multiplicación: 24
División: 6.25
División entera: 6
Residuo: 1
Potencia: 8
```

### 3.2 Operadores con texto

#### Explicación para instructor

El significado de un operador depende del tipo de datos. Con textos, `+` concatena o une cadenas y `*` las repite. No se puede sumar directamente texto y número; por ahora, muéstrales que cada operación requiere valores compatibles.

#### Texto para una celda Markdown del notebook

## Operadores con texto

Con cadenas de texto, `+` une textos y `*` los repite.

### Código para una celda de Colab

```python
saludo = "Hola"
nombre = " Sofía"

print(saludo + nombre)
print("Python " * 3)
```

### Salida esperada

```text
Hola Sofía
Python Python Python 
```

> **Reto breve:** cambia la cantidad de repeticiones y observa qué sucede.

---

## 4. El puente hacia los datos: listas (20 min)

### 4.1 Crear una lista

#### Explicación para instructor

Una lista es una colección ordenada de valores. Se escribe entre corchetes y sus elementos se separan con comas. Es una estructura fundamental porque los datos suelen llegar en grupos: calificaciones, ventas diarias, nombres de clientes o mediciones de sensores.

Las listas pueden contener valores de distintos tipos, aunque en ciencia de datos normalmente procuraremos que una colección represente una sola característica y use valores del mismo tipo. Las listas son mutables: se pueden modificar después de crearlas.

Más adelante, los arreglos de NumPy y las columnas de pandas resolverán problemas más avanzados, pero la idea de reunir y acceder a varios valores comienza aquí.

#### Texto para una celda Markdown del notebook

## Listas

Una lista guarda varios valores ordenados entre corchetes: `[ ]`.

Las listas pueden modificarse y son el primer paso para trabajar con colecciones de datos.

### Código para una celda de Colab

```python
calificaciones = [8.5, 9.0, 7.8, 10.0]
datos_mezclados = ["Ana", 20, True]

print("Calificaciones:", calificaciones)
print("Lista con distintos tipos:", datos_mezclados)
```

### Salida esperada

```text
Calificaciones: [8.5, 9.0, 7.8, 10.0]
Lista con distintos tipos: ['Ana', 20, True]
```

### 4.2 Acceder a elementos mediante índices

#### Explicación para instructor

Cada elemento de una lista tiene una posición llamada índice. En Python, el conteo inicia en cero: el primer elemento tiene índice `0`, el segundo índice `1`, y así sucesivamente. Para acceder, escribimos el nombre de la lista seguido del índice entre corchetes.

También existen índices negativos: `-1` es el último elemento, `-2` el anterior. Esta convención aparece de forma frecuente al revisar el registro más reciente de una colección.

#### Texto para una celda Markdown del notebook

## Índices en listas

Los índices indican la posición de un elemento y comienzan en `0`.

- `lista[0]`: primer elemento.
- `lista[-1]`: último elemento.

### Código para una celda de Colab

```python
calificaciones = [8.5, 9.0, 7.8, 10.0]

print("Primera calificación:", calificaciones[0])
print("Tercera calificación:", calificaciones[2])
print("Última calificación:", calificaciones[-1])
```

### Salida esperada

```text
Primera calificación: 8.5
Tercera calificación: 7.8
Última calificación: 10.0
```

> **Error común que puedes anticipar:** `calificaciones[4]` falla porque la lista tiene cuatro elementos y sus índices válidos son `0`, `1`, `2` y `3`.

### 4.3 Tamaño y modificación de una lista

#### Explicación para instructor

La función `len()` cuenta cuántos elementos contiene una lista. El método `.append()` agrega un elemento al final. Un método es una acción disponible para un tipo de objeto; en este caso, se escribe después del nombre de la lista.

Destaca que `.append()` modifica la lista original. Por eso imprimimos la lista después de usarlo: así comprobamos el cambio. Esta costumbre de inspeccionar resultados será esencial al limpiar y transformar datos.

#### Texto para una celda Markdown del notebook

## Tamaño y cambios en una lista

`len(lista)` cuenta elementos.  
`lista.append(valor)` agrega un valor al final de la lista.

### Código para una celda de Colab

```python
ventas_diarias = [120, 150, 90]

print("Ventas iniciales:", ventas_diarias)
print("Número de días registrados:", len(ventas_diarias))

ventas_diarias.append(175)

print("Ventas después de agregar un día:", ventas_diarias)
print("Número de días ahora:", len(ventas_diarias))
```

### Salida esperada

```text
Ventas iniciales: [120, 150, 90]
Número de días registrados: 3
Ventas después de agregar un día: [120, 150, 90, 175]
Número de días ahora: 4
```

---

## 5. Ejercicio integrador de cierre (5 min)

### Explicación para instructor

Este ejercicio conecta los temas de la sesión sin introducir conceptos nuevos. Primero deja que el grupo intente escribirlo; después construyan una posible solución. Recuérdales que no hay problema si necesitan consultar los ejemplos anteriores: programar también consiste en buscar patrones y reutilizar soluciones.

### Texto para una celda Markdown del notebook

## Ejercicio: registro de temperaturas

Tenemos temperaturas registradas durante tres días. Muestra:

1. La lista completa.
2. La primera y la última temperatura.
3. Cuántos registros hay.
4. La lista después de agregar una temperatura nueva.

### Código para una celda de Colab

```python
temperaturas = [22.5, 24.0, 23.2]

print("Temperaturas registradas:", temperaturas)
print("Primera temperatura:", temperaturas[0])
print("Última temperatura:", temperaturas[-1])
print("Cantidad de registros:", len(temperaturas))

temperaturas.append(25.1)
print("Registro actualizado:", temperaturas)
```

### Salida esperada

```text
Temperaturas registradas: [22.5, 24.0, 23.2]
Primera temperatura: 22.5
Última temperatura: 23.2
Cantidad de registros: 3
Registro actualizado: [22.5, 24.0, 23.2, 25.1]
```

---

## Cierre de la sesión (5 min)

### Explicación para instructor

Recapitula: Python ejecuta instrucciones; las variables guardan valores; los tipos determinan cómo se comportan esos valores; los operadores realizan transformaciones; y las listas organizan varios datos. Con estos fundamentos, la siguiente clase podrá incorporar decisiones (`if`), repeticiones (`for` y `while`) y funciones.

Conecta explícitamente con ciencia de datos: una lista de calificaciones o temperaturas ya representa un pequeño conjunto de datos. Las herramientas que verán después permitirán hacer operaciones similares, pero sobre miles o millones de registros.

### Texto para una celda Markdown del notebook

## Lo que aprendimos hoy

- Ejecutar código en Google Colab.
- Guardar valores en variables.
- Reconocer `int`, `float`, `str` y `bool`.
- Usar operadores básicos.
- Crear, consultar y modificar listas.

En la siguiente sesión aprenderemos a tomar decisiones y repetir tareas con Python.
