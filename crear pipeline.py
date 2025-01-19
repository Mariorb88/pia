import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Cargar los datos
file_path = 'life_expectancy.csv'  # Cambia esto por la ruta real de tu archivo
df = pd.read_csv(file_path)

# Seleccionar características (X) y la variable objetivo (y)
target_column = 'Life expectancy '  # Ajusta esto si el nombre de la columna tiene espacios o errores
X = df.drop(columns=[target_column])
y = df[target_column]

# 1. Preprocesamiento de columnas numéricas y categóricas
# Columnas numéricas (a las que se les puede imputar la media)
numerical_cols = X.select_dtypes(include=['int64', 'float64']).columns

# Columnas categóricas (a las que se les aplicará codificación one-hot)
categorical_cols = X.select_dtypes(include=['object']).columns

# Pipeline para preprocesar los datos:
# - Imputación de valores nulos para columnas numéricas
# - Codificación one-hot para columnas categóricas
preprocessor = ColumnTransformer(
    transformers=[
        ('num', SimpleImputer(strategy='mean'), numerical_cols),
        ('cat', OneHotEncoder(drop='first'), categorical_cols)
    ])

# 2. Crear el pipeline completo
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('scaler', StandardScaler()),  # Opcional: Escalar las características
    ('regressor', LinearRegression())
])

# 3. Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Ajustar el modelo usando el pipeline
pipeline.fit(X_train, y_train)

# 5. Evaluar el modelo
y_pred = pipeline.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Error medio cuadrado (MSE): {mse:.2f}")
print(f"Coeficiente de determinación (R²): {r2:.2f}")
