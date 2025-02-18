### 🔹 **Accuracy (Exactitud)** vs. **Precision (Precisión)**

Ambas son **métricas de evaluación** utilizadas para medir el rendimiento de un modelo de clasificación, pero se enfocan en aspectos diferentes de las predicciones. A continuación, te explico sus diferencias clave:

---

### 1. **Accuracy (Exactitud)**

**Definición:**  
La exactitud mide la **proporción de predicciones correctas** sobre el total de predicciones realizadas. Es una métrica simple que se calcula así:

\[
\text{Accuracy} = \frac{\text{Predicciones correctas}}{\text{Total de predicciones}}
\]

**Fórmula:**
\[
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
\]
Donde:
- **TP (True Positives)**: Verdaderos positivos
- **TN (True Negatives)**: Verdaderos negativos
- **FP (False Positives)**: Falsos positivos
- **FN (False Negatives)**: Falsos negativos

**Cuando usarla:**  
La **exactitud** es útil cuando el conjunto de datos está **balanceado**, es decir, cuando las clases positivas y negativas están igualmente distribuidas.

**Ejemplo:**
Si un modelo predice correctamente que 90 de 100 pacientes están sanos, pero falla en detectar a 10 con alguna enfermedad, la **exactitud** podría ser bastante alta, pero el modelo estaría mal porque no detectó a los enfermos.

---

### 2. **Precision (Precisión)**

**Definición:**  
La **precisión** mide la proporción de **predicciones positivas correctas** sobre todas las predicciones positivas realizadas. Es decir, de todas las veces que el modelo predijo que algo es positivo, ¿cuántas veces fue realmente correcto?

\[
\text{Precision} = \frac{\text{TP}}{\text{TP + FP}}
\]

**Fórmula:**
\[
\text{Precision} = \frac{TP}{TP + FP}
\]

**Cuando usarla:**  
La **precisión** es especialmente útil cuando te interesa minimizar los **falsos positivos**, es decir, cuando un error en el que el modelo predice un positivo erróneo es más costoso que predecir un negativo erróneo.

**Ejemplo:**  
En un modelo de **detección de spam**, donde te interesa saber cuántos de los correos etiquetados como spam **realmente lo son**, la **precisión** es más relevante. Un **falso positivo** (marcar un correo legítimo como spam) es más problemático que un **falso negativo** (dejar pasar un correo de spam).

---

### 🔹 **Diferencias clave:**

| Métrica        | Fórmula                                      | ¿Cuándo usarla?                                                   |
|----------------|----------------------------------------------|-------------------------------------------------------------------|
| **Accuracy**    | \(\frac{TP + TN}{TP + TN + FP + FN}\)         | Conjuntos de datos balanceados.                                   |
| **Precision**   | \(\frac{TP}{TP + FP}\)                        | Cuando los falsos positivos son costosos o problemáticos.         |

---

### **Resumen:**

- **Accuracy (Exactitud)** mide cuán bien lo hace el modelo en general, considerando todas las predicciones correctas. Es útil cuando las clases están equilibradas.
  
- **Precision (Precisión)** mide cuántos de los positivos predichos son realmente correctos. Es crucial cuando los falsos positivos son costosos o problemáticos.

---

¿Te gustaría más detalles sobre alguna de estas métricas o ejemplos de cómo calcularlas en un modelo específico? 😊