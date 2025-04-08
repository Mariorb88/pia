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

        He probado a añadir 6 capas ocultas con 7 neuronas a modo didáctico-experimental y obviamente también se entrena sin problemas pero sí que he notado que tarda ligeramente más: [Prueba2](https://playground.tensorflow.org/#activation=linear&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.001&regularizationRate=0&noise=0&networkShape=7,7,7,7,7,7&seed=0.08033&showTestData=false&discretize=false&percTrainData=30&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=regression&initZero=false&hideText=false)

        Feature Engineering: Probando a añadir más características de entrada y el modelo se entrena bien. He probado a dejar la característica X1 y de esta manera nunca llega atener un error 0 ya que los valores no varían únicamente en un eje. [Prueba3](https://playground.tensorflow.org/#activation=linear&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.001&regularizationRate=0&noise=0&networkShape=&seed=0.65640&showTestData=false&discretize=false&percTrainData=30&x=true&y=false&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=regression&initZero=false&hideText=false)

    - Multi Gaussian

        Problema: En este dataset tenemos una representación de valores multi gaousiana por lo que el algoritmo Linear ya no será válido. Trabajaré con un 30% de datos destinado a test y dejaré el ruido y el número de batch con sus valores por defecto 0 % y 10.

        Hiperparámetros: Para este conjunto de datos usaré un Learning Rate de 0.003 Ya que seguramente necesite avanzar más rápido.
        Pruebo con el Algoritmo Tanh, con las car5acterísticas de entrada X1 y X2 y con 2 capas ocultas de 3 neuronas cada una.
        Con esta configuración el modelo se entrena en unos pocos segundos con un error bastante majo: [Prueba1](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-gauss&learningRate=0.003&regularizationRate=0&noise=0&networkShape=3,3&seed=0.75122&showTestData=false&discretize=true&percTrainData=30&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=regression&initZero=false&hideText=false)

        He probado a añadir 4 capas ocultas con 4 neuronas el resultado ha sido peor, tardando bastante más en entrenar el modelo: [Prueba2](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-gauss&learningRate=0.003&regularizationRate=0&noise=0&networkShape=4,4,4,4&seed=0.75122&showTestData=false&discretize=true&percTrainData=30&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=regression&initZero=false&hideText=false)

        Feature Engineering: En este caso añadiendo más características no he encontrado una mejora en el entrenamiento ya que los valores se alejaban de la distribución objetivo.

2. Clasificación:
    - Gaussian
        Problema: En este dataset tenemos una representación de valores claramente clasificados en 2 grupos Gausianos fácilmente identificables y separables por un plano. Trabajaré con un 30% de datos destinado a test y dejaré el ruido y el número de batch con sus valores por defecto 0 % y 10.

        Hiperparámetros: Al tratarse de un conjunto de datos sencillo y linealmente separable indicaré un Learning Rate de 0.001 y el algoritmo de Activación "Linear" y no voy a añadir capas ocultas por lo que tampoco habrá neuronas. Dejaré únicamente las características X1 y X2
        Con esta configuración el modelo se entrena en muy pocas Epoch, rápido y sin error: [Prueba1](https://playground.tensorflow.org/#activation=linear&batchSize=10&dataset=gauss&regDataset=reg-plane&learningRate=0.001&regularizationRate=0&noise=0&networkShape=&seed=0.69549&showTestData=false&discretize=false&percTrainData=30&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

        Evidentemente es un caso muy sencillo por lo que no haría falta probar con múltiples capas, neuronas u otro algoritmo, pero por experimentar he probado con el algoritmo Sigmoid con 3 capas ocultas y 6 neuronas cada una y aunque llega a entrenarse correctamente sí que tarda más: [Prueba2](https://playground.tensorflow.org/#activation=sigmoid&batchSize=10&dataset=gauss&regDataset=reg-plane&learningRate=0.001&regularizationRate=0&noise=0&networkShape=6,6,6&seed=0.12179&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

        Feature Engineering: Probando a añadir más características de entrada y el modelo se entrena bien. He probado a dejar la característica X1 y de esta manera nunca llega atener un error 0 ya que los valores no son separables con un único eje totalmente vertical. [Prueba3](https://playground.tensorflow.org/#activation=relu&batchSize=10&dataset=gauss&regDataset=reg-plane&learningRate=0.001&regularizationRate=0&noise=0&networkShape=2,2,2&seed=0.64335&showTestData=false&discretize=false&percTrainData=30&x=true&y=false&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)


    - Exclusive or
        Problema: En este dataset tenemos una representación de valores basada en la lógica XOR por lo que en este caso necesitaremos múltiples capas y neuroas al no ser linealmente separable. Trabajaré con un 30% de datos destinado a test y dejaré el ruido y el número de batch con sus valores por defecto 0 % y 10.

        Hiperparámetros: En este caso usando las variables de entrada X1 y X2 he usado un learning rate 0,003 para que avance más rápido debido a la complejidad del dataset y he añadido 2 capas ocultas con 4 neuronas cada una con el algoritmo de activación ReLU. De este modo el modelo se entrena bastante rápido: [Prueba1](https://playground.tensorflow.org/#activation=relu&batchSize=10&dataset=xor&regDataset=reg-plane&learningRate=0.003&regularizationRate=0&noise=0&networkShape=4,4&seed=0.14985&showTestData=false&discretize=true&percTrainData=30&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

        Probando con menos capas ocultas y neuronas en algunos casos llega a entrenarse bien debido a la semilla de la que parte pero se observa que no es un entrenamiento del que podamos extraer que siempore va a dar un buen resultado, sacando como conclusión que con estas features como mínimo deberíamos usar un mínimo de 2capas y entorno a 4 neuronas: [Prueba2](https://playground.tensorflow.org/#activation=relu&batchSize=10&dataset=xor&regDataset=reg-plane&learningRate=0.003&regularizationRate=0&noise=0&networkShape=2,3&seed=0.14985&showTestData=false&discretize=true&percTrainData=30&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

        Feature Engineering: En este caso parece que si usamos como variable de entrada el X1X2 podemos entrenar el módelo sin capas intermediasrápidamente y sin error porque básicamente la entrada de datos es igual a la salida . [Prueba3](https://playground.tensorflow.org/#activation=relu&batchSize=10&dataset=xor&regDataset=reg-plane&learningRate=0.003&regularizationRate=0&noise=0&networkShape=&seed=0.14985&showTestData=false&discretize=true&percTrainData=30&x=false&y=false&xTimesY=true&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)


    - Circle

        Problema: En este dataset tenemos una representación de valores en las que nos encontramos un grupo de valores gausiano rodeado por un círculo con otros valores, para entrenar este modelo necesitaremos múltiples capas y neuronas al no ser linealmente separable. Trabajaré con un 30% de datos destinado a test y dejaré el ruido y el número de batch con sus valores por defecto 0 % y 10.

        Hiperparámetros: En este caso usando las variables de entrada X1 y X2 he usado un learning rate 0,01 para que avance más rápido debido a la complejidad del dataset y he añadido 4 capas ocultas con 4 neuronas la primera y 2 la segunda con el algoritmo de activación Tanh. De este modo el modelo se entrena bastante rápido clasificando correctamente los distintos valores: [Prueba1](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.01&regularizationRate=0&noise=0&networkShape=4,2&seed=0.82071&showTestData=false&discretize=true&percTrainData=30&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

        Probando con menos capas ocultas y neuronas llega a entrenarse correctamente con Tanh con 1 capa oculta de 3 neuronas aunque tarda un poco más, este es el mínimo ya que si en lugar de 3 neuronas usamos 2 nunca llega reducir el error a valores aceptables: [Prueba2](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.01&regularizationRate=0&noise=0&networkShape=2&seed=0.82071&showTestData=false&discretize=true&percTrainData=30&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

        Feature Engineering: En este caso parece que si usamos como variable de entrada el X1² X2² podemos entrenar el módelo con una única capa de una neurona. [Prueba3](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=1&seed=0.28352&showTestData=false&discretize=true&percTrainData=30&x=false&y=false&xTimesY=false&xSquared=true&ySquared=true&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)


    - Spiral

        Problema: En este dataset tenemos una representación de valores en las que nos encontramos un grupo de valores gausiano rodeado por un círculo con otros valores, para entrenar este modelo necesitaremos múltiples capas y neuronas al no ser linealmente separable. Trabajaré con un 30% de datos destinado a test y dejaré el ruido y el número de batch con sus valores por defecto 0 % y 10.

        Hiperparámetros: En este caso usando las variables de entrada X1 y X2 he usado un learning rate 0,01 para que avance más rápido debido a la complejidad del dataset y he añadido 4 capas ocultas con 4 neuronas la primera y 2 la segunda con el algoritmo de activación Tanh. De este modo el modelo se entrena bastante rápido clasificando correctamente los distintos valores: [Prueba1](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.01&regularizationRate=0&noise=0&networkShape=4,2&seed=0.82071&showTestData=false&discretize=true&percTrainData=30&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

        Probando con menos capas ocultas y neuronas llega a entrenarse correctamente con Tanh con 1 capa oculta de 3 neuronas aunque tarda un poco más, este es el mínimo ya que si en lugar de 3 neuronas usamos 2 nunca llega reducir el error a valores aceptables: [Prueba2](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.01&regularizationRate=0&noise=0&networkShape=2&seed=0.82071&showTestData=false&discretize=true&percTrainData=30&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)

        Feature Engineering: En este caso parece que si usamos como variable de entrada el X1² X2² podemos entrenar el módelo con una única capa de una neurona. [Prueba3](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=1&seed=0.28352&showTestData=false&discretize=true&percTrainData=30&x=false&y=false&xTimesY=false&xSquared=true&ySquared=true&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)
