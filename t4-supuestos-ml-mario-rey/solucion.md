# Tarea 4: Supuestos sobre modelos de aprendizaje automático


## Casos detallados:

Explica qué tipo de aprendizaje automático y qué tipo de problema de aprendizaje automático serían los siguientes casos. Investiga qué algoritmos serían más adecuados para abordarlos.


### Supuesto 1: diabetes

*Queremos desarrollar un modelo que ayude a detectar posibles casos de diabetes entre mujeres. Contamos con una base de datos de 156.374 fichas con diferentes casos ya estudiados. Tenemos los siguientes campos en cada ficha: edad, número de embarazos, nivel de glucosa, presión sanguínea, pliegue cutáneo, insulina, índice de masa corporal, historial familiar de diabetes y si tiene diabetes o no.*

Se trata de un problema de **aprendizaje supervisado**. El objetivo es predecir si una mujer tiene diabetes o no, por lo que es un problema de **clasificación binaria**. Se pueden aplicar algoritmos como regresión logística, árboles de decisión, random forest, SVM. El dataset es suficientemente grande como para poder aplicar **redes neuronales**, pero con ello perderíamos **interpretabilidad** del modelo, que en este caso puede ser importante; una regresión logística podría ser suficiente, dado que es un algoritmo sencillo y rápido que funciona bien en problemas de clasificación binaria.


### Supuesto 2: inmobiliaria

*Queremos obtener un modelo que prediga el precio de venta de un inmueble. Nuestra base de datos consta de 239.751 inmuebles vendidos en el último año en todo el territorio nacional. Contamos con la siguiente información por cada inmueble: metros cuadrados habitables, número de habitaciones, categoría de inmueble (piso, casa, adosado), código postal donde se encuentra el inmueble, valor según catastro, año de construcción, número de reformas realizadas hasta la fecha y precio de venta.*

Si nos piden predecir algo y ese algo es uno de los datos que nos aportan en la base de datos (en este caso el precio de venta del inmueble), está claro que se trata de un Aprendizaje Automático **Supervisado**, en el que el dato objetivo es el precio de venta. Se trata de un valor numérico real, por lo que se trata de un problema de regresión. Además podemos presuponer que va a tener relación lineal con la mayoría de los otros datos disponibles. Por tanto podríamos utilizar por ejemplo un algoritmo de regresión lineal. Sin embargo, el código postal o la categoría de inmueble pueden tener una relación no lineal con el precio, por lo que podríamos utilizar regresión polinómica, que es una extensión de la regresión lineal pero que permite capturar relaciones no lineales. Al igual que en el caso anterior, el dataset es suficientemente grande como para poder aplicar redes neuronales, pero con ello perderíamos **interpretabilidad** del modelo, que en este caso puede ser importante.


### Supuesto 3: fraude en tarjetas de crédito

*Queremos obtener un modelo que ayude a detectar posibles usos fraudulentos en tarjetas de crédito. Nuestra base de datos cuenta con 2.351.298 datos de transacciones en los últimos nueve meses. Para cada transacción contamos con estos datos: fecha, hora, localización (código postal) donde se ha realizado la transacción, cantidad, tipo de dispositivo en el que se ha realizado la transacción (cajero, comercio de productos, comercio de servicios), saldo medio del propietario en el último año y saldo actual del propietario en el momento de hacer la transacción.*

En este caso no contamos entre los datos con ningún campo relacionado directamente con lo que queremos saber (si ha habido uso fraudulento o no). Es un caso de Aprendizaje Automático **No supervisado**. Se trata de un problema de "**detección de anomalías**". Se pueden aplicar algoritmos como **DBSCAN** (clusterización basada en densidad, útil para detectar outliers), ***Isolation Forest*** (identificación de anomalías basada en árboles de decisión) o **Autoencoders** (reconstrucción para identificar puntos que no encajan bien en los datos normales).


