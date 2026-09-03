# Plan de Contenido Redes Sociales (Grupo 1: Ciencia de Datos)

Este documento contiene la planificación y los prompts detallados para generar un **Carrusel de LinkedIn** y un **Video de TikTok/Reels** para cada una de las clases del **Grupo 1 (Ciencia de Datos)** a partir de la Clase 6, omitiendo los contenidos redundantes que ya se programaron en el Grupo 2.

---

## 📊 Módulo 2: Cómputo Numérico y Manipulación de Datos (Clases 6 a 9)

### 📂 Clase 6: NumPy Fundamental y Análisis Estadístico Vectorizado
* **Objetivo:** Demostrar la velocidad del cómputo vectorizado frente al bucle tradicional y el filtrado por dimensiones.

#### 👔 Carrusel de LinkedIn (Imágenes)
* **Tema:** "Por qué dejar de usar bucles 'for' en grandes volúmenes de datos"
* **Estilo Visual:** *Sleek 3D comparison, slow runner vs. jet plane, neon metrics.*
* **Estructura de Slides:**
  * **Slide 1 (Portada):** "La velocidad de NumPy: Por qué los loops normales te retrasan." (Visual: Una pista de carreras donde un auto deportivo de neón pasa al lado de un corredor lento).
  * **Slide 2:** "El problema del bucle for." (Python tradicional procesa los datos uno por uno. Ejecutar lógica en 1 millón de filas calienta tu CPU y retrasa tu entrega).
  * **Slide 3:** "Cómputo Vectorizado." (NumPy corre sobre lenguaje C a bajo nivel, aplicando operaciones a arreglos completos de forma simultánea).
  * **Slide 4:** "Cifras de Rendimiento." (Un loop tarda 3.5 segundos en tu máquina; la operación vectorizada de NumPy toma 0.003 segundos).
  * **Slide 5:** "Indexación y Máscaras 2D." (Filtrar y segmentar matrices multidimensionales usando máscaras lógicas en lugar de condiciones anidadas).
  * **Slide 6:** "El Eslabón del Científico de Datos." (NumPy es la base matemática imprescindible para alimentar algoritmos y redes neuronales en producción).
  * **Slide 7 (CTA):** "Comenta **'SPEED'** y te comparto el script para que pruebes el rendimiento de NumPy frente a loops locales."

#### 📱 Video de TikTok/Reels (Motion Graphics)
* **Tema:** "Bucle for vs. NumPy (La carrera de velocidad)"
* **Duración:** 60 segundos (6 escenas de 10s).
* **Guión de Escenas:**
  * **Escena 1 (0-10s):** *Visual:* Un peatón caminando despacio frente a un avión de combate despegando. *Voz en Off:* "¿Sabías que procesar datos con bucles tradicionales es como ir a pie, cuando tu computadora podría estar volando?"
  * **Escena 2 (10-20s):** *Visual:* Código Python con un loop iterando registro por registro de forma lenta. *Voz en Off:* "Python estándar procesa registros uno a uno. Si tu base de datos tiene un millón de renglones, esto puede tomar valiosos segundos."
  * **Escena 3 (20-30s):** *Visual:* El avión (representando NumPy) escaneando e integrando una matriz completa de una sola vez. *Voz en Off:* "NumPy utiliza cómputo vectorizado. Aplica cálculos en toda la colección de datos de golpe usando optimizaciones a bajo nivel."
  * **Escena 4 (30-40s):** *Visual:* Marcador de velocidad en pantalla: Loop = 3.5s vs NumPy = 0.003s. *Voz en Off:* "¡En las pruebas de rendimiento, NumPy llega a ser hasta mil veces más rápido que un bucle tradicional!"
  * **Escena 5 (40-50s):** *Visual:* Una cuadrícula lógica filtrando matrices bidimensionales. *Voz en Off:* "Es la herramienta fundacional que todo científico de datos necesita para preparar datos antes de entrenar Inteligencia Artificial."
  * **Escena 6 (50-60s):** *Visual:* CTA de seguidor. *Voz en Off:* "Aprende programación de alto rendimiento. ¡Síguenos para la siguiente sesión!"

---

### 📂 Clase 7: Introducción a Pandas & Estructura de DataFrames
> ⚠️ **Este material ya se va a generar (ver Clase 5 del Grupo 2)**  
> *El contenido sobre Series, DataFrames, `pd.read_csv()` e inspección general con `.head()`, `.info()` y `.describe()` ya está cubierto en el plan del Grupo 2.*

