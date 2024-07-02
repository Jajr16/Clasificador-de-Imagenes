import os
from flask import Flask, request, jsonify, send_file, render_template, make_response, redirect, url_for
from skimage import img_as_ubyte
import io
import cv2
from datetime import datetime
from uuid import uuid4
import numpy as np
from image_processing.mejorar import mejorarFoto

app = Flask(__name__)

UPLOAD_FOLDER = 'static/enhanced_images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_create_sessionid():
    session = request.cookies.get('session_id')
    if not session:
        session = str(uuid4())
        response = make_response(render_template('index.html'))
        expires = datetime(9999, 12, 31)
        response.set_cookie('session_id', session, expires=expires)
        return session, response
    return session, None

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
    print(request)

    img = cv2.imdecode(np.frombuffer(in_memory_file.read(), np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        return jsonify({'error': 'Invalid image file'}), 400

    img_enhanced, mensaje = mejorarFoto(img)
    _, img_encoded = cv2.imencode('.jpg', img_as_ubyte(img_enhanced))
    
    # Guardar la imagen mejorada en el directorio UPLOAD_FOLDER
    enhanced_image_filename = f"{uuid4()}.jpg"
    enhanced_image_path = os.path.join(UPLOAD_FOLDER, enhanced_image_filename)
    with open(enhanced_image_path, 'wb') as f:
        f.write(img_encoded)

    # Obtener la URL de la imagen mejorada
    enhanced_image_url = url_for('static', filename=f"enhanced_images/{enhanced_image_filename}")

    session = request.cookies.get('session_id')
    if not session:
        return redirect(url_for('index'))

    enhanced_img_urls = request.cookies.get(session, '').split(',')
    enhanced_img_urls.append(enhanced_image_url)

    response = make_response(send_file(io.BytesIO(img_encoded), mimetype='image/jpeg', as_attachment=True, download_name='imagen_mejorada.jpg'))
    expires = datetime(9999, 12, 31)
    response.set_cookie(session, ','.join(enhanced_img_urls), expires=expires)

    return response

@app.route('/')
def index():
    session, response = get_create_sessionid()
    if response:
        return response
    return render_template('index.html')

@app.route('/my_images')
def images():
    session = request.cookies.get('session_id')
    if not session:
        return redirect(url_for('index'))
    enhanced_img_urls = request.cookies.get(session, '').split(',')
    return render_template('my_images.html', enhanced_image_urls=enhanced_img_urls)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