### Supuesto 4: detección de caras en vídeo

*Queremos incorporar en la cámara de fotos del móvil una tecnología que reconozca caras para que en esos casos la cámara las enfoque prioritariamente al resto de elementos que aparezcan en el encuadre. Contamos con un banco de más de 2.000.000 de imágenes clasificadas y etiquetadas en las que se indica en cuáles hay rostros humanos, y, en las que sí los hay, en qué zonas de la imagen se encuentran.*

Usaremos nuestra base de datos de imágenes para entrenar un modelo de **aprendizaje supervisado**. Se trataría en principio de un problema de **clasificación**, pero al buscar una detección en tiempo real el proceso es más complejo: se trata de un problema de **detección de objetos**. Para un problema de este tipo se utilizan **redes neuronales convolucionales (CNN)**, por ejemplo sistemas como **YOLO**.


## Casos abiertos:

Haz un breve análisis preliminar indicando el tipo de aprendizaje y el tipo de problema. Matiza qué información habría que pedir al cliente que no se cite explícitamente. Los casos pueden tener varios abordajes dependiendo de la información que falta.


### Supuesto 5: dígitos escritos a mano

*Tenemos un conjunto de imágenes de dígitos escritos a mano y queremos hacer un modelo que permita identificar qué dígito es cada imagen.*

Se trata de un problema de **aprendizaje supervisado, asumiendo que los dígitos están etiquetados**. El problema es de **clasificación**, ya que se busca asignar una etiqueta a cada imagen.
KNN es un algoritmo que ha dado buenos resultados con el clásico dataset MNIST, o también SVM, pero destacan principalmente las redes neuronales convolucionales (CNN), que son especialmente útiles para el procesamiento de imágenes.

**Si no contásemos con las etiquetas de las imágenes, podríamos plantear un problema de clustering (no supervisado)**, para intentar agrupar las imágenes en función de sus características, sabiendo que buscaríamos agruparlas en 10 grupos (uno por cada dígito). Podríamos aplicar K-means con K fijado a 10.


### Supuesto 6: análisis de sentimientos en *tweets*

*Tenemos un conjunto de *tweets* y una indicación por cada uno de si el sentimiento del tweet fue positivo, negativo o neutral. Queremos un modelo que prediga el sentimiento de futuros tweets.*

Se trata de un problema de **Procesamiento de Lenguaje Natural (NLP)**. En concreto, es un problema de análisis de sentimientos, que es un tipo de **clasificación supervisada**.

Algoritmos clásicos para estas tareas son **Naive Bayes**, **SVM**, **Regresión Logística** o **Random Forest**, aunque con el auge de las redes neuronales, se pasó a utilizar **redes neuronales recurrentes (RNN)** o **redes neuronales convolucionales (CNN)**, y más recientemente el estándar en NLP son las **redes neuronales transformer**.


### Supuesto 7: viviendas vendidas

*Tenemos un conjunto de registros sobre viviendas vendidas en el último año (ubicación, cantidad de habitaciones, precio, etc.) y queremos hacer un modelo que permita predecir el precio por el que se va a vender una vivienda en el futuro.*

Mismo caso que el supuesto 2, pero con menos información. Se trata de un problema de **aprendizaje supervisado**. El objetivo es predecir el precio de venta de una vivienda, por lo que es un problema de **regresión**. Dado que solo se citan dos *features* (ubicación y cantidad de habitaciones), es importante reseñar que una de ellas (la ubicación) puede no guardar relación lineal con el precio, por lo que la una regresión lineal podría no ser suficiente. En este caso, se podría utilizar regresión polinómica, que es una extensión de la regresión lineal pero que permite capturar relaciones no lineales. También se podría utilizar un algoritmo de regresión no paramétrico como como **Random Forest** o una **red neuronal**.


### Supuesto 8: clasificación de flores