---

### 📂 Clase 8: Limpieza y Filtrado de Datos con Pandas
> ⚠️ **Este material ya se va a generar (ver Clases 6 y 7 del Grupo 2)**  
> *El contenido sobre tratamiento de nulos (`isna`, `dropna`, `fillna`), duplicados, casting y selección con `.loc` e `.iloc` ya está cubierto en el plan del Grupo 2.*

---

### 📂 Clase 9: Transformación, Agregación y Uniones en Pandas
* **Objetivo:** Enseñar transformaciones condicionales complejas de columnas usando `.apply()`.

#### 👔 Carrusel de LinkedIn (Imágenes)
* **Tema:** "El superpoder oculto de Pandas: .apply()"
* **Estilo Visual:** *Conveyor belt with automated stamping machines, coding brackets glowing.*
* **Estructura de Slides:**
  * **Slide 1 (Portada):** "Cómo aplicar funciones complejas a tus columnas con Pandas." (Visual: Un brazo robótico aplicando un sello a celdas digitales).
  * **Slide 2:** "El límite de las operaciones básicas." (Multiplicar o sumar columnas es fácil, pero ¿qué pasa si tu regla requiere condicionales lógicos anidados?).
  * **Slide 3:** "Crear tu Función." (Escribe una función nativa en Python con `def`, parámetros y la lógica de negocio requerida).
  * **Slide 4:** "El comando .apply()." (Pasa tu función personalizada a toda la columna en una sola línea de código limpia).
  * **Slide 5:** "Caso de Uso." (Clasificar el riesgo crediticio de miles de clientes basándote en múltiples variables complejas).
  * **Slide 6:** "Ventajas de Optimización." (El código es limpio, legible y reduce drásticamente las líneas de código frente a bucles tradicionales).
  * **Slide 7 (CTA):** "Comenta **'APPLY'** y te comparto el notebook con ejemplos de funciones avanzadas aplicadas."

#### 📱 Video de TikTok/Reels (Motion Graphics)
* **Tema:** "Cómo transformar columnas enteras en Pandas (.apply)"
* **Duración:** 60 segundos (6 escenas de 10s).
* **Guión de Escenas:**
  * **Escena 1 (0-10s):** *Visual:* Una banda transportadora con celdas de datos desordenadas pasando bajo una prensa automatizada. *Voz en Off:* "¿Necesitas transformar una columna completa en Pandas aplicando una regla lógica muy compleja? Te presento a `.apply()`."
  * **Escena 2 (10-20s):** *Visual:* Se escribe una función clásica `def evaluar_riesgo(edad, score):` a la izquierda. *Voz en Off:* "Primero, escribes tu función personalizada en Python con todas las condiciones y variables que requiera tu negocio."
  * **Escena 3 (20-30s):** *Visual:* La prensa estampa el logo de la función en cada celda a medida que avanza. *Voz en Off:* "Luego, le pides a Pandas que la ejecute en la columna completa usando `.apply()`. Es como poner un sello automático en cada fila."
  * **Escena 4 (30-40s):** *Visual:* Los valores de la columna cambian de crudos a clasificaciones de colores al instante. *Voz en Off:* "En menos de un segundo, todos tus registros se actualizan según tus reglas complejas sin escribir bucles manuales."
  * **Escena 5 (40-50s):** *Visual:* Línea de código limpia: `df['Clasif'] = df['Ventas'].apply(mi_funcion)`. *Voz en Off:* "El código resultante es corto, rápido de ejecutar y sumamente profesional."
  * **Escena 6 (50-60s):** *Visual:* Cierre con logo del canal. *Voz en Off:* "Lleva tus habilidades de Pandas al siguiente nivel. ¡Síguenos para más tips!"

---

## 📈 Módulo 3: Visualización de Datos y Análisis Exploratorio (Clases 10 y 11)

### 📂 Clase 10: Visualización de Datos I con Matplotlib
> ⚠️ **Este material ya se va a generar (ver Clase 10 del Grupo 2)**  
> *Los fundamentos de Matplotlib, Figure vs Axes y gráficos básicos ya están cubiertos.*

---

