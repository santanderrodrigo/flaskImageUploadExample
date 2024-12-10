# Flask Image Upload

Esta es una aplicación simple de Flask que permite a los usuarios subir imágenes a través de una interfaz web y luego ver todas las imágenes subidas.

## Estructura del Proyecto

```plaintext
.
├── app.py
├── templates
│   ├── index.html
│   └── images.html
└── static
    └── uploads
```

- `app.py`: El archivo principal de la aplicación Flask.
- `templates/index.html`: El archivo HTML para el formulario de subida.
- `templates/images.html`: El archivo HTML para mostrar las imágenes subidas.
- `static/uploads`: El directorio donde se almacenan las imágenes subidas.

## Configuración

1. Clona el repositorio:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Crea un entorno virtual y actívalo:
    ```sh
    python -m venv venv
    venv\Scripts\activate
    ```

3. Instala los paquetes necesarios:
    ```sh
    pip install flask
    ```

## Ejecución de la Aplicación

1. Asegúrate de estar en el directorio del proyecto y de que el entorno virtual esté activado.
2. Ejecuta la aplicación Flask:
    ```sh
    python app.py
    ```
3. Abre tu navegador web y navega a `http://127.0.0.1:5000/` para acceder al formulario de subida.

## Uso

1. Abre la aplicación en tu navegador web.
2. Usa el formulario para seleccionar un archivo de imagen desde tu computadora.
3. Haz clic en el botón "Upload" para subir la imagen.
4. Serás redirigido a una página que muestra todas las imágenes subidas.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT.
