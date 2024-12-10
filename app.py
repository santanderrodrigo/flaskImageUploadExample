from flask import Flask, request, render_template, redirect, url_for
import os

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Configurar la carpeta de subida de archivos
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Crear la carpeta de subida si no existe
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Ruta para la página principal que muestra el formulario de subida
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar la subida de archivos
@app.route('/upload', methods=['POST'])
def upload_file():
    # Verificar si el archivo está en la solicitud
    if 'image' not in request.files:
        return 'No file part'
    
    file = request.files['image']
    
    # Verificar si se seleccionó un archivo
    if file.filename == '':
        return 'No selected file'
    
    # Guardar el archivo si es válido
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return redirect(url_for('show_images'))

# Ruta para mostrar las imágenes subidas
@app.route('/images')
def show_images():
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('images.html', images=images)

# Ejecutar la aplicación en modo de depuración
if __name__ == '__main__':
    app.run(debug=True)