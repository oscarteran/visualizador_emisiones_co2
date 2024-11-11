
# CO2 Emissions Viewer
This repository contains the code to deploy a web app focused on disseminating information where scientific data and articles related to CO2 emissions across Mexico can be consulted.

This work has been developed as part of the activities carried out in the Social Service program **Data Science and Information Visualization for Research and Teaching**.

## Running in Local Environment
The application is designed to run through the Python interpreter or using Docker.

### Clone the Repository
To run the application, the first step is to clone the repository to your computer:
```bash
git clone https://github.com/oscarteran/visualizador_emisiones_co2
```

Change directory:
```bash
cd visualizador_emisiones_co2
```

### Python
For proper functionality, it is necessary to create a virtual environment with the required libraries.

#### Windows

1. Open the terminal (CMD or PowerShell) and navigate to the project folder:

Create a virtual environment:
```bash
python -m venv venv
```
Activate the virtual environment:
```bash
.env\Scriptsctivate
```
Install the dependencies:
```bash
pip install -r requirements.txt
```
#### macOS and Linux

Open the terminal and navigate to the project folder:

```bash
cd path/to/project
```
Create a virtual environment:

```bash
python3 -m venv venv
```
Activate the virtual environment:

```bash
source venv/bin/activate
```
Install the dependencies:

```bash
pip install -r requirements.txt
```

##### Deactivate the Virtual Environment
When you finish working, you can deactivate the virtual environment:

On any operating system:

```bash
deactivate
```
Important Notes

- Make sure you have Python installed on your system
- The `requirements.txt` file should be in the root of the project
- The virtual environment (venv) is by default in the .gitignore
- It is recommended to activate the virtual environment each time you work on the project


#### Execution
Once the virtual environment with its libraries is installed, navigate to the root of the repository and run:
```bash
streamlit run app.py
```
By default, the application will open on a free port of `localhost`.

### Docker
Running on Docker only requires installing this tool. [See Docker Install](https://docs.docker.com/engine/install/).

In the root of the repository, execute in the following order:
Build the Docker image:

```bash
docker build -t app-name .
```

The period (.) at the end indicates that the Dockerfile is in the current directory


Verify that the image was created successfully:

```bash
docker images
```

You should see 'app-name' in the list of images


Run the container:

```bash
docker run -p 8501:8501 app-name
```

The -p flag maps port 8501 of the container to port 8501 of your local machine.


#### Access the Application:

Open your browser
Visit http://localhost:8501

#### Useful Commands

Stop the container
```bash
docker ps                         # View running containers
docker stop <container_id>        # Stop a specific container
```
Remove containers and images
```bash
docker rm <container_id>          # Remove a container
docker rmi app-name               # Remove the image
```

View logs
```bash
docker logs <container_id>        # View container logs
```

#### Troubleshooting

If port 8501 is in use, you can use another port:

```bash
docker run -p 8502:8501 app-name
```
To run the container in the background:

```bash
docker run -d -p 8501:8501 app-name
```
If you need to access the container:

```bash
docker exec -it <container_id> /bin/bash
```
Notes

- The container will run until you stop it manually.
- Changes made inside the container do not persist after stopping it.
- Make sure the necessary ports are available on your machine.

## Contributions


### Important Links for Reference

[Folium Documentation](https://python-visualization.github.io/folium/latest/getting_started.html)

[Map Views](https://leaflet-extras.github.io/leaflet-providers/preview/)

[Views Repository](https://github.com/leaflet-extras/leaflet-providers)


### Developer and Contact
**Oscar Hernández Terán**                          
- oscarhdzteran@gmail.com
- [LinkedIn](https://www.linkedin.com/in/oscarhernandezteran/)