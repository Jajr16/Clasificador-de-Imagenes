# Usar una imagen base de Python
FROM python:3.8-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo requirements.txt en el contenedor
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación en el contenedor
COPY . .

# Exponer el puerto en el que la aplicación correrá
EXPOSE 8080

# Comando para correr la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
