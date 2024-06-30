from flask import Flask, request, jsonify, send_file, render_template
from skimage import img_as_ubyte
import io
import cv2
import numpy as np
from image_processing.mejorar import mejorarFoto

app = Flask(__name__)

@app.route('/mejorar', methods=['POST'])
def mejorar():
    print("Solicitud recibida")
    file = request.files['image']
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400
    
    print("Archivo recibido:", file.filename)
    in_memory_file = io.BytesIO()
    file.save(in_memory_file)
    in_memory_file.seek(0)

    img = cv2.imdecode(np.frombuffer(in_memory_file.read(), np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        return jsonify({'error': 'Invalid image file'}), 400

    img_enhanced, mensaje = mejorarFoto(img)
    _, img_encoded = cv2.imencode('.jpg', img_as_ubyte(img_enhanced))
    img_io = io.BytesIO(img_encoded)

    print("Imagen mejorada con éxito")
    return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name='imagen_mejorada.jpg')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    import os
    
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)