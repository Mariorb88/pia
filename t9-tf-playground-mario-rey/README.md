# Tarea 9: TensorFlow Playground

## 1. Repositorio
Crea un nuevo repositorio de trabajo en [avidaldo-ia24](https://github.com/organizations/avidaldo-ia24/repositories/new):

- `Owner` debe ser `avidaldo-ia24`.
- El nombre debe ser `t9-tf-playground-nombre1-apellido1`, sustituyendo `nombre1-apellido1` por tu identificador.
- Ese nuevo repositorio debe ser **privado**.

## 2. Tarea

> [!TIP]  
> En [este vídeo de clase](https://youtu.be/UvJrYDttV44) se dan explicaciones sobre esta tarea.

Crea un documento markdown llamado **`tarea9.md`** con tus soluciones a los datasets propuestos en [el playground de tensorflow](https://playground.tensorflow.org/):

- Regresión:
    - Plane
    - Multi Gaussian

- Clasificación:
    - Gaussian
    - Exclusive or
    - Circle
    - Spiral

Para cada uno de estos casos, se debe trabajar bajo el enfoque de soluciones mínimas, es decir, identificar y justificar la configuración que utilice la menor complejidad (menos capas y neuronas) sin sacrificar la precisión y generalización del modelo.

Para cada dataset, describe:

- **Problema**: Breve resumen de las características y retos del dataset. Puedes también ver los efectos de modificar ratio train/test, el ruido o el tamaño de lote.

- **Hiperparámetros**: **arquitectura del modelo**: Número de capas, cantidad de neuronas por capa y la razón detrás de estas elecciones y configuración elegida (tasa de aprendizaje, épocas, regularización, etc.). **Añade la URL de la configuración utilizada**. También puedes añadir capturas.

- **Feature Engineering**: Proponer al menos una solución que utilice únicamente las características básicas (X1 y X2). Adicionalmente, se pueden explorar otras soluciones que incluyan técnicas de transformación o selección de características.

- **Resultados y Evaluación**: análisis y comparación de los resultados.

Se valorará la inclusión de secciones que expliquen el proceso de experimentación, análisis de errores y aprendizajes obtenidos a lo largo de la tarea.

Cita los **recursos** que encuentres que te hayan sido de utilidad. Puedes usar libremente asistentes con LLMs (usándolos para entender lo que sucede) o fuentes de Internet (hay multitud de explicaciones en las que se usa, como por ejemplo [este vídeo de Dot CSV](https://www.youtube.com/watch?v=FVozZVUNOOA&ab_channel=DotCSV))