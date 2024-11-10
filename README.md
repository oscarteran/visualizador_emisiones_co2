# Visualizador de emisiones de CO2
Este repositorio contiene el codigo para desplegar una web app de divulagación en la que se puede consultar datos y artículos científicos relacionados a la toma de datos de emisiones de CO2 a lo larga de la República Mexicana.

Este trabajo se ha desarrollado como parte de las actividades realizadas en el programa de Servicio Social 
**Ciencia de datos y visualización de la información para investigación y docencia**.

## Ejecución en ambiente local
La aplicacion esta diseñada para ejecutarse a través del intérprete de Python, o bien, haciendo uso de Docker.

### Clonar el repositorio
Para poder ejecutar la aplicación, el primer paso es clonar el repositorio en tu equipo:
```bash
git clone https://github.com/oscarteran/visualizador_emisiones_co2
```

Cambiar de directorio:
```bash
cd visualizador_emisiones_co2
```

### Python
Para el correcto funcionamiento es necesario crear un ambiente virtual con las librerias requeridas.

#### Windows

1. Abre la terminal (CMD o PowerShell) y navega hasta la carpeta del proyecto:

Crea un ambiente virtual:
```bash
python -m venv venv
```
Activa el ambiente virtual:
```bash
.\venv\Scripts\activate
```
Instala las dependencias:
```bash
pip install -r requirements.txt
```
#### macOS y Linux

Abre la terminal y navega hasta la carpeta del proyecto:

```bash
cd ruta/del/proyecto
```
Crea un ambiente virtual:

```bash
python3 -m venv venv
```
Activa el ambiente virtual:

```bash
source venv/bin/activate
```
Instala las dependencias:

```bash
pip install -r requirements.txt
```

##### Desactivar el Ambiente Virtual
Cuando hayas terminado de trabajar, puedes desactivar el ambiente virtual:

En cualquier sistema operativo:

```bash
deactivate
```
Notas Importantes

- Asegúrate de tener Python instalado en tu sistema
- El archivo `requirements.txt` debe estar en la raíz del proyecto
- El ambiente virtual (venv) se encuentra en el .gitignore por defecto
- Se recomienda activar el ambiente virtual cada vez que se trabaje en el proyecto


#### Ejecución
Una vez instalado el ambiente virtual con sus librerias, se debe posicionar sobre la raiz del repositorio y ejecutar:
```bash
streamlit run app.py
```
Por defecto la aplicacion abrirá un puerto libre del `localhost`.

### Docker
La ejecución en Docker requiere únicamente la instalación de esta herramienta. [Véase Docker Install](https://docs.docker.com/engine/install/).

En la raiz del repositorio, ejecutar en el siguiente orden:
Construye la imagen de Docker:

```bash
docker build -t nombre-app .
```

El punto (.) al final indica que el Dockerfile está en el directorio actual


Verifica que la imagen se creó correctamente:

```bash
docker images
```

Deberías ver 'nombre-app' en la lista de imágenes


Ejecuta el contenedor:

```bash
docker run -p 8501:8501 nombre-app
```

El flag -p mapea el puerto 8501 del contenedor al puerto 8501 de tu máquina local.


#### Accede a la aplicación:

Abre tu navegador
Visita http://localhost:8501

#### Comandos Útiles

Detener el contenedor
```bash
docker ps                         # Ver contenedores en ejecución
docker stop <container_id>        # Detener un contenedor específico
```
Eliminar contenedores e imágenes
```bash
docker rm <container_id>          # Eliminar un contenedor
docker rmi nombre-app 
           # Eliminar la imagen
```

Ver logs
```bash
docker logs <container_id>        # Ver logs del contenedor
```

#### Solución de Problemas

Si el puerto 8501 está ocupado, puedes usar otro puerto:

```bash
docker run -p 8502:8501 nombre-app
```
Para ejecutar el contenedor en segundo plano:

```bash
docker run -d -p 8501:8501 nombre-app
```
Si necesitas acceder al contenedor:

```bash
docker exec -it <container_id> /bin/bash
```
Notas

- El contenedor se ejecutará hasta que lo detengas manualmente.
- Los cambios realizados dentro del contenedor no persisten después de detenerlo.
- Asegúrate de que los puertos necesarios estén disponibles en tu máquina.

## Contribuciones


### Enlaces importantes para consultas

[Documetación de Folium](https://python-visualization.github.io/folium/latest/getting_started.html)

[Vistas de mapas](https://leaflet-extras.github.io/leaflet-providers/preview/)

[Repositorio de vistas](https://github.com/leaflet-extras/leaflet-providers)


### Desarrollador y contacto
**Oscar Hernández Terán**                          
- oscarhdzteran@gmail.com
- [LinkedIn](https://www.linkedin.com/in/oscarhernandezteran/) 