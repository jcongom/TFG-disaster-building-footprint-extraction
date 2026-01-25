# 🌋 Integración de la IA en la evaluación de daños por desastres naturales mediante extracción de huellas de edificios

## 📋 Descripción

En las últimas tres décadas, el aumento de eventos meteorológicos extremos ha provocado más de 765.000 muertes y pérdidas por 4.200 millones de dólares. El análisis de estos riesgos subraya la urgencia de herramientas para una evaluación rápida de daños estructurales, optimizando la toma de decisiones en fases de respuesta y recuperación.

Este Trabajo de Fin de Grado desarrolla un sistema automatizado de evaluación de daños mediante IA y análisis geoespacial, aplicado a la erupción de La Palma de 2021. La metodología integra el estudio del estado del arte, datos satelitales abiertos y algoritmos de segmentación para la extracción y regularización de huellas de edificios, validados mediante sistemas de información geográfica.

## 🗂️ Estructura del repositorio

```
/
├── data/                 # Datos en crudo, procesados y modelos de GeoAI
│   ├── geoai/
│   ├── processed/
│   ├── raw/
│   ├── test/
│   └── train/
├── docs/                 # Dashboard de visualización web
│   ├── assets/
│   ├── script/
│   └── index.html
├── documentation/        # Memoria y presentación del TFG
│   ├── presentation/
│   └── thesis/
├── notebooks/            # Cuadernos de Jupyter con el flujo de trabajo
│   ├── 00_preprocesamiento.ipynb
│   ├── 01_extraccion_datos.ipynb
│   ├── 02_creacion_modelo.ipynb
│   └── 03_extraccion_huellas.ipynb
├── qgis/                 # Proyecto de QGIS para validación
│   ├── 01 - validation.gpkg
│   └── 01 - validation.qgz
├── .gitignore
├── environment.yml       # Archivo de configuración del entorno Conda
├── LICENSE
└── README.md
```

## ⚙️ Instalación y despliegue


### 1. Clonar el repositorio
```bash
git clone https://github.com/jcongom/TFG-disaster-building-footprint-extraction.git
cd TFG-disaster-building-footprint-extraction
```

### 2. Descargar los datos
Los modelos entrenados y los datos geoespaciales utilizados en la ejecución de los cuadernos son demasiado grandes para ser alojados directamente en el repositorio. Para recuperar la versión original del poryecto, han sido comprimidos y divididos en partes.

*   Acude a la sección de **[Releases](https://github.com/jcongom/TFG-disaster-building-footprint-extraction/releases)** en este repositorio.
*   Descarga todos los archivos divididos (`jcongom_binarios.7z.001`, `jcongom_binarios.7z.002`, etc.).
*   Mueve todos los archivos descargados a la raíz de este repositorio.
*   Para descomprimir, solo es necesario extraer el primer archivo (`.001`). El resto se unirá automáticamente. Puedes usar [7-Zip](https://www.7-zip.org/) o una herramienta similar.
    ```bash
    7z x jcongom_binarios.7z.001
    ```
    Esto creará las carpetas con todos los contenidos necesarios.

### 3. Configurar el entorno
Asegúrate de tener instalada una distribución de Conda (Miniconda o Anaconda).

*   **Crear el entorno:**
    ```bash
    conda env create -f environment.yml
    ```
*   **Activar el entorno:**
    ```bash
    conda activate TFG
    ```

> [!WARNING]
> 1.  Este proyecto está configurado originalmente para ser ejecutado con una GPU **AMD** utilizando **ROCm** en un sistema operativo Linux.
> 2.  El archivo `environment.yml` se basa en dependencias específicas de ROCm para `PyTorch`.
> 3.  Si utilizas otro sistema operativo, una GPU **NVIDIA (CUDA)** o solo CPU, puedes ignorar las líneas correspondientes a `pytorch`, `torchvision`, etc. GeoAI ya incluye las dependencias necesarias para esos casos. Consulta la [web oficial de GeoAI](https://opengeoai.org/#installation) para más detalles de instalación.

## 📄 Licencia

[![CC BY-NC-ND 4.0][cc-by-nc-nd-shield]][cc-by-nc-nd]

Este proyecto se distribuye bajo la licencia [Creative Commons Attribution-NonCommercial-NoDerivs 4.0 International License][cc-by-nc-nd].

[![CC BY-NC-ND 4.0][cc-by-nc-nd-image]][cc-by-nc-nd]

[cc-by-nc-nd]: http://creativecommons.org/licenses/by-nc-nd/4.0/
[cc-by-nc-nd-image]: https://licensebuttons.net/l/by-nc-nd/4.0/88x31.png
[cc-by-nc-nd-shield]: https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg

## ✍️ Autor

**Javier Concha Gómez**

Grado de Ingeniería de Tecnologías y Servicios de Telecomunicación

Universitat Oberta de Catalunya