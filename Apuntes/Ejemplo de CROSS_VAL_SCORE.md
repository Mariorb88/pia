Claro, te voy a mostrar cómo usar **`cross_val_score`** en un **pipeline** de **scikit-learn**. **`cross_val_score`** permite realizar validación cruzada de forma más sencilla, ya que automáticamente divide los datos en varias particiones (folds), entrena el modelo en cada partición y evalúa su rendimiento.

### Ejemplo: Usando `cross_val_score` en un pipeline

Imagina que tienes un dataset con características y una columna objetivo, y deseas evaluar el rendimiento de un modelo de **Regresión Logística** dentro de un pipeline que incluya un **escalado de datos** y una **imputación de valores faltantes**.

```python
import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.datasets import load_iris
import numpy as np

# Cargar el dataset de ejemplo (en este caso, el Iris dataset)
data = load_iris()
X = data.data
y = data.target

# Crear el pipeline
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')),  # Imputar valores faltantes con la media
    ('scaler', StandardScaler()),  # Escalar las características
    ('model', LogisticRegression(max_iter=1000))  # Modelo de regresión logística
])

# Evaluar el modelo usando cross-validation
scores = cross_val_score(pipeline, X, y, cv=5, scoring='accuracy')  # 5 folds para validación cruzada

# Mostrar los resultados
print(f"Scores de validación cruzada: {scores}")
print(f"Promedio de precisión: {np.mean(scores)}")
```

### **Explicación del código**:

1. **Dataset**: Utilicé el dataset Iris (`load_iris()`) como ejemplo, pero puedes usar cualquier dataset de tu interés.
2. **Pipeline**: El pipeline consta de tres pasos:
   - **Imputación de valores faltantes** (`SimpleImputer`): Rellena los valores faltantes usando la media de cada columna.
   - **Escalado de características** (`StandardScaler`): Escala las características para que tengan media 0 y desviación estándar 1.
   - **Modelo de regresión logística** (`LogisticRegression`): El modelo que se va a entrenar.
3. **`cross_val_score`**: Se usa para realizar la validación cruzada. El argumento `cv=5` indica que se usarán 5 particiones (folds). El argumento `scoring='accuracy'` indica que se evaluará el rendimiento en términos de precisión (accuracy).
4. **Resultados**: El valor de **`scores`** contiene las precisiones obtenidas en cada fold. Al final, se muestra el promedio de estas precisiones.

### **Salida esperada** (puede variar según el modelo y dataset):

```plaintext
Scores de validación cruzada: [0.96666667 0.96666667 1.         0.96666667 1.        ]
Promedio de precisión: 0.9866666666666667
```

### **Notas**:
- **`cross_val_score`** realiza la validación cruzada sin necesidad de dividir explícitamente los datos en entrenamiento y prueba. Solo debes pasarle el pipeline y el conjunto de datos, y él se encarga del resto.
- **`cv=5`**: Número de folds para la validación cruzada (puedes ajustarlo según tus necesidades).
- Puedes cambiar el argumento **`scoring`** para usar diferentes métricas de evaluación, como `precision`, `recall`, `f1`, etc.

Este es un ejemplo simple, pero puedes usarlo para evaluar modelos más complejos o combinarlo con técnicas como **GridSearchCV** para la optimización de hiperparámetros. Si necesitas más detalles, ¡no dudes en preguntar!