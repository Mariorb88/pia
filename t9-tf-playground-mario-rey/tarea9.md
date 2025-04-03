# Tarea 9: Playground online de TensorFlow

Problema: Breve resumen de las características y retos del dataset. Puedes también ver los efectos de modificar ratio train/test, el ruido o el tamaño de lote.

Hiperparámetros: arquitectura del modelo: Número de capas, cantidad de neuronas por capa y la razón detrás de estas elecciones y configuración elegida (tasa de aprendizaje, épocas, regularización, etc.). Añade la URL de la configuración utilizada. También puedes añadir capturas.

Feature Engineering: Proponer al menos una solución que utilice únicamente las características básicas (X1 y X2). Adicionalmente, se pueden explorar otras soluciones que incluyan técnicas de transformación o selección de características.

Resultados y Evaluación: análisis y comparación de los resultados.

1. Regresión:
    - Plane:
    
        Problema: En este dataset tenemos una representación de valores continuos en diagonal en el que podemos observar una relación lineal por la transición de los valores. Trabajaré con un 30% de datos destinado a test y dejaré el ruido y el número de batch con sus valores por defecto 0 % y 10.

        Hiperparámetros: Ya qué parece un conjunto de datos sencillo y lineal indicaré un Learning Rate de 0.001 y el algoritmo de Activación "Linear" y no voy a añadir capas ocultas por lo que tampoco habrá neuronas. Dejaré únicamente las características X1 y X2
        Con esta configuración el modelo se entrena en muy pocas Epoch, rápido y sin error: [Prueba1](https://playground.tensorflow.org/#activation=linear&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.001&regularizationRate=0&noise=0&networkShape=&seed=0.08033&showTestData=false&discretize=false&percTrainData=30&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=regression&initZero=false&hideText=false)

        He probado a añador 6 capas ocultas con 7 neuronas a modo didáctico-experimental y obviamente también se entrena sin problemas pero sí que he notado que tarda ligeramente más: [Prueba2](https://playground.tensorflow.org/#activation=linear&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.001&regularizationRate=0&noise=0&networkShape=7,7,7,7,7,7&seed=0.08033&showTestData=false&discretize=false&percTrainData=30&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=regression&initZero=false&hideText=false)

        Feature Engineering: Probando a añadir más características de entrada y el modelo se entrena bien. He probado a dejar la característica X1 y de esta manera nunca llega atener un error 0 ya que los valores no varían únicamente en un eje. [Prueba3](https://playground.tensorflow.org/#activation=linear&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.001&regularizationRate=0&noise=0&networkShape=&seed=0.65640&showTestData=false&discretize=false&percTrainData=30&x=true&y=false&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=regression&initZero=false&hideText=false)

    - Multi Gaussian

        Problema: En este dataset tenemos una representación de valores multi gaousiana por lo que el algoritmo Linear ya no será válido. Trabajaré con un 30% de datos destinado a test y dejaré el ruido y el número de batch con sus valores por defecto 0 % y 10.

        Hiperparámetros: Para este conjunto de datos usaré un Learning Rate de 0.003 Ya que seguramente necesite avanzar más rápido.
        Pruebo con el Algoritmo Tanh, con las car5acterísticas de entrada X1 y X2 y con 2 capas ocultas de 3 neuronas cada una.
        Con esta configuración el modelo se entrena en unos pocos segundos con un error bastante majo: [Prueba1](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-gauss&learningRate=0.003&regularizationRate=0&noise=0&networkShape=3,3&seed=0.75122&showTestData=false&discretize=true&percTrainData=30&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=regression&initZero=false&hideText=false)

        He probado a añador 4 capas ocultas con 4 neuronas el resultado ha sido peor, tardando bastante más en entrenar el modelo: [Prueba2](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-gauss&learningRate=0.003&regularizationRate=0&noise=0&networkShape=4,4,4,4&seed=0.75122&showTestData=false&discretize=true&percTrainData=30&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=regression&initZero=false&hideText=false)

        Feature Engineering: En este caso añadiendo más características no he encontrado una mejora en el entrenamiento ya que los valores se alejaban de la distribución objetivo.

2. Clasificación:
    - Gaussian
    - Exclusive or
    - Circle
    - Spiral

