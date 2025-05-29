# Resumen: Adquisición de Datos en Big Data

## 🔹 Introducción

La adquisición de datos es la primera fase del proceso **ETL** (Extracción, Transformación, Carga) en Big Data. En clase se han abordado tres herramientas clave:

* **APIs a través de CKAN**
* **Web scraping con BeautifulSoup**
* **Automatización con Selenium**

---

## 📁 1. CKAN y uso de APIs públicas

**CKAN** es una plataforma para la gestión y publicación de datos abiertos.

### Características:

* Muchas administraciones públicas (como el Concello de Vigo) usan CKAN.
* Permite acceder a datasets en tiempo real (ej. ocupación de parkings, tráfico, clima).
* Los datos suelen estar en formatos como JSON, CSV, Excel, etc.

### Proceso:

1. **Buscar el dataset** en el catálogo de CKAN.
2. **Extraer el ID o URL** del recurso.
3. **Realizar una petición HTTP** con `requests` en Python.
4. **Procesar la respuesta** (generalmente JSON).

### Ventajas:

* Acceso directo a datos estructurados.
* Ideal para automatizar la recogida de información.

---

## 🔍 2. Web Scraping con BeautifulSoup

**BeautifulSoup** es una librería de Python para extraer información de páginas HTML.

### Funcionamiento:

* Permite navegar el DOM de una página web.
* Se pueden localizar etiquetas HTML por:

  * Nombre de etiqueta (`<span>`, `<div>`, etc.).
  * Atributos como `class`, `id` o estilos CSS.

### Herramientas:

* `find()` para obtener una única etiqueta.
* `find_all()` para obtener una lista de etiquetas.

### Proceso:

1. Obtener la página con `requests.get()`.
2. Analizar el HTML con BeautifulSoup.
3. Identificar el dato a extraer mediante inspección de elementos.
4. Acceder al contenido de la etiqueta deseada.

### Limitaciones:

* No funciona con páginas cargadas dinámicamente con JavaScript.

---

## 🚀 3. Selenium para automatización de navegación

**Selenium** es una herramienta para simular la interacción humana con páginas web.

### Características:

* Abre un navegador real o virtual (Chrome, Firefox, Edge...).
* Permite simular clicks, inputs, envío de formularios, etc.
* Útil para páginas con autenticación, formularios o JavaScript complejo.

### Proceso:

1. Inicializar un navegador con WebDriver.
2. Navegar a la URL deseada.
3. Localizar elementos con `find_element()`.
4. Realizar acciones como `.click()`, `.send_keys()`, `.submit()`.

### Complemento con BeautifulSoup:

* Una vez la página está cargada y el contenido generado por JavaScript, se puede extraer el HTML con Selenium y luego analizarlo con BeautifulSoup.

### Ejemplo de uso:

* Loguearse en un aula virtual y descargar contenidos protegidos por sesión.
* Navegar en un formulario de selección múltiple y extraer la información seleccionada.

---

## 🔮 Conclusión

* **CKAN** es ideal para acceder a datos públicos bien estructurados.
* **BeautifulSoup** permite capturar datos de páginas HTML estáticas.
* **Selenium** permite acceder a páginas dinámicas y con autenticación.

Estas herramientas forman la base para la **extracción automatizada de datos**, esencial para cualquier sistema Big Data moderno.