### 📂 Clase 11: Visualización Estadística con Seaborn y EDA
> ⚠️ **Este material ya se va a generar (ver Clases 11 y 12 del Grupo 2)**  
> *Los gráficos avanzados (boxplots, heatmaps) y la metodología de taller guiado de EDA ya están cubiertos en el Grupo 2.*

---

## 🤖 Módulo 4: Estadística, Machine Learning y Proyecto Final (Clases 12 a 16)

### 📂 Clase 12: Estadística Descriptiva e Introducción a Machine Learning
* **Objetivo:** Introducir el paradigma predictivo y la diferencia entre aprendizaje supervisado y no supervisado.

#### 👔 Carrusel de LinkedIn (Imágenes)
* **Tema:** "Machine Learning desmitificado: El cambio de paradigma"
* **Estilo Visual:** *Gears vs. neural network vector graphics, logical splits, dark theme.*
* **Estructura de Slides:**
  * **Slide 1 (Portada):** "Cómo funciona el Machine Learning: Explicado de forma sencilla." (Visual: Una red de conexiones neuronales iluminándose).
  * **Slide 2:** "Programación Clásica." (Tú escribes las reglas y metes los datos; la computadora te da respuestas manuales).
  * **Slide 3:** "El Nuevo Paradigma." (Le das los datos e históricos de respuestas; la computadora descubre las reglas de forma automática).
  * **Slide 4:** "Aprendizaje Supervisado." (Predicción con una variable objetivo o etiqueta clara. Ej: Estimar precios de casas).
  * **Slide 5:** "Aprendizaje No Supervisado." (Agrupar registros sin etiquetas previas. Ej: Segmentar clientes de un banco).
  * **Slide 6:** "La Matriz X y el Vector y." (La estructura estándar para entrenar modelos predictivos).
  * **Slide 7 (CTA):** "Comenta **'INTROML'** y descarga la infografía conceptual de tipos de Machine Learning."

#### 📱 Video de TikTok/Reels (Motion Graphics)
* **Tema:** "El cambio de paradigma del Machine Learning"
* **Duración:** 60 segundos (6 escenas de 10s).
* **Guión de Escenas:**
  * **Escena 1 (0-10s):** *Visual:* Un programador escribiendo miles de reglas lógicas complejas a mano con cara de cansado. *Voz en Off:* "En la programación clásica, tú escribes todas las reglas de negocio a mano y el sistema solo calcula resultados."
  * **Escena 2 (10-20s):** *Visual:* Un servidor recibiendo datos y respuestas, y arrojando una llave brillante (el modelo predictivo). *Voz en Off:* "En Machine Learning invertimos la ecuación: le das datos e históricos de respuestas, y la computadora aprende las reglas sola."
  * **Escena 3 (20-30s):** *Visual:* Fotos de casas con precios y el modelo infiriendo el costo de una casa nueva. *Voz en Off:* "Si le enseñas casas con sus precios reales para que aprenda a predecir precios de casas nuevas, es **Aprendizaje Supervisado**."
  * **Escena 4 (30-40s):** *Visual:* Clientes agrupándose en burbujas de colores según afinidades. *Voz en Off:* "Si le das datos de clientes para que los agrupe por intereses comunes sin etiquetas previas, es **Aprendizaje No Supervisado**."
  * **Escena 5 (40-50s):** *Visual:* Estructuración de la matriz $X$ y el vector $y$. *Voz en Off:* "Para entrenar, dividimos los datos en la matriz $X$ de características y el vector $y$ de lo que queremos predecir."
  * **Escena 6 (50-60s):** *Visual:* Cierre con título de Clase 13. *Voz en Off:* "Entra al mundo de la Inteligencia Artificial. ¡Síguenos para la Clase 13!"

---

### 📂 Clase 13: Preparación de Datos y Regresión Lineal con Scikit-Learn
* **Objetivo:** Entrenar un modelo de regresión numérica con Scikit-Learn y aplicar la división train/test y escalado.

