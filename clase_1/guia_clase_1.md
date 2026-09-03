# Guía de la Clase 1: Historia de la Ciencia de Datos y Panorama Profesional

**Duración sugerida:** 60 minutos  
**Modalidad:** Teórico-práctica (Con debates interactivos y análisis de casos de estudio).  
**Objetivo:** Que el alumnado comprenda el origen y valor de la Ciencia de Datos, diferencie los roles clave del ecosistema (Data Scientist vs. Data Engineer vs. BI Analyst), entienda el ciclo de vida de un proyecto de datos usando la metodología CRISP-DM y aprenda a identificar problemas que aportan valor real de negocio.

---

### 🎨 Apoyo Visual para el Aprendizaje
* **Metáfora Conceptual:** El ciclo de vida de los datos (CRISP-DM) es como abrir y operar un restaurante. 
  1. **Business Understanding:** Defines el menú basándote en lo que quiere comer la gente del barrio.
  2. **Data Understanding:** Consigues e inspeccionas los ingredientes frescos del mercado.
  3. **Data Preparation:** Lavas, cortas y preparas los ingredientes antes de cocinar.
  4. **Modeling:** Sigues la receta técnica paso a paso para cocinar el platillo.
  5. **Evaluation:** Pruebas el platillo antes de servirlo para asegurar la calidad.
  6. **Deployment:** Sirves la comida en la mesa al cliente final. Si al cliente le gusta y regresa, el negocio prospera.
* **Prompt para Generar Imagen con IA (Midjourney/DALL-E 3):**
  > *A sleek isometric flat vector illustration representing the data science lifecycle. A circular conveyor belt with 6 glowing stages representing: a lightbulb (business understanding), database drums (data acquisition), a cleaning brush and filter (data preparation), a neural network gear (modeling), a checklist checkmark (evaluation), and a rocket launching (deployment). Clean corporate color palette (teal, navy blue, and orange), professional tech design.*

---

## 1. Introducción al Ecosistema y Evolución Histórica (15 min)

### Explicación para instructor
Presenta la Ciencia de Datos como la intersección de la Computación, la Matemática/Estadística y el Conocimiento del Negocio (el clásico Diagrama de Venn de Drew Conway). Explica brevemente cómo evolucionó de la estadística clásica al análisis masivo de datos gracias al abaratamiento del cómputo y el almacenamiento en la nube.
* **Hito clave:** El término popularizado por DJ Patil y Jeff Hammerbacher en 2008 al definir sus equipos en LinkedIn y Facebook.
* **Caso real para inspirar:** El algoritmo de recomendación de Netflix que ahorra mil millones de dólares anuales en retención de usuarios.

#### Texto para una celda Markdown del notebook / Diapositiva
```markdown
# Clase 1: Historia de la Ciencia de Datos y Panorama Profesional
La Ciencia de Datos no consiste únicamente en escribir código o entrenar modelos de Inteligencia Artificial; su fin último es resolver problemas reales de negocio y tomar mejores decisiones utilizando la información disponible.
```

---

## 2. El Ciclo de Vida de los Datos: Metodología CRISP-DM (20 min)

### Explicación para instructor
Explica el ciclo estándar de la industria: **CRISP-DM** (*Cross-Industry Standard Process for Data Mining*). Destaca que **no es un proceso lineal**, sino cíclico e iterativo.
1. **Comprensión del Negocio (Business Understanding):** ¿Qué problema queremos resolver?
2. **Comprensión de los Datos (Data Understanding):** ¿Qué datos tenemos, dónde están y qué tan limpios están?
3. **Preparación de los Datos (Data Preparation):** Limpieza, selección de variables y transformaciones.
4. **Modelado (Modeling):** Selección del algoritmo y entrenamiento.
5. **Evaluación (Evaluation):** Comprobar que el modelo cumpla con las métricas de negocio y de precisión técnica.
6. **Despliegue (Deployment):** Integrar el modelo en un sistema en producción para el uso diario del negocio.

#### Texto para una celda Markdown del notebook / Diapositiva
```markdown
## El Ciclo CRISP-DM
Un proyecto de datos exitoso siempre empieza con una pregunta de negocio clara y termina con una solución implementada que genera valor real.
```

---

## 3. Roles del Ecosistema de Datos: ¿Quién hace qué? (15 min)

### Explicación para instructor
Desmitifica la idea de que un Científico de Datos lo hace todo. Explica las diferencias de roles usando analogías de construcción:
* **Data Engineer (El Plomero/Arquitecto):** Construye la infraestructura y las tuberías (ETL) para transportar el agua (los datos) de forma segura.
* **Data Scientist (El Químico/Cocinero):** Analiza el agua, experimenta y crea fórmulas avanzadas (modelos predictivos/Machine Learning).
* **BI / Data Analyst (El Sommelier/Comunicador):** Prueba el agua, evalúa las tendencias y crea reportes o tableros (dashboards) visuales que el negocio entiende fácilmente.

#### Tabla comparativa de roles

| Rol | Enfoque Principal | Herramientas Comunes | Pregunta Clave que Resuelve |
| :--- | :--- | :--- | :--- |
| **Data Engineer** | Infraestructura, ETL, flujos de datos y bases de datos. | SQL, Spark, Airflow, AWS/GCP, Docker. | *¿Cómo garantizamos que los datos lleguen limpios y a tiempo a los servidores?* |
| **Data Scientist** | Predicción, algoritmos complejos, Machine Learning. | Python (Scikit-Learn), R, Estadística, Jupyter. | *¿Cómo predecimos el comportamiento futuro del usuario o las ventas?* |
| **BI / Data Analyst** | Reporting, descriptivo, dashboards y métricas de negocio. | SQL, Power BI, Tableau, Excel. | *¿Qué pasó en el último trimestre y por qué cambiaron nuestras ventas?* |

---

## 4. Taller de Cierre: El Caso "Pizza Delivery" (10 min)

### Explicación para instructor
Guía a los alumnos en una dinámica rápida de lluvia de ideas para resolver un problema de negocio aplicando CRISP-DM y mapeando los roles.

#### Planteamiento del Problema
Una cadena de pizzerías local lanzó una aplicación de entregas a domicilio, pero está perdiendo clientes porque el **25% de los pedidos llega tarde (más de 30 minutos)**. El gerente quiere usar Ciencia de Datos para resolver esto.

#### Ejercicio Práctico
* **Paso 1 (Negocio):** ¿Cuál es el objetivo principal del proyecto?
* **Paso 2 (Datos):** ¿Qué tipo de información necesitaríamos recopilar? (Ej. hora del pedido, tráfico, clima, tiempo de preparación, repartidor asignado).
* **Paso 3 (Roles):** ¿Qué haría cada especialista para solucionar el problema?

#### Resolución Sugerida para el Instructor (Feedback rápido)
* **Objetivo de Negocio:** Predecir si un pedido llegará tarde antes de salir de la cocina para alertar al cliente o reasignar rutas.
* **Datos requeridos:** Historial de entregas, coordenadas GPS, tráfico en tiempo real, día de la semana y carga de pedidos en cocina.
* **División de Roles:**
  * **Data Engineer:** Crea la base de datos y la tubería para jalar el tráfico de Google Maps y conectarlo con los pedidos.
  * **Data Scientist:** Desarrolla un modelo que estima el tiempo de entrega y asigna alertas rojas a pedidos con alta probabilidad de retrasarse.
  * **BI Analyst:** Diseña un tablero para el gerente general que muestra los cuellos de botella por sucursal y el porcentaje de entregas a tiempo diario.
