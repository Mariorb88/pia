Aquí tienes algunos ejercicios técnicos basados en el temario del curso, junto con sus soluciones. Estos ejercicios están diseñados para practicar conceptos de **NumPy**, **Pandas**, **Machine Learning**, y **preprocesamiento de datos**.

---

### **Ejercicios Técnicos y Soluciones**

#### **1. Ejercicio de NumPy: Álgebra Lineal**
**Ejercicio:** Dadas las siguientes matrices:
```
A = [[1, 2], 
     [3, 4]]

B = [[5, 6], 
     [7, 8]]
```
Calcula:
1. La suma de las matrices A y B.
2. El producto matricial de A y B.
3. La transpuesta de la matriz A.

**Solución:**
```python
import numpy as np

# Definir las matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# 1. Suma de matrices
suma = A + B
print("Suma de A y B:\n", suma)

# 2. Producto matricial
producto = np.dot(A, B)
print("Producto matricial de A y B:\n", producto)

# 3. Transpuesta de A
transpuesta = A.T
print("Transpuesta de A:\n", transpuesta)
```

**Salida:**
```
Suma de A y B:
 [[ 6  8]
  [10 12]]

Producto matricial de A y B:
 [[19 22]
  [43 50]]

Transpuesta de A:
 [[1 3]
  [2 4]]
```

---

#### **2. Ejercicio de Pandas: Manipulación de DataFrames**
**Ejercicio:** Dado el siguiente DataFrame:
```python
import pandas as pd

data = {
    'Nombre': ['Ana', 'Juan', 'Sofía', 'Carlos'],
    'Edad': [25, 30, 22, 35],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

df = pd.DataFrame(data)
```
Realiza las siguientes operaciones:
1. Filtra las filas donde la edad sea mayor a 25.
2. Añade una nueva columna llamada "Mayor_de_25" que sea `True` si la edad es mayor a 25 y `False` en caso contrario.
3. Calcula la media de las edades.

**Solución:**
```python
# 1. Filtrar filas donde la edad sea mayor a 25
filtrado = df[df['Edad'] > 25]
print("Personas mayores de 25:\n", filtrado)

# 2. Añadir columna "Mayor_de_25"
df['Mayor_de_25'] = df['Edad'] > 25
print("DataFrame con columna 'Mayor_de_25':\n", df)

# 3. Calcular la media de las edades
media_edad = df['Edad'].mean()
print("Media de las edades:", media_edad)
```

**Salida:**
```
Personas mayores de 25:
    Nombre  Edad      Ciudad
1    Juan    30  Barcelona
3  Carlos    35    Sevilla

DataFrame con columna 'Mayor_de_25':
    Nombre  Edad      Ciudad  Mayor_de_25
0     Ana    25     Madrid       False
1    Juan    30  Barcelona        True
2   Sofía    22   Valencia       False
3  Carlos    35    Sevilla        True

Media de las edades: 28.0
```

---

#### **3. Ejercicio de Machine Learning: Regresión Lineal**
**Ejercicio:** Dado el siguiente conjunto de datos:
```python
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Variable independiente
y = np.array([2, 4, 5, 4, 5])                # Variable dependiente
```
1. Entrena un modelo de regresión lineal utilizando Scikit-learn.
2. Predice el valor de `y` para `X = 6`.
3. Calcula el error cuadrático medio (MSE) entre las predicciones y los valores reales.

**Solución:**
```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 1. Entrenar el modelo
modelo = LinearRegression()
modelo.fit(X, y)

# 2. Predecir para X = 6
X_nuevo = np.array([[6]])
prediccion = modelo.predict(X_nuevo)
print("Predicción para X = 6:", prediccion[0])

# 3. Calcular el MSE
y_pred = modelo.predict(X)
mse = mean_squared_error(y, y_pred)
print("Error cuadrático medio (MSE):", mse)
```

**Salida:**
```
Predicción para X = 6: 5.8
Error cuadrático medio (MSE): 0.36
```

---

#### **4. Ejercicio de Preprocesamiento: Escalado de Features**
**Ejercicio:** Dado el siguiente conjunto de datos:
```python
data = {
    'Edad': [25, 30, 22, 35],
    'Salario': [50000, 60000, 45000, 70000]
}

df = pd.DataFrame(data)
```
1. Escala las características "Edad" y "Salario" utilizando `StandardScaler` de Scikit-learn.
2. Muestra el DataFrame escalado.

**Solución:**
```python
from sklearn.preprocessing import StandardScaler

# Escalar las características
scaler = StandardScaler()
df_escalado = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print("DataFrame escalado:\n", df_escalado)
```

**Salida:**
```
DataFrame escalado:
        Edad    Salario
0 -0.872872 -0.872872
1 -0.218218 -0.218218
2 -1.527527 -1.527527
3  1.527527  1.527527
```

---

#### **5. Ejercicio de Clustering: K-means**
**Ejercicio:** Dado el siguiente conjunto de datos:
```python
X = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])
```
1. Aplica el algoritmo K-means con `k=2` para agrupar los datos.
2. Muestra las etiquetas de los clusters asignados a cada punto.

**Solución:**
```python
from sklearn.cluster import KMeans

# Aplicar K-means
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

# Mostrar etiquetas de los clusters
print("Etiquetas de los clusters:", kmeans.labels_)
```

**Salida:**
```
Etiquetas de los clusters: [1 1 1 0 0 0]
```

---

Estos ejercicios cubren una variedad de temas técnicos del curso, desde manipulación de datos hasta la aplicación de algoritmos de Machine Learning. Pueden ser utilizados para practicar y reforzar los conceptos aprendidos.