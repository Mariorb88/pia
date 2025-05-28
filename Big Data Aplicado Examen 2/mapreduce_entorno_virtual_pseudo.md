
# 🧠 MapReduce con entorno virtual en Hadoop Streaming (vía script intermedio)

Este enfoque permite usar un entorno virtual de Python comprimido (`entorno.zip`) en Hadoop Streaming, activándolo manualmente desde un `script.py` que ejecuta el verdadero `mapper.py`.

---

## 🧾 1. `script.py` (lanzador del mapper)

```python
# Pseudocódigo
SI no existe carpeta "venv":
    DESCOMPRIMIR "entorno.zip" en el directorio actual

EJECUTAR "./venv/bin/python3 mapper.py"
```

---

## 🔁 2. `mapper.py` (lector línea a línea de stdin)

```python
# Pseudocódigo
PARA cada línea en entrada estándar:
    DIVIDIR línea en palabras
    PARA cada palabra:
        ESCRIBIR palabra + "\t1" a salida estándar
```

---

## 📉 3. `reducer.py` (agregador de conteos)

```python
# Pseudocódigo
contador ← 0
palabra_actual ← ""

PARA cada línea en entrada estándar:
    SEPARAR palabra y valor
    SI palabra = palabra_actual:
        contador ← contador + valor
    SINO:
        SI palabra_actual ≠ "":
            ESCRIBIR palabra_actual + "\t" + contador
        palabra_actual ← palabra
        contador ← valor

# Escribir última palabra
SI palabra_actual ≠ "":
    ESCRIBIR palabra_actual + "\t" + contador
```

---

## 📦 4. `entorno.zip` (estructura del entorno virtual comprimido)

```plaintext
entorno.zip
└── venv/
    ├── bin/
    │   └── python3
    ├── lib/
    └── ...
```

> Este entorno debe contener todas las librerías necesarias (`pip install ...`) y estar comprimido con `zip -r entorno.zip venv/`.

---

## 🚀 5. Comando de ejecución con Hadoop/YARN

```bash
yarn jar /hadoop/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
  -input /entrada \
  -output /salida_contador \
  -mapper script.py \
  -file script.py \
  -file mapper.py \
  -file entorno.zip \
  -reducer reducer.py \
  -file reducer.py
```

---

## ✅ Ventajas

- No dependes de `-archives`
- Compatible con cualquier librería Python
- Control completo desde `script.py`
