# Tarea Clase 5: Uso de Librerías y Configuración de Entorno Local (Grupo 1)

¡Hola! En esta tarea pondremos en práctica el uso de librerías básicas (`import`) en Python y daremos nuestros primeros pasos ejecutando código de manera local en nuestras computadoras con **Anaconda** y **Jupyter Lab**.

Esta tarea se divide en dos partes sencillas guiadas paso a paso:
1. **Parte 1: Práctica en Google Colab** (Uso de librerías, bucles y condicionales).
2. **Parte 2: Configuración del Entorno Local** (Instalación de Anaconda y Jupyter Lab).

---

## 📝 Parte 1: Ejercicios Guiados (Google Colab)

Crea un nuevo cuaderno en Google Colab con el nombre `Tarea_Clase_5_NombreApellido.ipynb` y sigue las instrucciones para resolver los siguientes ejercicios:

### Ejercicio 1: Números Aleatorios y Matemáticas (Uso de `import`)
Vamos a practicar cómo importar librerías nativas de Python y usar sus funciones básicas.

1. **Paso 1:** En una celda de código, importa la librería `random` y la librería `math`.
2. **Paso 2:** Genera un número entero aleatorio entre 1 y 100 usando la función `random.randint(1, 100)` y guárdalo en una variable llamada `numero_secreto`.
3. **Paso 3:** Calcula la raíz cuadrada de `numero_secreto` usando `math.sqrt()` y guarda el resultado en una variable llamada `raiz_cuadrada`.
4. **Paso 4:** Imprime el resultado usando un texto con formato (`f-string`) que diga exactamente lo siguiente:
   *`"El número generado de forma aleatoria es X y su raíz cuadrada es Y"`* (donde X y Y son los valores de tus variables).

---

### Ejercicio 2: Clasificación de Temperaturas (Bucles y Condicionales)
Vamos a recorrer una lista de datos y clasificar cada elemento usando lógica condicional.

1. **Paso 1:** Crea una lista llamada `temperaturas` con los siguientes valores: `[15, 32, 24, 12, 28]`.
2. **Paso 2:** Escribe un bucle `for` para recorrer uno por uno los elementos de la lista `temperaturas`.
3. **Paso 3:** Dentro del bucle, utiliza condicionales (`if / else`) para evaluar el valor de cada temperatura:
   - Si la temperatura es **menor a 20**, clasifícala como `"Clima Frío"`.
   - Si la temperatura es **20 o mayor**, clasifícala como `"Clima Cálido"`.
4. **Paso 4:** Imprime el resultado de cada evaluación dentro del bucle con un mensaje que diga:
   *`"Temperatura de X grados: Clima Frío / Cálido"`*.

---

## 💻 Parte 2: Instalación de Anaconda y Jupyter Lab (Entorno Local)

Para nuestras siguientes clases, utilizaremos una herramienta profesional instalada en tu propia computadora llamada **Jupyter Lab**. Sigue estos pasos para configurarlo:

1. **Paso 1: Instalación:** Abre el archivo de la **Guía de Instalación de Anaconda** (`guia_instalacion_anaconda.md`) adjunto en el correo y sigue las instrucciones específicas para tu computadora (Windows, Mac o Linux).
2. **Paso 2: Abrir Jupyter Lab:** Una vez instalado Anaconda, abre la aplicación **Anaconda Navigator** y haz clic en el botón **Launch** dentro de la tarjeta de **Jupyter Lab** (o si prefieres la terminal, escribe `jupyter lab`).
3. **Paso 3: Crear tu Notebook:** En Jupyter Lab, crea un nuevo cuaderno (Notebook) en blanco y cámbiale el nombre a `mi_entorno_local.ipynb`.
4. **Paso 4: Probar el código:** Escribe y ejecuta el siguiente código en la primera celda:
   ```python
   import sys
   print("¡Mi entorno local de Anaconda y Jupyter Lab está listo!")
   print("Versión de Python instalada:", sys.version)
   ```
5. **Paso 5: Evidencia:** Toma una captura de pantalla completa de tu pantalla donde se vea la ventana de tu navegador con **Jupyter Lab** abierto y el código anterior ejecutado con éxito.

---

## 📬 Instrucciones de Entrega

Responde al correo enviado por tu instructor adjuntando únicamente:
1. El archivo `.ipynb` con los ejercicios de Google Colab (descárgalo en Colab desde *Archivo > Descargar > Descargar .ipynb*).
2. La captura de pantalla de tu Jupyter Lab local funcionando.

**Fecha límite de entrega:** [Insertar fecha y hora]
