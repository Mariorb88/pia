#-----------------------------------------------------------------------------------------------------
# 1.  Instalación de las bibliotecas necesarias
#-----------------------------------------------------------------------------------------------------
import tensorflow as tf
import numpy as np
import random
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense

#------------------------------------------------------------------------
# 2. Preparación de los datos
#------------------------------------------------------------------------
# 2.1. Creación de dos funciones
#-------------------------------------------------------------------------------
def celsiusFahrenheit(celsius):
    fahrenheit = ((celsius * 1.8) + 32)
    return fahrenheit

def FahrenheitError(fahrenheit):
    fahrenheit = fahrenheit * (1 + ( random.random() - random.random() ) * 0.25 )
    return fahrenheit

#-------------------------------------------------------------------------------
# 2.2. Generación de dos tablas: una para grados Celsius y otra para Fahrenheit
#      La lista Celsius es la de entrada de datos y la Fahrenheit la de salida
#-------------------------------------------------------------------------------
CELSIUS = np.random.randint( -150, 150, size = random.randint( 20, 1000 ) )
FAHRENHEIT = FahrenheitError( celsiusFahrenheit( CELSIUS ) )

#------------------------------------------------------------------------
# 3. Elección del modelo
#------------------------------------------------------------------------
modelo = tf.keras.Sequential()

#------------------------------------------------------------------------
# 4. Configuración de los parámetros del modelo:
#------------------------------------------------------------------------
#     El modelo elegido es el más sencillo: Perceptron
#       salida = peso  * X  + bias
#       salida = peso1 * X1 + peso2 * X2 + bias
#-------------------------------------------------------------------------------
modelo.add( Dense( units = 10, activation = 'relu', input_shape = [ 1 ] ) )   # Capa de entrada con 10 neuronas
modelo.add( Dense( units = 10, activation = 'relu' ) )                         # Capa oculta con 10 neuronas
modelo.add( Dense( units = 1 ) )                                              # Capa de salida con 1 neurona

#------------------------------------------------------------------------
# 5. Compilación del modelo
#------------------------------------------------------------------------
#     optimizer: algoritmo de optimización con el que se entrenará el modelo.
#     loss: función de pérdida que se minimizará durante el entrenamiento
#     metrics: métricas que monitorean el entrenamiento y la evaluación del modelo
#       - MÉTRICAS DE CLASIFICACIÓN
#             - accuracy  métrica de clasificación que mide la fracción de muestras correctamente clasificadas
#             - precision
#             - recall
#
#       - MÉTRICAS DE REGRESIÓN
#             - loss      medida de cuánto difieren las predicciones de los valores reales.
#-------------------------------------------------------------------------------
modelo.compile(
    optimizer = tf.keras.optimizers.Adam( 0.01 ), # Tasa de aprendizaje reducida
    loss = 'mean_squared_error',                  # Función de pérdida para regresión
    metrics = ['mean_squared_error']              # Métrica para evaluar durante el entrenamiento
)

#------------------------------------------------------------------------
# 6. Entrenamiento del modelo
#------------------------------------------------------------------------
#     Se utiliza la función fit sobre el modelo, especificando:
#       - Datos de entrada: 'celsius'
#       - Datos de salida esperados: 'fahrenheit'
#       - Número de interaciones: 'epochs'
#       - Si muestra evolución por pantalla: 'verbose'
#-------------------------------------------------------------------------------
print("Comenzamos el entrenamiento ...")
ACIERTOS = 0.90   # 90% de aciertos
INTENTOS = 0

while True:
    historial = modelo.fit( CELSIUS, FAHRENHEIT, epochs = 100, verbose = False ) # Más epochs
    INTENTOS = INTENTOS + 1
    perdida = historial.history[ 'loss' ][ -1 ]

    print( f"Iteración {INTENTOS} - Pérdida: {perdida}" )
    if perdida < ( 1 - ACIERTOS )/100:  # Criterio de parada
        break

print("Modelo ya entrenado ..." )

print( f"Totalidad de elementos {len(CELSIUS)}" )

#------------------------------------------------------------------------
# 7. Evaluación del modelo
#------------------------------------------------------------------------
evaluacion = modelo.evaluate( CELSIUS, FAHRENHEIT, verbose = 0 )
print( "\nResultados de la evaluación:" )
print( "----------------------------" )
print( f"Pérdida: {evaluacion[ 0 ]   * 100:.2f}%" )
print( f"Precisión: {evaluacion[ 1 ] * 100:.2f}%" )

#------------------------------------------------------------------------
# 8. Predicción o inferencia
#------------------------------------------------------------------------
# Generar predicciones
predicciones = modelo.predict( CELSIUS, verbose = False )

#------------------------------------------------------------------------
# Predicción gráfica
#------------------------------------------------------------------------
# Gráfico de dispersión de datos reales
plt.scatter( CELSIUS, FAHRENHEIT, color='red', label = 'Datos reales')

# Línea de predicción
plt.plot( CELSIUS, predicciones, color = 'blue', label = 'Predicciones' )

# Etiquetas y título
plt.xlabel( 'Celsius' )
plt.ylabel( 'Fahrenheit' )
plt.title(  'Datos reales vs Predicciones' )

# Leyenda
plt.legend()
plt.show()

#------------------------------------------------------------------------
# Fórmula asociada
#------------------------------------------------------------------------
capa = modelo.layers[0]
print( f"Fahrenheit = Celsius * {capa.get_weights()[0][0][0]:.4f} + {capa.get_weights()[1][0]:.4f}" )

#------------------------------------------------------------------------
# Predicción con un valor
#------------------------------------------------------------------------
print()
print("Hagamos una predicción")

# Más valores de prueba
for i in range(5):
    celsiusPrueba = random.randint(-150, 150)
    resultado = modelo.predict(np.array([celsiusPrueba]), verbose=False)
    print(f"{celsiusPrueba}ºC son {resultado[0][0]:.4f} ºF, frente a los reales {celsiusFahrenheit(celsiusPrueba):.4f} ºF")