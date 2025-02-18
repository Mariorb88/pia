# Tarea 7: detección de enfermedades de tiroides

1. Crea un nuevo repositorio de trabajo en [avidaldo-ia24](https://github.com/organizations/avidaldo-ia24/repositories/new):
    - `Owner` debe ser `avidaldo-ia24`.
    - El nombre debe ser `t7-thyroid-detection-nombre1-apellido1`, sustituyendo `nombre1-apellido1` por tu identificador.
    - Ese nuevo repositorio debe ser **privado**.

> [!TIP]
> Puedes descargar este repo y subir los ficheros al tuyo para continuar desde allí siguiendo los mismos pasos que en la [tarea 6](https://github.com/avidaldo-ia24/t6-life-expectancy), pero esta vez [entrega la tarea en moodle](https://fpadistancia.edu.xunta.gal/mod/assign/view.php?id=1216540) solo cuando la tengas terminada o cuando quieras que revise lo que tienes hasta entonces.

2. Continúa el notebook "tarea7.ipynb" para crear un modelo de aprendizaje supervisado con scikit-learn de detección de hipotiroidismo e hipertiroidismo. El dataset está sacado de [aquí](https://www.kaggle.com/datasets/emmanuelfwerr/thyroid-disease-data/data). Incluyo al inicio del notebook la carga de datos y una simplificación de la variable objetivo para hacer más sencilla la tarea. El objetivo es que crees un modelo de clasificación que sea capaz de predecir si un paciente tiene hipotiroidismo o hipertiroidismo, ignorando el resto de categorías recogidas en el dataset original.

> [!TIP]
> Ten en cuenta lo explicado en el [notebook de sobre evaluación de modelos de clasificación](https://github.com/avidaldo/ia24/blob/main/sklearn/mnist_svm_eval.ipynb)
