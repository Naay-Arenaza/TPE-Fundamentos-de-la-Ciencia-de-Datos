# TPE-Fundamentos-de-la-Ciencia-de-Datos
Este repositorio contiene el Trabajo Práctico Especial (TPE) para la materia **Fundamentos de la Ciencia de Datos**. 
El proyecto consiste en un análisis exploratorio y validación estadística de hipótesis sobre el dataset **"Online Shoppers Purchasing Intention"**, con el objetivo de identificar qué factores influyen en la decisión de compra.

## Integrantes (Grupo 8)
* **Arenaza, Nayla Solange**
* **Astigueta, Ignacio**
* **Lertora, Santiago Tomas**

## Estructura del Proyecto
- **TPE.ipynb** → Notebook principal con análisis, visualizaciones y pruebas estadísticas.  
- **requirements.txt** → Librerías necesarias para reproducir el entorno.  
- **README.md** → Documentación del proyecto.  
- *(Opcional)* `online_shoppers_intention.csv` → Dataset original.  
- *(Opcional)* `online_shoppers_intention_mod.csv` → Dataset procesado.

## Instrucciones de Instalación y Ejecución

El proyecto puede ejecutarse en la nube (Google Colab) o en un entorno local.

### Opción A: Google Colab
1. Subir el archivo **TPE.ipynb** a Google Drive.
2. Abrir el archivo con Google Colab.
3. Ejecutar las celdas secuencialmente (Entorno de ejecución > Ejecutar todas).
   *Nota:* No es necesaria ninguna instalación previa, ya que el notebook utiliza librerías estándar preinstaladas en Colab.

### Opción B: Ejecución Local
Para ejecutar este proyecto en tu computadora:
**1. Clonar el repositorio o descargar los archivos**

`git clone https://github.com/Naay-Arenaza/TPE-Fundamentos-de-la-Ciencia-de-Datos.git`

**2. Crear un entorno virtual**
Abre tu terminal y ejecuta:
**En Windows:**
`python -m venv env`
`env\Scripts\activate`
**En Mac/Linux:**
`python3 -m venv env`
`source env/bin/activate`

**3. Instalar jupyterlab, Reconstruir el ambiente de PIP y Ejecutar el proyecto**
`pip install jupyterlab`
`pip install -r requirements.txt`
`jupyter-lab`