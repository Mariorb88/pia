Para calcular la media de una columna con valores nulos, pero basándote en la agrupación de otra columna, puedes usar el método `groupby()` de **pandas** para agrupar los datos y luego aplicar la función de **media** en las filas con valores nulos, utilizando el parámetro `transform` o aplicando `fillna()` para llenar los valores nulos.

Aquí te dejo un ejemplo de cómo hacerlo:

### Ejemplo:

Supongamos que tienes un DataFrame llamado `df`, donde la columna `columna_a` contiene valores nulos, y deseas calcular la media de `columna_a` agrupada por `columna_b`, para reemplazar los valores nulos.

```python
import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'columna_a': [10, 20, None, 30, None, 40, 50, None],
    'columna_b': ['grupo1', 'grupo1', 'grupo1', 'grupo2', 'grupo2', 'grupo2', 'grupo3', 'grupo3']
}

df = pd.DataFrame(data)

# Agrupar por 'columna_b' y calcular la media de 'columna_a' para cada grupo
media_por_grupo = df.groupby('columna_b')['columna_a'].transform('mean')

# Reemplazar los valores nulos en 'columna_a' con la media correspondiente
df['columna_a'] = df['columna_a'].fillna(media_por_grupo)

print(df)
```

### Explicación:
1. **Agrupar** por `columna_b` usando `groupby()`.
2. **Calcular la media** de `columna_a` dentro de cada grupo con `transform('mean')`.
3. **Reemplazar** los valores nulos de `columna_a` con las medias calculadas de su grupo respectivo usando `fillna()`.

### Resultado:

```plaintext
   columna_a columna_b
0       10.0    grupo1
1       20.0    grupo1
2       15.0    grupo1
3       30.0    grupo2
4       35.0    grupo2
5       40.0    grupo2
6       50.0    grupo3
7       50.0    grupo3
```

En este caso, los valores nulos en `columna_a` se reemplazan con la media de su grupo respectivo de `columna_b`.

### Caso alternativo: **Si no deseas modificar los valores originales**, pero sí hacer un cálculo, puedes usar `transform()` directamente para obtener la media sin modificar el DataFrame:

```python
df['media_por_grupo'] = df.groupby('columna_b')['columna_a'].transform('mean')
```

De esta manera, tendrás la media calculada para cada grupo sin alterar los valores nulos de la columna original.

---

Si necesitas algún ajuste en este ejemplo, como hacerlo para otro tipo de operación o con otro formato de datos, no dudes en comentarlo. 😊