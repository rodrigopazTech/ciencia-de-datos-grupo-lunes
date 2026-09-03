# Clase 5: Modularidad de Código y Entorno Local (Jupyter Lab)

**Duración sugerida:** 60 minutos  
**Modalidad:** práctica en Google Colab (primera mitad) y local en Jupyter Lab (segunda mitad)  
**Objetivo:** que el alumnado aprenda a empaquetar código reutilizable en Funciones, importar y renombrar Módulos externos, e instale y configure Anaconda y Jupyter Lab para ejecutar su primer código de manera local en su computadora.

---

### 🎨 Apoyo Visual para el Aprendizaje
* **Concepto:** Una función representada como una máquina industrial (Entrada: materias primas labeled 'Parameters/Arguments' $\rightarrow$ Procesamiento $\rightarrow$ Salida: producto terminado con la etiqueta `return`). Un Módulo como una caja de herramientas prefabricadas.
* **Prompt para Generar Imagen con IA (Midjourney/DALL-E 3):**
  > *A 3D concept design of a sleek, futuristic factory machine. Raw materials (labeled 'Parameters/Arguments') enter on the left, the machine has gears and processors (labeled 'Function logic'), and a finished glowing product (labeled 'Return Value') exits on the right. Minimalist design, neon cyan and deep blue lighting, professional slide graphics style.*

---

## 1. Modularidad: Funciones (`def`) (20 min)

### 1.1 Estructura de una función

#### Explicación para instructor

