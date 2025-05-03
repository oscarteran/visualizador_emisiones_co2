# Usa una imagen base de Python
FROM python:3.10

# Configura el directorio de trabajo dentro del contenedor
WORKDIR /visualizador

# Copia los archivos de la aplicación al contenedor
COPY . /visualizador

# Actualización de pip en contenedor
RUN pip install --upgrade pip

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto que utiliza Streamlit (8501 por defecto)
EXPOSE 8080

# Define el comando para iniciar la aplicación
CMD ["streamlit", "run", "app.py"]
