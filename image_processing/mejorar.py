from scipy.ndimage import gaussian_filter
import cv2
import numpy as np

def mejorarFoto(img):
    alto, ancho, canales = img.shape
    mensaje = "Se ha mejorado su calidad con éxito"

    if alto > 2000 or ancho > 2000:
        mensaje = "No se puede mejorar su foto, llegó a su mejor calidad"
        return img, mensaje

    # Separar las capas R, G, B
    R = img[:, :, 0]
    G = img[:, :, 1]
    B = img[:, :, 2]

    # Definir el factor de escala y el filtro gaussiano
    scale_factor = 2  # Factor de escala (ajusta según sea necesario)

    # Función para escalar y suavizar una capa
    def scale_and_smooth(channel):
        resized = cv2.resize(channel, (0, 0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
        smoothed = gaussian_filter(resized, sigma=1.5)
        return smoothed

    # Escalar y suavizar las capas R, G, B
    R_smoothed = scale_and_smooth(R)
    G_smoothed = scale_and_smooth(G)
    B_smoothed = scale_and_smooth(B)

    # Concatenar las capas R, G, B
    imagen_mejorada = np.stack((R_smoothed, G_smoothed, B_smoothed), axis=2)

    if imagen_mejorada.shape[2] == 1:
        raise ValueError('La imagen debe ser en color (RGB)')

    # Separar las capas R, G, B nuevamente
    R = imagen_mejorada[:, :, 0]
    G = imagen_mejorada[:, :, 1]
    B = imagen_mejorada[:, :, 2]

    # Crear el kernel de nitidez
    sharpeningKernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    # Aplicar el filtro a cada capa por separado
    R_sharpened = cv2.filter2D(R, -1, sharpeningKernel)
    G_sharpened = cv2.filter2D(G, -1, sharpeningKernel)
    B_sharpened = cv2.filter2D(B, -1, sharpeningKernel)

    # Concatenar las capas R, G, B
    imagen_mejorada = np.stack((R_sharpened, G_sharpened, B_sharpened), axis=2)

    return imagen_mejorada, mensaje