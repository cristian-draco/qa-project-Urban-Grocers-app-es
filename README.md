# Urban Grocers API Automation Testing Project 
###### `Cristian Draco`

Este proyecto contiene pruebas automatizadas para la API de Urban Grocers de Tripleten.  

Urban Grocers es una plataforma de compra de alimentos en línea con un servicio de entrega de productos. Los usuarios pueden crear cuentas de usuario, crear kits de productos, modificar, agregar y eliminarlos.

Precisamente las pruebas de este proyecto verifican estas funciones de la aplicación, así como validaciones del campo `name` y algunos endpoints adicionales.

---

## Tecnologías utilizadas

- Python 3.13
- Pytest
- Requests
- API REST

---

## Estructura del proyecto

###### qa-project-Urban-Grocers-app-es/
├── configuration.py
├── data.py
├── sender_stand_request.py
├── create_kit_name_kit_test.py
├── README.md
└── .gitignore  

---

## Descripción de archivos

### configuration.py
Contiene la URL base del servicio y las rutas de los endpoints utilizados.

### data.py
Contiene:
- Headers
- Body para crear usuario
- Body para crear kit
- Datos de prueba (positivos y negativos)

### sender_stand_request.py
Contiene funciones que envían solicitudes HTTP a la API:

- Crear usuario (POST)
- Obtener token
- Crear kit (POST)
- Obtener kits (GET)
- Buscar kit por nombre (GET)
- Solicitudes sin autorización (pruebas negativas)

### create_kit_name_kit_test.py
Contiene las pruebas automatizadas:

- Validaciones positivas del nombre
- Validaciones negativas del nombre
- Búsqueda de kit
- Pruebas sin autorización

### README.md
Contiene la información básica del proyecto.

### .gitignore
Contiene una lista de archivos y carpetas que Git debe ignorar y no subir al repositorio.

---
## Instalación

1. Enlaza tu cuenta de GitHub a TripleTen.
2. Una vez que hayas vinculado tu cuenta de TripleTen con GitHub, se creará un repositorio automáticamente. El nombre del repositorio será qa-project-Urban-Grocers-app-es.
3. Ve a GitHub y clona el nuevo repositorio en tu computadora local, siguiendo estos pasos:

    - Abre la línea de comandos en tu computadora.
    
    ` cd` `~`               # asegúrate de estar en tu directorio de inicio
    `mkdir` `projects`     # crea una carpeta llamada projects
    `cd` `projects`        # cambia el directorio a la nueva carpeta de proyectos
4. Clona el repositorio con SSH.
`git` `clone` `git@github.com:username/qa-project-Urban-Grocers-app-es.git`

💡 Asegúrate de clonar el repositorio correcto. El nombre de usuario debe ser tu propio nombre de usuario, no tripleten-com.
5. Trabaja con el proyecto de manera local.

---

## Cómo ejecutar las pruebas

Para este proyecto fue usado PyCharm como IDE.

Instalar dependencias:
`pip` `install` `pytest`  
`pip` `install` `requests`  

Ejecutar las pruebas con el comando:
`pytest`

---

## Casos de prueba cubiertos

### POST /api/v1/kits

Validaciones del campo `name`:

- 1 carácter permitido  
- 511 caracteres permitidos  
- Cadena vacía  
- Más de 511 caracteres  
- Caracteres especiales  
- Espacios  
- Números  
- Parámetro faltante  
- Tipo de dato incorrecto  

### GET /api/v1/kits

- Obtener kits sin autorización  

### GET /api/v1/kits/search

- Búsqueda de kit por nombre  

---

## Bugs encontrados en la API

Durante la ejecución de las pruebas se detectaron los siguientes problemas:

1. La API permite crear un kit con nombre vacío  
2. La API permite nombres mayores a 511 caracteres  
3. La API acepta valores numéricos como nombre  
4. La API devuelve error 500 cuando falta el campo `name` (debería ser 400)  
5. Validaciones del backend incompletas  

Estos fallos indican problemas en las validaciones del servidor.

---

## Resultado esperado

Al ejecutar `pytest`:

- Algunas pruebas pasan correctamente  
- Algunas pruebas fallan debido a bugs del backend  
- Esto es comportamiento esperado del proyecto  

---

## Fuente de documentación

Documentación:

Se utilizó apiDoc para el siguiente link:
https://cnt-0aac2295-6919-433b-9292-1bcdd8a51d91.containerhub.tripleten-services.com/docs/

---

## Documentación de referencia

Se utilizó la documentación oficial para este proyecto desde la API disponible en la URL:
https://cnt-0aac2295-6919-433b-9292-1bcdd8a51d91.containerhub.tripleten-services.com de Tripleten.