#### 👔 Carrusel de LinkedIn (Imágenes)
* **Tema:** "Tu primer modelo predictivo en Python con Scikit-Learn"
* **Estilo Visual:** *Database split bars, data scaling charts, line fitting scatter points.*
* **Estructura de Slides:**
  * **Slide 1 (Portada):** "Cómo entrenar un modelo de Regresión Lineal paso a paso." (Visual: Un plano cartesiano donde una recta atraviesa varios puntos).
  * **Slide 2:** "La Librería Scikit-Learn." (El estándar absoluto de la industria en Python para Machine Learning clásico).
  * **Slide 3:** "División Train/Test." (Separamos los datos en 80% para entrenar y 20% para evaluar de forma imparcial).
  * **Slide 4:** "Escalado (StandardScaler)." (Normalizar las variables para evitar que las escalas grandes dominen al modelo).
  * **Slide 5:** "El flujo Fit y Predict." (Entrenar el algoritmo con `.fit()` y estimar nuevos valores con `.predict()`).
  * **Slide 6:** "Caso Práctico." (Predecir los precios de oficinas en CDMX en base a sus metros cuadrados).
  * **Slide 7 (CTA):** "Comenta **'REGRESION'** y descarga el Jupyter Notebook con el código de entrenamiento."

#### 📱 Video de TikTok/Reels (Motion Graphics)
* **Tema:** "Cómo predecir el futuro en Python (Regresión Lineal)"
* **Duración:** 60 segundos (6 escenas de 10s).
* **Guión de Escenas:**
  * **Escena 1 (0-10s):** *Visual:* Una oficina con un precio flotando que sube y baja según sus características. *Voz en Off:* "¿Quieres predecir el precio de venta de una oficina usando Python y Machine Learning? Aquí está el proceso científico."
  * **Escena 2 (10-20s):** *Visual:* Una base de datos dividiéndose en dos bloques: Entrenamiento (80%) y Prueba (20%). *Voz en Off:* "Primero, dividimos los datos históricos: 80% para entrenar al modelo y 20% reservado para evaluar que aprenda de verdad."
  * **Escena 3 (20-30s):** *Visual:* Dos medidores igualándose en una escala de 0 a 1. *Voz en Off:* "Luego, escalamos los datos para que variables de rangos grandes no dominen injustamente a las pequeñas en el algoritmo."
  * **Escena 4 (30-40s):** *Visual:* Una ecuación lineal ajustándose a una nube de puntos. *Voz en Off:* "Instanciamos la Regresión Lineal. El modelo traza la línea perfecta que minimiza la distancia al valor real."
  * **Escena 5 (40-50s):** *Visual:* Ejecución rápida de `model.fit()` y `model.predict()` en Jupyter. *Voz en Off:* "Corremos `.fit()` para entrenarlo y `.predict()` para calcular el precio estimado de una oficina nueva."
  * **Escena 6 (50-60s):** *Visual:* Cierre con título de Clase 14. *Voz en Off:* "Crea tus propios modelos predictivos. ¡Síguenos para la Clase 14 de Evaluación!"

---

### 📂 Clase 14: Evaluación de Modelos y Clasificación
* **Objetivo:** Evaluar métricas de clasificación usando la matriz de confusión y comprender Accuracy vs. Precision vs. Recall.

#### 👔 Carrusel de LinkedIn (Imágenes)
* **Tema:** "Métricas de Clasificación: Accuracy vs. Precision vs. Recall"
* **Estilo Visual:** *Confusion matrix template, gauges of accuracy vs recall, filter checkpoints.*
* **Estructura de Slides:**
  * **Slide 1 (Portada):** "Por qué la Exactitud (Accuracy) te puede mentir al evaluar tu IA." (Visual: Un medidor al 99% con una luz roja de advertencia).
  * **Slide 2:** "Modelos de Clasificación." (Predecir eventos binarios. Ej: ¿Este correo es spam?, ¿esta transacción es fraude?).
  * **Slide 3:** "La Matriz de Confusión." (Una cuadrícula que organiza los aciertos y fallos: verdaderos/falsos positivos y negativos).
  * **Slide 4:** "Precisión vs. Recall." (Precisión: de lo que predije como positivo, cuánto era real. Recall: de lo real positivo, cuánto logré detectar).
  * **Slide 5:** "El peligro del desbalanceo." (Si solo 1 de cada 100 correos es spam, un modelo inútil que prediga 'No Spam' tendrá 99% de Accuracy).
  * **Slide 6:** "El veredicto." (Saber elegir la métrica según el costo de los errores para el negocio).
  * **Slide 7 (CTA):** "Comenta **'METRICAS'** y te comparto el acordeón con el resumen visual de evaluación de modelos."

