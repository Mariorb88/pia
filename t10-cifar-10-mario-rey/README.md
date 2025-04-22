# Tarea 10: CIFAR-10 con Pytorch

## 1. Repositorio
Crea un nuevo repositorio de trabajo en [avidaldo-ia24](https://github.com/organizations/avidaldo-ia24/repositories/new):

- `Owner` debe ser `avidaldo-ia24`.
- El nombre debe ser `t10-cifar-10-nombre1-apellido1`, sustituyendo `nombre1-apellido1` por tu identificador.
- Ese nuevo repositorio debe ser privado.


## 2. Tarea

Crea un *notebook* claro y estructurado llamado **`tarea10.ipynb`** con tu solución para el problema de clasificación de CIFAR-10 usando PyTorch. Documenta todo el proceso siguiendo las instrucciones que se indican en las siguientes secciones.

### 2.1 Documentación base

Utilizaremos como base el [tutorial oficial de PyTorch para la clasificación en CIFAR-10](https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html)  

Estudia detenidamente y ejecuta el código del tutorial proporcionado. Asegúrate de comprender cada bloque: carga y preprocesamiento de datos (transforms), definición de la arquitectura CNN propuesta, definición de la función de pérdida (loss) y el optimizador, y el bucle de entrenamiento y evaluación.

> [!NOTE]  
> Hemos visto [los fundamentos de las redes neuronales (FNNs) y las redes convolucionales (CNNs), así como su implementación básica en PyTorch](https://github.com/avidaldo/ia24#redes-neuronales).


> [!TIP]  
> Tienes también los ejemplos [FNN y CNN para CIFAR-10 en escala de grises](https://github.com/avidaldo/ia24/blob/main/pytorch/CIFAR10_gray.ipynb) donde se aborda este mismo problema pero convirtiendo el dataset a escala de grises para simplificarlo y que sea más similar a MNIST. Sin embargo, CIFAR-10 tiene 3 canales de color (RGB), por lo que el problema es más complejo: en MNIST se tiene una imagen de 28x28x1 (1 canal: un número con el valor de gris para cada píxel), mientras que en CIFAR-10 se tiene una imagen de 32x32x3 (3 canales: un array de 3 valores -rojo, verde y azul- para cada píxel).

### 2.2 Conjunto de validación

El tutorial original evalúa directamente sobre el conjunto de test ya que solo presenta el resultado final y no realiza ajustes de hiperparámetros. Para poder experimentar y seleccionar la mejor arquitectura sin sesgar los resultados hacia el conjunto de test, es **fundamental** modificar el código para crear un **conjunto de validación**.

El conjunto de test original (10,000 imágenes) se debe reservar exclusivamente para la evaluación final del modelo que selecciones como el mejor.

### 2.3 Entrenamiento y evaluación del modelo base (*Baseline*)

Entrena la arquitectura CNN propuesta en el tutorial utilizando tu nuevo conjunto de entrenamiento.
Evalúa su rendimiento (*accuracy* y *loss*) periódicamente (p.ej., cada *epoch*) sobre el conjunto de validación. Guarda las curvas de aprendizaje (*loss/accuracy* vs. *epochs*) para entrenamiento y validación.
Este rendimiento en validación será tu línea base (***baseline***) con la que compararás tus propuestas posteriores. El objetivo es mejorar este rendimiento.

### 2.4 Propuesta implementación y comparación de mejoras

Diseña y programa otra arquitectura que intente mejorar el rendimiento del modelo base. **Justifica** las hipótesis que propones. ¿Por qué crees que podrían mejorar el rendimiento?

Entrena tus nuevas arquitecturas utilizando **exactamente los mismos conjuntos de entrenamiento y validación** y con la mismas métricas de evaluación y función de pérdida que usaste para la *baseline* para poder compara el rendimiento de cada una.

> [!TIP]  
> Para cada una de las propuestas de arquitectura, puedes ajustar hiperparámetros de entrenamiento (como el optimizador, la tasa de aprendizaje, batch size, etc.) si lo consideras necesario, con el fin de asegurar que cada arquitectura pueda mostrar su potencial de rendimiento de manera justa antes de compararlas. No es necesario hacer un ajuste exhaustivo (como Grid Search o Randomized Search) ni incluir todo el código de cada prueba intermedia que realices, pero sí debes **dejar comentarios en el notebook explicando brevemente qué ajustes probaste para cada arquitectura y cuáles fueron los finales utilizados**, justificando tu elección final de hiperparámetros para esa arquitectura.

Evalúa su rendimiento en el conjunto de **validación** de la misma forma que hiciste con el modelo base (métricas por *epoch*, curvas de aprendizaje).

**Compara** de forma clara (p.ej., con tablas y gráficas superpuestas) las curvas de aprendizaje y el rendimiento final en **validación** de todos los modelos probados (baseline y tus alternativas).

> [!IMPORTANT]  
> Repite este proceso al menos una vez más, **mostrando los resultados de al menos 2 arquitecturas alternativas a la propuesta original**.

> [!IMPORTANT]  
> Muestra en las celdas de entrenamiento el tiempo que tarda en entrenar cada arquitectura.


### 2.5 Selección del mejor modelo y evaluación final en test

Basándote únicamente en los resultados obtenidos en el conjunto de validación, selecciona la arquitectura que haya demostrado el mejor rendimiento. Justifica tu elección.

Una vez seleccionada tu mejor arquitectura, reentrénala usando la unión de los conjuntos de entrenamiento y validación para luego hacer la evaluación final en test. 


