# 1. Imagen base con Python
FROM python:3.10-slim

# 2. Setea el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copia los archivos de tu proyecto al contenedor
COPY . /app

# 4. Instala las dependencias (asegúrate de tener requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expone el puerto por donde corre Django
EXPOSE 8000

# 6. Comando por defecto para correr el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
