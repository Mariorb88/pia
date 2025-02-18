Convertir variables categóricas a numéricas es un paso esencial en el preprocesamiento de datos para muchos modelos de machine learning, ya que los algoritmos generalmente no pueden trabajar con datos categóricos directamente. Aquí tienes algunos de los métodos más comunes para hacer esta conversión:

1. Label Encoding (Codificación de Etiquetas)
Este método asigna un número único a cada categoría dentro de una variable categórica. Es útil cuando hay un orden o jerarquía en las categorías (por ejemplo, "Bajo", "Medio", "Alto").

Ejemplo:
Supón que tienes una columna color con categorías ['Rojo', 'Verde', 'Azul'].

python
Copiar
Editar
from sklearn.preprocessing import LabelEncoder

# Crear el codificador
le = LabelEncoder()

# Datos de ejemplo
color = ['Rojo', 'Verde', 'Azul', 'Verde', 'Rojo']

# Convertir las etiquetas a números
color_encoded = le.fit_transform(color)

print(color_encoded)  # Salida: [2 1 0 1 2]
Cuando usarlo:
Útil cuando las categorías tienen un orden implícito o ordinal.
No se recomienda usarlo en variables categóricas nominales (sin orden), ya que los modelos pueden interpretar los valores como números con relaciones ordinales.
2. One-Hot Encoding (Codificación One-Hot)
La codificación One-Hot convierte cada categoría en una nueva columna binaria (0 o 1). Cada categoría se representa como una columna separada y la presencia de esa categoría se marca con un 1, mientras que el resto son 0.

Ejemplo:
Supón que tienes una columna color con categorías ['Rojo', 'Verde', 'Azul'].

python
Copiar
Editar
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Datos de ejemplo
color = ['Rojo', 'Verde', 'Azul', 'Verde', 'Rojo']

# Crear el codificador
encoder = OneHotEncoder(sparse=False)  # sparse=False para obtener un DataFrame en lugar de una matriz dispersa

# Ajustar y transformar
color_encoded = encoder.fit_transform(pd.DataFrame(color))

# Convertirlo a un DataFrame para mejor visualización
color_df = pd.DataFrame(color_encoded, columns=encoder.categories_[0])

print(color_df)
Salida:
plaintext
Copiar
Editar
   Azul  Rojo  Verde
0   0.0   1.0    0.0
1   0.0   0.0    1.0
2   1.0   0.0    0.0
3   0.0   0.0    1.0
4   0.0   1.0    0.0