Una **función** es un bloque de código organizado y reutilizable al que le asignamos un nombre.
- Permite evitar la repetición de código (filosofía DRY: Don't Repeat Yourself).
- Se define con la palabra reservada `def nombre_funcion(parametros):`.
- El bloque de código interno debe estar indentado.

#### Texto para una celda Markdown del notebook

## Funciones en Python

Una función agrupa código reutilizable bajo un nombre específico.
- Se crea usando `def nombre_funcion(parametros):`.
- Se ejecuta ("llama") escribiendo su nombre y pasando los argumentos entre paréntesis: `nombre_funcion(argumentos)`.

#### Código para una celda de Colab

```python
# 1. Definición de la función
def saludar_usuario(nombre):
    print(f"¡Hola, {nombre}! Bienvenido a la sesión de hoy.")

# 2. Llamado a la función con diferentes argumentos
saludar_usuario("Valeria")
saludar_usuario("Mateo")
```

#### Salida esperada

```text
¡Hola, Valeria! Bienvenido a la sesión de hoy.
¡Hola, Mateo! Bienvenido a la sesión de hoy.
```

### 1.2 Retorno de valores: `return` frente a `print()`

#### Explicación para instructor

Un error común al iniciar es confundir `print()` y `return`:
- `print()` solo **muestra** un texto en pantalla de forma visual, pero el programa no puede almacenar ni usar ese resultado más adelante.
- `return` **devuelve** el resultado calculado de vuelta al flujo principal del programa, permitiendo guardarlo en una variable o pasarlo a otra función.

#### Texto para una celda Markdown del notebook

## Retorno de valores

- `print()` muestra información visualmente en la salida.
- `return` entrega el resultado del cálculo para que pueda guardarse en una variable y seguir operando con él en el programa.

#### Código para una celda de Colab

```python
# Función que calcula el promedio
def calcular_promedio(calificaciones):
    suma = sum(calificaciones)
    cantidad = len(calificaciones)
    return suma / cantidad  # Retorna el valor decimal

# Uso del valor retornado
mis_calificaciones = [8.5, 9.0, 7.8]
promedio_final = calcular_promedio(mis_calificaciones)

# Ahora podemos usar promedio_final en cualquier parte del código
print(f"Promedio calculado: {promedio_final:.2f}")
if promedio_final >= 8.0:
    print("Estado: Aprobado")
```

#### Salida esperada

```text
Promedio calculado: 8.43
Estado: Aprobado
```

---

## 2. Importación de Módulos (15 min)

### Explicación para instructor

Un **Módulo** es una librería o archivo de código que contiene funciones creadas por otros desarrolladores (o provistas nativamente por Python) que podemos importar para usar en nuestro programa.
Para importarlas, usamos la palabra reservada `import`. Contamos con variaciones:
- `import modulo`: importa todo el módulo. Para usar una función escribimos `modulo.funcion()`.
- `import modulo as alias`: asigna un alias corto para no escribir el nombre largo (ej. `import random as rd`). Esta es la base para NumPy (`import numpy as np`) y Pandas (`import pandas as pd`).
- `from modulo import funcion`: importa únicamente una función específica del módulo, lo que optimiza la memoria.

#### Texto para una celda Markdown del notebook

## Importar Módulos y Librerías

Expandimos las capacidades de Python importando librerías externas:
- `import modulo`
- `import modulo as alias` (asigna un nombre corto reutilizable)
- `from modulo import funcion` (carga una función específica)

#### Código para una celda de Colab

```python
import math
import random as rd
from datetime import datetime

# 1. Uso de math (funciones matemáticas)
numero = 16
raiz = math.sqrt(numero)
print(f"Raíz cuadrada de {numero}: {raiz}")

# 2. Uso de random con alias
dado = rd.randint(1, 6)
print(f"Lanzamiento de dado (aleatorio): {dado}")

# 3. Uso de función importada selectivamente
print("Fecha y hora actual:", datetime.now())
```

#### Salida esperada

```text
Raíz cuadrada de 16: 4.0
Lanzamiento de dado (aleatorio): 4
Fecha y hora actual: 2026-08-06 12:49:38.123456
```

---

## 3. Configuración del Entorno Local: Anaconda y Jupyter Lab (15 min)

### Explicación para instructor

Guía al grupo en el entendimiento e instalación de su entorno local (es recomendable haberles pedido la instalación previa de Anaconda, o usar este espacio para demostrar cómo se descarga y se abre).
- **¿Qué es Anaconda?:** Es una distribución libre y abierta orientada a Ciencia de Datos y Machine Learning. Contiene el intérprete de Python, un gestor de paquetes (`conda`) y las librerías más importantes (NumPy, Pandas, Matplotlib, Scikit-Learn) preinstaladas.
- **¿Qué es Jupyter Lab?:** La interfaz estándar local para crear y compartir notebooks. Funciona de manera idéntica a Google Colab, pero se ejecuta directamente en el disco duro local, permitiendo procesar archivos de manera privada y sin límites de tiempo de sesión en la nube.
- **Paso a paso de apertura:**
  1. Abrir *Anaconda Navigator* y hacer clic en Launch en **Jupyter Lab** (o abrir la terminal y escribir `jupyter lab`).
  2. Mostrar cómo se navega por el directorio local para crear un nuevo notebook `.ipynb`.

---

## 4. Taller de Cierre: Ejecución Local en Jupyter Lab (10 min)

### Explicación para instructor

Instruye a los alumnos a abrir Jupyter Lab en sus computadoras y crear su primer notebook local. El ejercicio consiste en empaquetar una función y usar un módulo.

*Nota:* Si algún alumno presenta problemas técnicos con su instalación local, puede realizar la práctica en Google Colab para no retrasar la clase y recibir soporte técnico al finalizar.

#### Actividad para el alumno (Jupyter Lab Local)

Crea un nuevo notebook en Jupyter Lab local y escribe un programa que:
1. Importe la función `randint` de la librería nativa `random` con el alias `rd`.
2. Defina una función personalizada llamada `simular_dado_personalizado(lados)` que reciba el número de lados del dado como parámetro y devuelva un número aleatorio entre 1 y ese parámetro.
3. Ejecute la función localmente con un dado de 20 lados (`lados = 20`) e imprima el resultado.

#### Código para el notebook

```python
import random as rd

def simular_dado_personalizado(lados):
    resultado = rd.randint(1, lados)
    return resultado

# Simular lanzamiento
lados_dado = 20
tiro = simular_dado_personalizado(lados_dado)

print(f"Lanzando un dado de {lados_dado} lados...")
print(f"Resultado del tiro: {tiro}")
```

#### Salida esperada (en Jupyter Lab local)

```text
Lanzando un dado de 20 lados...
Resultado del tiro: 14
```

---

## Cierre de la sesión (2 min)

Recapitula brevemente:
Hoy cerramos la base de fundamentos de Python aprendiendo a modularizar el código con **Funciones** y a incorporar librerías usando **Módulos**. Adicionalmente, dimos el gran paso de configurar y ejecutar nuestro propio servidor de **Jupyter Lab** de manera local.

A partir de la siguiente sesión (Clase 6) entramos de lleno al Módulo 2 de Ciencia de Datos profesional, comenzando a manipular conjuntos de datos masivos con la librería reina del cómputo numérico: **NumPy**.
