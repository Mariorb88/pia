En clasificación, estas métricas evalúan el rendimiento del modelo de diferentes maneras:  

### **1. Accuracy (Exactitud)**  
Es el porcentaje de predicciones correctas sobre el total de datos.  

\[
\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}
\]

✅ Útil cuando las clases están equilibradas.  
⚠️ Engañosa en datasets desbalanceados (por ejemplo, si el 95% de los datos pertenecen a una clase, un modelo que siempre predice esa clase tendrá 95% de accuracy, pero será inútil).  

---

### **2. Precision (Precisión o Valor Predictivo Positivo, VPP)**  
De todas las veces que el modelo predijo la clase positiva, ¿cuántas fueron correctas?  

\[
\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}
\]

✅ Útil cuando **los falsos positivos son costosos** (ej., diagnóstico de cáncer: un falso positivo puede llevar a pruebas innecesarias y estrés).  
⚠️ Un modelo con alta precisión puede tener baja recall si no detecta suficientes casos positivos.  

---

### **3. Recall (Sensibilidad o Tasa de Verdaderos Positivos, TVP)**  
De todos los casos positivos reales, ¿cuántos fueron detectados correctamente?  

\[
\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}
\]

✅ Útil cuando **los falsos negativos son costosos** (ej., detección de enfermedades: es mejor detectar todos los casos aunque algunos sean falsos positivos).  
⚠️ Un modelo con alta recall puede tener baja precisión si predice demasiados falsos positivos.  

---

### **4. F1-Score**  
Es el **balance** entre precisión y recall. Se calcula con la media armónica:

\[
\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
\]

✅ Útil cuando **hay un trade-off entre precisión y recall**.  
⚠️ No se usa si accuracy es suficiente o si hay que priorizar más una métrica que otra.  

---

### **Resumen práctico**  

| Métrica   | ¿Qué mide? | Útil cuando... |  
|-----------|-----------|---------------|  
| **Accuracy**  | Predicciones correctas en total | Las clases están balanceadas |  
| **Precision** | Qué tan confiable es la clase positiva | Los falsos positivos son costosos |  
| **Recall**    | Qué tan bien se detecta la clase positiva | Los falsos negativos son costosos |  
| **F1-Score**  | Balance entre precisión y recall | Hay que encontrar equilibrio entre ambas |  

Si trabajas con **detección de hipotiroidismo e hipertiroidismo**, probablemente te interese más **recall**, para no pasar por alto pacientes enfermos.