#### 📱 Video de TikTok/Reels (Motion Graphics)
* **Tema:** "¿Por qué el 99% de exactitud en IA puede ser un fracaso?"
* **Duración:** 60 segundos (6 escenas de 10s).
* **Guión de Escenas:**
  * **Escena 1 (0-10s):** *Visual:* Un marcador digital brillando al 99% pero con una alarma parpadeando al lado. *Voz en Off:* "¿Sabías que un modelo de inteligencia artificial con 99% de exactitud puede ser un absoluto fracaso?"
  * **Escena 2 (10-20s):** *Visual:* Cien transacciones pasando y solo una pintándose de rojo (fraude). *Voz en Off:* "Imagina que detectas fraudes bancarios. Si solo 1 de cada 100 operaciones es fraudulenta, y tu modelo siempre dice 'No es fraude'..."
  * **Escena 3 (20-30s):** *Visual:* Una rejilla de Matriz de Confusión mostrando los fraudes escapados. *Voz en Off:* "Tu modelo tiene 99% de exactitud, ¡pero dejó pasar todos los robos! El banco perdería miles de dólares."
  * **Escena 4 (30-40s):** *Visual:* Dos diales interactivos: Precisión y Recall. *Voz en Off:* "Por eso, los científicos de datos usan la **matriz de confusión** para medir la Precisión y el Recall en lugar de solo la Exactitud."
  * **Escena 5 (40-50s):** *Visual:* Un escáner de aeropuerto detectando un artículo prohibido. *Voz en Off:* "El Recall te asegura encontrar todos los casos críticos, incluso si genera falsas alarmas de vez en cuando."
  * **Escena 6 (50-60s):** *Visual:* Cierre con título de Clase 15. *Voz en Off:* "Aprende a evaluar modelos reales. ¡Síguenos para la Clase 15 de Proyecto Final!"

---

### 📂 Clase 15: Proyecto Final Aplicado
* **Objetivo:** Estructurar un proyecto de extremo a extremo e integrar ingesta, limpieza, modelado y evaluación.

#### 👔 Carrusel de LinkedIn (Imágenes)
* **Tema:** "Cómo estructurar un proyecto de Ciencia de Datos para tu Portafolio"
* **Estilo Visual:** *Integrated pipeline schematic, data stages connected with arrows, clean outputs.*
* **Estructura de Slides:**
  * **Slide 1 (Portada):** "Cómo estructurar un proyecto final de Ciencia de Datos de extremo a extremo." (Visual: Carpeta de proyecto con logos de Pandas y Scikit-Learn).
  * **Slide 2:** "El Reto Comercial." (Definir el problema a resolver. Ej: Estimar demanda de inventario para una tienda).
  * **Slide 3:** "Preparación de Datos." (Carga, diagnóstico de nulos y duplicados, e ingeniería de variables con Pandas).
  * **Slide 4:** "Modelado Predictivo." (Entrenamiento de algoritmos de regresión y clasificación usando Scikit-Learn).
  * **Slide 5:** "Evaluación de Resultados." (Comparar predicciones contra datos de test y calcular métricas de error).
  * **Slide 6:** "El Entregable en GitHub." (Código limpio, estructurado y documentado en un Jupyter Notebook reproducible).
  * **Slide 7 (CTA):** "Comenta **'PROYECTODS'** y te comparto el repositorio base del proyecto de Ciencia de Datos."

#### 📱 Video de TikTok/Reels (Motion Graphics)
* **Tema:** "De datos crudos a predicciones (El pipeline de Ciencia de Datos)"
* **Duración:** 60 segundos (6 escenas de 10s).
* **Guión de Escenas:**
  * **Escena 1 (0-10s):** *Visual:* Datos binarios sucios entrando en una fábrica digital y saliendo como gráficos estructurados. *Voz en Off:* "¿Quieres saber cómo se construye un proyecto de Ciencia de Datos completo para tu portafolio? Aquí tienes el pipeline en 4 pasos."
  * **Escena 2 (10-20s):** *Visual:* Pandas limpiando valores nulos. *Voz en Off:* "Paso 1: Ingesta y Limpieza. Descargamos datos históricos reales y eliminamos nulos y duplicados usando Pandas."
  * **Escena 3 (20-30s):** *Visual:* Scikit-Learn entrenando una línea de regresión. *Voz en Off:* "Paso 2: Entrenamiento. Dividimos los datos, escalamos las variables y entrenamos nuestro modelo con Scikit-Learn."
  * **Escena 4 (30-40s):** *Visual:* Gráfico de comparación de errores. *Voz en Off:* "Paso 3: Evaluación. Medimos la diferencia entre las predicciones y los valores reales para garantizar la confiabilidad."
  * **Escena 5 (40-50s):** *Visual:* Archivos ordenados con un README en GitHub. *Voz en Off:* "Paso 4: Entrega. Documentamos y subimos el pipeline completo a un repositorio de GitHub público."
  * **Escena 6 (50-60s):** *Visual:* Cierre con título de Clase 16. *Voz en Off:* "Haz proyectos que demuestren tu nivel. ¡Síguenos para la última sesión de Storytelling!"

