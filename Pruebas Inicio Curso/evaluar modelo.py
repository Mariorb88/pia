import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Cargar los datos
file_path = "./life_expectancy.csv"  #
df = pd.read_csv(file_path)

# 2. Preprocesar los datos
# Rellenar valores nulos con la media
df.fillna(df.mean(numeric_only=True), inplace=True)

# Seleccionar características (X) y la variable objetivo (y)
# Suponiendo que queremos predecir 'Life expectancy'
target_column = 'LifeExpectancy'  # Ajusta esto si el nombre de la columna tiene espacios o errores
X = df.drop(columns=[target_column])
y = df[target_column]

# Convertir datos categóricos (si existen) a variables dummy
X = pd.get_dummies(X, drop_first=True)

# 3. Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluar el modelo
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Error medio cuadrado (MSE): {mse:.2f}")
print(f"Coeficiente de determinación (R²): {r2:.2f}")

# Opcional: Mostrar coeficientes del modelo
coef_df = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
})
print("\nCoeficientes del modelo:")
print(coef_df)
