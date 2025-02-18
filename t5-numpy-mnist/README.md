# Tarea 5: Numpy y MNIST

## Primera parte: Configuración manual de un fork en GitHub

1. Crea un nuevo repositorio de trabajo **vacío** en [avidaldo-ia24](https://github.com/organizations/avidaldo-ia24/repositories/new):
    - `Owner` debe ser `avidaldo-ia24`.
    - El nombre debe ser `t5-numpy-mnist-nombre1-apellido1`, sustituyendo `nombre1-apellido1` por tu identificador. 
    - Ese nuevo repositorio debe ser privado.

2. Clona éste repositorio en que estamos ahora.

3. Modifícalo para que sea "upstream" en lugar de "origin":

`git remote rename origin upstream`

> "upstream" es el nombre convencional que se le da al repositorio remoto del que se ha hecho un fork.

4. Añade un nuevo remoto llamado "origin" que apunte a tu nuevo repositorio en GitHub:

`git remote add origin <URL_de_tu_remoto>`

Por ejemplo, si estás usando HTTPS:

`git remote add origin https://github.com/avidaldo-ia24/t5-numpy-mnist-nombre1-apellido1.git`

5. Ahora sube a tu `origin` el contenido de este repositorio, configurando la rama `master` para que haga `push` por defecto:

`git push -u origin master`

6. De este modo, hemos configurado un repositorio remoto llamado `upstream` que apunta al repositorio original y un repositorio remoto llamado `origin` que apunta al tuyo de trabajo en GitHub. Si hago modificaciones en el repositorio original (os avisaría si se da el caso), puedes traerte esos cambios con:

`git pull upstream master`

7. Crea un commit vacío a continuación del último mío y súbelo a tu repositorio:

```
git commit --allow-empty -m "Configuración inicial"
git push
```

7. Una vez tengas montado tu repo, **sube ese commit a la tarea del aula virtual** para que pueda ir revisando que está bien configurado. Si no os llega ningún comentario, podéis dar por hecho que está bien, la calificación solo se pondrá cuando se termine la tarea completa

## Segunda parte: Creación de un entorno con Tensorflow

Para trabajar en este proyecto, necesitarás tener instalado Tensorflow (y otras librerías listadas en [environment.yml](environment.yml)). Tensorflow no se instala en el entorno base de Anaconda, por lo que necesitarás crear un entorno nuevo o instalarlo en tu entorno base.

## Tercera parte: Ejercicios de manejo de MNIST con Numpy

1. Realiza los ejercicios propuestos en el notebook [tarea5.ipynb](tarea5.ipynb) y súbelo a tu repositorio. **Sube al menos un commit por cada ejercicio resuelto** con un mensaje que lo indique (p.ej. "Ejercicio 1 terminado"), pero puedes subir tantos commits como te sea útil según vayas avanzando, aunque tengan errores (puedes llamarlos "wip" o "error en ejercicio X").

2. Cuando termines, **sube tu último commit a la tarea del aula virtual** para que pueda revisar tu trabajo.

> [!TIP]
> El proyecto incluye ciertos tests que puedes ejecutar para comprobar si tu código funciona correctamente. Puedes ejecutarlos con `pytest` desde la terminal.
> Además, se ejecutan automáticamente en GitHub Actions cuando haces un push, por lo que puedes ver si tu código pasa los tests en la pestaña "Actions" de tu repositorio.

> [!IMPORTANT]  
> Comenta en el foro o escribe al profesor con las dificultades que encuentres. No te quedes atascado sin intentar resolverlo.


