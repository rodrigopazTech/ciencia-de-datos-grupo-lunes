# Guía de Instalación de Anaconda y Jupyter Lab

Esta guía contiene las instrucciones paso a paso para descargar, instalar y ejecutar **Anaconda** y **Jupyter Lab** en los tres sistemas operativos principales: **Windows**, **macOS (MacBook)** y **Linux**.

---

## 1. Descarga del Instalador
Para todos los sistemas operativos, el primer paso es descargar el instalador oficial:
1. Ve al sitio oficial de Anaconda: [https://www.anaconda.com/download](https://www.anaconda.com/download)
2. El sitio detectará automáticamente tu sistema operativo. Haz clic en el botón **Download**.
   * *Nota:* Si estás en macOS o Linux y necesitas una arquitectura específica, puedes desplazarte al final de la página para ver todas las opciones disponibles.

---

## 2. Instrucciones de Instalación por Sistema Operativo

### 💻 Opción A: Windows

1. **Ejecutar el instalador:** Abre el archivo descargado (ej. `Anaconda3-xxxx.xx-Windows-x86_64.exe`).
2. **Asistente de configuración:**
   * Haz clic en **Next** (Siguiente).
   * Lee y acepta la licencia haciendo clic en **I Agree**.
   * Selecciona la opción **Just Me** (Solo para mí) y haz clic en **Next**.
   * Elige la ruta de instalación por defecto y haz clic en **Next**.
3. **Opciones avanzadas de instalación:**
   * **RECOMENDADO:** Asegúrate de que la casilla *"Register Anaconda3 as my default Python"* esté activada.
   * **IMPORTANTE:** *No* recomendamos activar la casilla de agregar Anaconda al PATH (a menos que seas un usuario avanzado), ya que puede generar conflictos con otras versiones de Python.
4. **Completar:** Haz clic en **Install**. La instalación puede tardar entre 5 y 10 minutos. Una vez completada, haz clic en **Next** y luego en **Finish**.

---

### 🍎 Opción B: macOS (MacBook)

Existen dos tipos de procesadores en Mac. Asegúrate de verificar cuál tienes (clic en el menú de la manzana  en la esquina superior izquierda $\rightarrow$ *Acerca de esta Mac* / *About This Mac*):
* **Apple Silicon (M1, M2, M3, etc.):** Descarga el instalador para *"M1/M2/M3"* (Apple Silicon).
* **Intel:** Descarga el instalador para *"Intel"*.

#### Instalador Gráfico (Recomendado para principiantes):
1. **Ejecutar el instalador:** Abre el archivo descargado (`.pkg`).
2. **Asistente:**
   * Haz clic en **Continuar** en las pantallas de bienvenida y términos de licencia.
   * Haz clic en **Aceptar** los términos de la licencia.
   * Selecciona **Instalar solo para mí** y haz clic en **Continuar**.
   * Haz clic en **Instalar** e ingresa la contraseña de administrador de tu Mac.
3. **Completar:** Una vez que el instalador finalice, haz clic en **Cerrar**.

---

### 🐧 Opción C: Linux (Ubuntu, Debian, Fedora, etc.)

La instalación en Linux se realiza mediante la terminal usando el script de shell descargado (`.sh`).

1. **Abrir la terminal:** Ve a tu carpeta de descargas (normalmente `~/Downloads`).
2. **Ejecutar el script:** Reemplaza el nombre del archivo en el comando siguiente por el que descargaste:
   ```bash
   bash Anaconda3-2024.02-Linux-x86_64.sh
   ```
3. **Seguir instrucciones en la terminal:**
   * Presiona **Enter** para leer el acuerdo de licencia (puedes presionar la barra espaciadora para avanzar rápido).
   * Escribe `yes` para aceptar los términos y presiona **Enter**.
   * Confirma la ubicación de instalación por defecto (normalmente `~/anaconda3`) presionando **Enter**.
4. **Inicializar Conda:**
   * Al final del proceso, el instalador te preguntará si deseas inicializar Anaconda ejecutando `conda init`. Escribe `yes` y presiona **Enter**.
5. **Aplicar cambios:** Cierra la terminal y vuelve a abrirla, o ejecuta el siguiente comando para cargar la nueva configuración:
   ```bash
   source ~/.bashrc
   ```

---

## 3. Cómo iniciar Jupyter Lab (Todos los sistemas)

Una vez completada la instalación, puedes abrir el entorno de Jupyter Lab de dos maneras:

### Método 1: A través de Anaconda Navigator (Gráfico)
1. Busca y abre la aplicación **Anaconda Navigator** en tu sistema operativo:
   * **Windows:** Búscalo en el menú de inicio.
   * **macOS:** Abre el Launchpad o ve a *Aplicaciones* y abre Anaconda Navigator.
   * **Linux:** Escribe `anaconda-navigator` en tu terminal.
2. Una vez que cargue la interfaz, verás varios iconos. Busca la tarjeta de **Jupyter Lab** (no confundir con Jupyter Notebook).
3. Haz clic en el botón **Launch**. Esto abrirá una pestaña en tu navegador web con la interfaz de Jupyter Lab.

### Método 2: A través de la terminal (Rápido y Recomendado)
1. Abre tu terminal o consola:
   * **Windows:** Busca y abre **Anaconda Prompt** desde el menú de inicio (no uses la consola estándar de CMD).
   * **macOS y Linux:** Abre tu terminal de sistema estándar.
2. Escribe el siguiente comando y presiona **Enter**:
   ```bash
   jupyter lab
   ```
3. Tu navegador web se abrirá automáticamente con el entorno gráfico de Jupyter Lab.
   * *Nota:* Mantén abierta la terminal mientras trabajas, ya que esta sirve como el servidor que ejecuta tus códigos en segundo plano.

---

## 4. Crear tu primer Notebook (.ipynb)

Una vez que visualices Jupyter Lab en tu navegador:
1. En la pestaña del "Launcher" (Lanzador), haz clic en el icono de **Python 3 (ipykernel)** dentro de la sección **Notebook**.
2. Esto creará un nuevo archivo en blanco llamado `Untitled.ipynb`.
3. Haz clic derecho sobre el archivo en la barra lateral izquierda para renombrarlo a algo descriptivo (ej. `mi_primer_codigo.ipynb`).
4. ¡Listo! Ya puedes escribir tu código en la celda y ejecutarlo usando el atajo de teclado **Shift + Enter**.
