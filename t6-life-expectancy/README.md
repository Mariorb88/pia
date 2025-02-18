# Tarea 6: Predicción de esperanza de vida

## Primera parte: Configuración manual de un fork en GitHub

1. Clona este repositorio con "upstream" como nombre del remoto:

    - Si usas HTTPS: `git clone --origin upstream https://github.com/avidaldo-ia24/t6-life-expectancy.git`
    - Si usas SSH: `git clone --origin upstream git@github.com:avidaldo-ia24/t6-life-expectancy.git`

> "upstream" es el nombre convencional que se le da al repositorio remoto del que se ha hecho un fork.

2. Crea un nuevo repositorio de trabajo **vacío** en [avidaldo-ia24](https://github.com/organizations/avidaldo-ia24/repositories/new):
    - `Owner` debe ser `avidaldo-ia24`.
    - El nombre debe ser `t6-life-expectancy-nombre1-apellido1`, sustituyendo `nombre1-apellido1` por tu identificador. 
    - Ese nuevo repositorio debe ser privado.

3. Añade tu nuevo repositorio de trabajo como remoto "origin" a tu repositorio local:

`git remote add origin <URL_de_tu_remoto>`

4. Ahora sube a tu `origin` el contenido de este repositorio, configurando la rama `master` para que haga `push` por defecto:

`git push -u origin master`

5. De este modo, hemos configurado un remoto llamado `upstream` que apunta al repositorio original y un remoto llamado `origin` que apunta al tuyo de trabajo en GitHub. Si hago modificaciones en el repositorio original, puedes traerte esos cambios con:

`git pull upstream master`

6. Crea un commit vacío a continuación del último mío y súbelo a tu repositorio:

```
git commit --allow-empty -m "Configuración inicial"
git push
```

7. Una vez tengas montado tu repo, **sube ese commit a la tarea del aula virtual** para que pueda ir revisando que está bien configurado. Si no te escribo, será que está correcto, la calificación solo se pondrá cuando se termine la tarea completa


## Segunda parte: Notebook creando y evaluando un modelo de predicción de esperanza de vida

1. Crea un notebook de Jupyter con el nombre "tarea6.ipynb" y realiza en el los siguientes pasos.

2. Realiza un análisis exploratorio de los datos del dataset "data/life_expectancy.csv".

3. Trata los valores no disponibles con [las estrategias explicadas en los apuntes](https://github.com/avidaldo/ia24/blob/main/end2end/e2e041_missing.ipynb) justificando la elección de cada una de ellas.

4. Compara al menos dos modelos para predicción de la esperanza de vida y evalúa su rendimiento.

5. Crea un pipeline de scikit-learn que incluya el preprocesamiento de los datos y el modelo de predicción elegido.