---

### 📂 Clase 16: Presentación de Proyectos, Conclusiones y Ruta Futura
* **Objetivo:** Comunicar resultados a tomadores de decisiones mediante Data Storytelling e identificar rutas de especialización.

#### 👔 Carrusel de LinkedIn (Imágenes)
* **Tema:** "Data Storytelling: Cómo vender tus proyectos a directivos"
* **Estilo Visual:** *Executive meeting room graphics, financial bar charts with single red highlights, clean layout.*
* **Estructura de Slides:**
  * **Slide 1 (Portada):** "Por qué programar no sirve de nada si no sabes comunicar tus hallazgos." (Visual: Un gráfico financiero proyectado ante una mesa directiva).
  * **Slide 2:** "La trampa del tecnicismo." (A los gerentes no les interesan las fórmulas ni las librerías; les interesa el ahorro de dinero o aumento de ventas).
  * **Slide 3:** "La Estructura de la Historia." (Presenta el problema  →  El hallazgo crítico del modelo  →  La decisión de negocio sugerida).
  * **Slide 4:** "Gráficos Ejecutivos." (Desecha gráficos saturados de datos. Resalta únicamente el punto clave con un color llamativo).
  * **Slide 5:** "La Ruta de Especialización." (El fin del camino básico. Siguientes pasos: Big Data, SQL avanzado y modelos en producción).
  * **Slide 6:** "El veredicto final." (Los mejores científicos de datos no solo escriben código; cuentan historias de negocio a través de él).
  * **Slide 7 (CTA):** "Comenta **'STORYTELLING'** y descarga la guía de presentación ejecutiva de proyectos de datos."

#### 📱 Video de TikTok/Reels (Motion Graphics)
* **Tema:** "El error número 1 al presentar proyectos de Datos"
* **Duración:** 60 segundos (6 escenas de 10s).
* **Guión de Escenas:**
  * **Escena 1 (0-10s):** *Visual:* Una diapositiva llena de fórmulas matemáticas complejas. Un gerente quedándose dormido. *Voz en Off:* "¿Sabías que el error más común de los científicos de datos es aburrir a sus jefes con tecnicismos matemáticos?"
  * **Escena 2 (10-20s):** *Visual:* Las fórmulas se tachan con una cruz roja y aparece un letrero de "Traducir a Dinero". *Voz en Off:* "A la junta directiva no le importa tu código ni el modelo exacto que usaste; les interesa saber el impacto de negocio."
  * **Escena 3 (20-30s):** *Visual:* Gráfico de barras indicando: "Predicción de demanda ahorra 15% de inventario". *Voz en Off:* "En lugar de decir: 'Entrenamos un modelo con bajo error cuadrático', di: 'Optimizamos el stock y ahorraremos un 15% de inventario'."
  * **Escena 4 (30-40s):** *Visual:* Recomendación accionable en pantalla. *Voz en Off:* "Acompaña tu gráfico con una recomendación de negocio: 'Sugerimos transferir excedentes a la Sucursal Centro'."
  * **Escena 5 (40-50s):** *Visual:* Un científico de datos sonriente estrechando la mano de su jefe. *Voz en Off:* "Saber comunicar tus datos es lo que te conseguirá ascensos y salarios altos en empresas remotas."
  * **Escena 6 (50-60s):** *Visual:* Birrete de graduación finalizando el curso de Ciencia de Datos. *Voz en Off:* "¡Felicidades por completar el curso de Ciencia de Datos! Síguenos para continuar aprendiendo."