*Queremos un modelo que permita identificar distintos tipos de flores partiendo de un conjunto de datos que contiene medidas del largo y ancho de los pétalos y sépalos de muchas flores.*

**Asumiendo que las flores están etiquetadas, se trata de un problema de clasificación (supervisado)**. Podríamos recurrir a algoritmos como regresión logística, KNN, árboles de decisión, random forest, SVM, etc.

**Si no contásemos con las etiquetas, podríamos plantear un problema de clustering (no supervisado)**, para intentar agrupar las flores en función de sus características. El algoritmo más común es K-means.

En ambos casos, se podría considerar el uso de redes neuronales si se dispone de suficientes datos (del orden de más de 1000 imágenes por clase).


### Supuesto 9: diagnóstico médico

*Queremos trabajar en un modelo de diagnóstico médico. Tenemos un registro de pacientes con enfermedades y sus síntomas.*

Entendiendo que los **síntomas son las variables predictoras** y los pacientes están **etiquetados con la enfermedad** que padecen, se trataría de un problema de **clasificación (supervisado)**. En este caso al poder un paciente tener más de una enfermedad, se trataría de un problema de **clasificación multietiqueta (*multilabel*)**. Asumiendo que además hay un gran número de clases y uchas variables predictoras con relaciones no lineales, probablemente trabajaríamos con redes neuronales.


### Supuesto 10: retrasos en vuelos

*Tenemos el registro de todos los vuelos de una aerolínea (horas de partida y de llegada, origen, destino. tripulación, etc.) y queremos hacer un modelo que permita predecir si un vuelo va a llegar tarde o no.*

Se asume que tenemos las horas de llegada esperada y real (son datos fácilmente accesibles). Claramente nos encontramos ante **aprendizaje supervisado**, ya que tenemos la información a predecir: sabemos si un avión llegó o no con retraso. Pero lo sabemos implícitamente: **una variable objetivo binaria se podría generar como variable sintética resultado de comparar la hora de llegada estimada y la real. Con esa variable objetivo binaria se podría aplicar un algoritmo de clasificación**.

Si asumimos que el dataset puede estar desequilibrado (que la mayoría de vuelos llegan a tiempo), existen algoritmos más robustos para este tipo de problemas, como **Random Forest** o **SVM**. También se podrían utilizar redes neuronales.

Es por eso que probablemente sea mejor **modelar el problema como de regresión, prediciendo en lugar de si el avión llegó tarde o no, cuánto se retrasó.** Una vez sabemos cuánto se retrasó, podemos poner un umbral para decidir si consideramos que llegó tarde o no en posprocesamiento, pero si lo hacemos en preprocesamiento, estaríamos, como ya se comentó, perdiendo información valiosa. En cualquier caso, siempre se puede probar ambos enfoques y ver cuál funciona mejor.


### Supuesto 11: ciberseguridad

*Queremos detectar ciberataques a la red de nuestra empresa, para ello el conjunto de datos sería tráfico de red, con características como direcciones IP, puertos, duración de la sesión, cantidad de datos transferidos, etc.*

Se trata de un problema de **detección de anomalías (no supervisado)**, similar al de encontrar casos fraudulentos en usos de tarjetas de crédito cuando no están etiquetados. Podría también tratarse con un **problema de clasificación binaria (supervisado)** si se dispusiese de datos etiquetados como ataques o no ataques, pero hay que tener en cuenta que los ataques pueden ser muy variados y no siempre se pueden etiquetar de forma sencilla.


### Supuesto 12

*Queremos hacer un filtro de *spam* para el correo electrónico. Tenemos un conjunto de mensajes etiquetados como *spam* o no *spam*.*

Problema de **clasificación binaria (supervisado)**. Tradicionalmente se aplican Naive Bayes, SVM y arboles de decisión, regresión logística, pero en la actualidad las redes neuronales son muy efectivas en este tipo de problemas, aplicando técnicas de **NLP**.

