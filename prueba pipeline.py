import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Cargar el DataFrame
df = pd.read_csv('./data/life_expectancy.csv')

# Separar la variable objetivo y las características
target = 'LifeExpectancy'
X = df.drop(columns=[target])
y = df[target]

# Eliminar registros donde LifeExpectancy sea nulo
X = X[y.notnull()]
y = y.dropna()

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Identificar variables categóricas y numéricas
categorical_cols = X.select_dtypes(include=['object']).columns
numerical_cols = X.select_dtypes(include=['number']).columns

# Crear el transformador para eliminar variables categóricas
drop_categorical = ('drop_cat', 'drop', categorical_cols)

# Crear el transformador para imputar valores numéricos y aplicar Z-score
impute_and_scale = Pipeline(steps=[
    ('impute', SimpleImputer(strategy='mean')),  # Imputar la media
    ('scale', StandardScaler())                 # Aplicar Z-score
])

scale_numerical = ('scale_num', impute_and_scale, numerical_cols)

# Combinar transformadores en un ColumnTransformer
preprocessor = ColumnTransformer(transformers=[drop_categorical, scale_numerical])

# Crear el pipeline con el modelo de regresión lineal
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

# Ajustar el pipeline a los datos de entrenamiento
pipeline.fit(X_train, y_train)

# Hacer predicciones
y_pred = pipeline.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")
