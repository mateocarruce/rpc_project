# Imagen base
FROM python:3.10-slim

# Copiar los archivos
WORKDIR /app
COPY ./server /app/server
COPY ./client /app/client

# Instala las dependencias del servidor
RUN pip install --no-cache-dir -r server/requirements.txt

# Exponer el puerto para el servidor
EXPOSE 5000

# Comando para ejecutar el servidor
CMD ["python", "server/server.py"]
