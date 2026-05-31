# Optimización Logística y Predicción de Demanda en Supermercados
**Prueba el simulador interactivo para asignación de logística aquí:** [[URL Streamlit Cloud](https://tendencias-consumo-3nzubedtwzxvda4dqzm49n.streamlit.app/)]

Proyecto de Ciencia de Datos orientado a analizar la evolución de las ventas presenciales y online en supermercados argentinos, con el objetivo de identificar tendencias que apoyen la planificación logística y la asignación de recursos.

## Descripción del proyecto

La transformación digital también ha cambiado la forma en que las personas realizan sus compras de supermercado. Mientras una parte de los clientes continúa comprando de manera presencial, cada vez más consumidores utilizan canales online para recibir sus pedidos en sus hogares.

Este cambio genera un desafío para las áreas de Logística y Recursos Humanos: planificar correctamente la dotación de personal necesaria para atender ambos canales de venta.

El objetivo de este proyecto es analizar la evolución de las ventas presenciales y online en supermercados argentinos y construir un modelo predictivo que permita estimar la tendencia futura de cada canal. Esta información puede servir como apoyo para decisiones relacionadas con la asignación de personal, la planificación operativa y la distribución de recursos.

### Fuente de datos
Se utilizó información pública proveniente del conjunto de datos "Ventas totales en supermercados a valores corrientes y constantes", publicado por la Subsecretaría de Programación Macroeconómica a través del portal Datos Argentina. 

[Acceder al dataset oficial aquí](https://www.datos.gob.ar/dataset/sspm-ventas-supermercados/archivo/sspm_455.1)

El análisis se centra en la evolución de las variables:
- `salon_ventas`
- `canales_on_line`

## Metodología

El proyecto se desarrolló siguiendo un flujo de trabajo típico de Ciencia de Datos:

1. Obtención y exploración de los datos.
2. Limpieza y preparación de la información.
3. Tratamiento de valores faltantes y validación de variables.
4. Análisis exploratorio de tendencias.
5. Construcción de un modelo de Regresión Lineal para identificar el crecimiento del canal online a lo largo del tiempo [Ver Notebook en Google Colab](https://colab.research.google.com/github/GMZepeda/tendencias-consumo/blob/main/analisis_ventas.ipynb).
6. Interpretación de resultados desde una perspectiva de negocio.

**Decisión técnica frente a la inflación:**
Para resolver el problema del impacto inflacionario presente en los datos históricos, se tomó la decisión técnica de no predecir valores monetarios nominales. En su lugar, el modelo calcula y proyecta el porcentaje de ventas online sobre el volumen total. Trabajar con proporciones permite cancelar matemáticamente el sesgo de la inflación y estabilizar la Regresión Lineal, reflejando el cambio real en los hábitos del consumidor.

## Principales hallazgos

El análisis muestra una tendencia sostenida de crecimiento en la participación de las ventas realizadas a través de canales online.

La pendiente positiva obtenida en el modelo indica que el canal digital continúa ganando relevancia mes a mes, mientras que las ventas presenciales mantienen una participación predominante pero con un crecimiento menos acelerado.

Estos resultados sugieren que las empresas del sector deberían considerar una planificación progresiva de recursos orientada a fortalecer las operaciones vinculadas al comercio electrónico, incluyendo preparación de pedidos, logística de distribución y atención de ventas digitales.

## Herramientas utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Jupyter Notebook

## Arquitectura de la Solución

[Ver diagrama de flujo de datos](canales-venta.png)

La arquitectura sigue un enfoque basado en servicios separados, donde cada componente cumple una función específica dentro del flujo de procesamiento y análisis de datos.

### Frontend (Interfaz de Usuario)

La interfaz fue desarrollada con **Streamlit** y desplegada en la nube para permitir que el usuario cargue archivos de datos y visualice los resultados de forma sencilla e interactiva.

### Backend y API

El procesamiento se implementó mediante **FastAPI**, alojado en **Hugging Face Spaces**. Este componente recibe los datos, valida su estructura, realiza tareas de limpieza y tratamiento de valores faltantes utilizando **Pandas** y **NumPy**, y prepara la información para el análisis.

### Motor Predictivo

La capa analítica utiliza **Scikit-Learn** para entrenar un modelo de **Regresión Lineal**, permitiendo identificar y proyectar la evolución de los distintos canales de venta a lo largo del tiempo.

### Control de Versiones

El desarrollo y mantenimiento del proyecto se gestionaron mediante **Git** y **GitHub**, facilitando el seguimiento de cambios, la documentación y la colaboración.


## Limitaciones

Los datos utilizados se encuentran agregados a nivel nacional y no incluyen información geográfica. Por este motivo, los resultados representan una tendencia promedio para Argentina y no capturan posibles diferencias entre regiones o ciudades.

Asimismo, el modelo empleado busca describir e interpretar tendencias generales y no reemplaza herramientas de pronóstico de demanda más complejas utilizadas en entornos productivos.
