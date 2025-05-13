# Tarea 11: Redes Neuronales - California Housing

## 1. Repositorio
Crea un nuevo repositorio de trabajo en [avidaldo-ia24](https://github.com/organizations/avidaldo-ia24/repositories/new):

- `Owner` debe ser `avidaldo-ia24`.
- El nombre debe ser `t11-california-nombre1-apellido1`, sustituyendo `nombre1-apellido1` por tu identificador.
- Ese nuevo repositorio debe ser privado.


## 2. Tarea

Crea un *notebook* claro y estructurado llamado **`tarea11.ipynb`** proponiendo una alternativa con redes neuronales al problema de regresión de California Housing. Documenta todo el proceso justificando las decisiones y comentando los resultados.

### 2.1 *Baseline*

Tomaremos el [mejor modelo conseguido hasta ahora con el algoritmo Random Forest tras ajustar sus hiperparámetros](https://github.com/avidaldo/ia24/blob/main/end2end/e2e081_hyperparameters_tarea.ipynb) como *baseline*, con el que hemos conseguido un RMSE de en torno a 41600$, siendo nuestro objetivo mejorarlo.

### 2.2 Propuesta implementación y comparación de mejoras

Manteniendo el mismo *pipeline* de preprocesamiento (puedes separarlo a otro fichero externo .py e importarlo en el *notebook* de la tarea, por comodidad) y la misma métrica de evaluación (RMSE), **implementa una red neuronal que reduzca el RMSE del modelo base**.

>[!WARNING]
> Usaremos el mismo *pipeline* de preprocesamiento para poder comparar la eficiencia de los algoritmos (Random Forest vs Red Neuronal) para este problema. Sin embargo, esto podemos hacerlo en este caso ya que hemos desarrollado un preprocesador genérico, ya que un algoritmo basado en árboles de decisión (como Random Forest) no requeriría escalar los datos ni hacer OHE, mientras que una red neuronal sí.

>[!IMPORTANT]
> Puedes buscar otros ejemplos de modelos sobre este dataset (es muy popular) y consultar asistentes para investigar opciones de cómo implementar la red neuronal, pero no olvides utilizar los foros o entregar tus versiones parciales para poder tener feedback si no eres capaz de entrenar un modelo que mejore la *baseline*.




