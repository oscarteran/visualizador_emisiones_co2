import pandas as pd
from pyproj import Proj
import folium
from streamlit_folium import st_folium
import streamlit as st
import json
from .pages import *
import glob
from io import BytesIO
import os




# Función para mostrar el texto en la columna izquierda
def show_description():
    """
    Muestra una descripción general del proyecto en la aplicación, incluyendo el propósito del mapa
    y detalles sobre los puntos de recolección de datos de CO₂.

    Parámetros:
    -----------
    - No recibe parámetros de entrada.
    """
    st.subheader("Descripción del Proyecto")
    st.write("""
        Este mapa muestra los puntos de recolección de datos de CO₂ en una zona específica. 
        La cuadrícula azul indica el promedio de CO₂ en distintas áreas geográficas.
        Los valores de CO₂ se expresan en **gm-2-d-1**.
    """)
    st.write("""
        Usa el cursor para interactuar con los marcadores y ver los valores exactos.
    """)



# Función para cambiar de página
def go_to_page(page_name):
    """
    Cambia la página actual de la aplicación según el nombre de página especificado, 
    actualizando el estado de la sesión en Streamlit.

    Parámetros:
    -----------
    - page_name (str): Nombre de la página a la cual se desea navegar.
    """
    st.session_state["page"] = page_name
    
    
def encabezado():
    """
    Muestra un encabezado centrado en la aplicación con el título del catálogo 
    de emisiones de CO₂ y la información institucional de la UNAM y el Instituto de Geofísica.

    Parámetros:
    -----------
    - No recibe parámetros de entrada.
    """
    st.markdown(
    """
    <div style='text-align: center;'>
        <h1>Catálogo Nacional de Emisiones de CO2</h1>
        <h2>UNAM: Universidad Nacional Autónoma de México.</h2>
        <h3>Instituto de Geofísica. Departamento de Recursos Nacionales.</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    
def n_espacios(n: int):
    """
    Inserta una cantidad específica de espacios verticales (líneas en blanco) en la interfaz de la aplicación.

    Parámetros:
    -----------
    - n (int): Número de líneas en blanco que se desea agregar.
    """
    for _ in range(n):
        st.markdown("<br>", unsafe_allow_html=True)


def definir_pagina_actual():
    """
    Define la página actual de la aplicación y muestra los botones de navegación en la barra lateral.

    Esta función establece el título de la página y crea botones que, al ser presionados, redireccionan a diferentes secciones de la aplicación.

    Parámetros:
    -----------
    - No recibe parámetros de entrada.
    """
    titulo = "Inventario nacional de emisiones de CO"

    # Mostrar ícono como botón para cambiar de página
    st.sidebar.title(titulo)
    st.sidebar.button("Descripción del proyecto", on_click=go_to_page, args=("Inicio",))
    st.sidebar.button("Modulo 1. Datos nacionales", on_click=go_to_page, args=("Acerca de",))
    st.sidebar.button("Redirección a los mapas", on_click=go_to_page, args=("Mapas",))
    st.sidebar.button("Bibliografía", on_click=go_to_page, args=("Bibliografía",))
    
    
    
def contenido_principal():
    """
    Genera y muestra el contenido principal de una página web utilizando Streamlit.
    
    Esta función construye la estructura principal de una página web que forma parte
    de un proyecto de inventario nacional de emisiones de CO2. La función realiza
    las siguientes tareas:
    
    1. Crea un diseño de dos columnas para mostrar logos
    2. Carga y muestra los logos de la institución
    3. Inserta un encabezado personalizado
    4. Agrega texto descriptivo del proyecto con formato HTML

    Parámetros:
    -----------
    - No recibe parámetros de entrada.

    Returns:
    -----------
        None: La función modifica directamente la interfaz de Streamlit
    """
    
    # Carga de imágenes y logos
    col1, col2 = st.columns([20, 5])
    with col1:
        n_espacios(n=2)
        st.image("output/images/LogoIG.png", width=300)
    with col2:
        st.image("output/images/LogoUnam.png", width=200)

    encabezado()
    
    st.markdown(
        """
        <div style="text-align: justify;">
            <p>Este proyecto es un esfuerzo colectivo por recolectar datos y generar datos geolocalizados 
            con el fin de generar un inventario nacional de emisiones de CO2. 
            A través de la barra de navegación lateral es posible acceder a las diferentes páginas, mapas y contenido relacionado.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div style="text-align: justify;">
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    
def bibliografia():
    """
    Genera y muestra una página de recursos bibliográficos con funcionalidad de descarga de datos.

    Esta función crea una página web utilizando Streamlit que contiene información bibliográfica
    y permite la descarga de archivos CSV relacionados con diferentes ubicaciones geográficas.
    La función realiza las siguientes operaciones:

    1. Muestra un encabezado y texto descriptivo
    2. Crea y muestra una tabla de datos con información de diferentes ubicaciones
    3. Genera botones de descarga para archivos CSV asociados a cada ubicación

    Parámetros:
    -----------
    - No recibe parámetros de entrada.

    Returns:
    -----------
        None: La función modifica directamente la interfaz de Streamlit
    """
    # Titulos y encabezados
    encabezado()
    
    n_espacios(n=3)
    
    st.markdown(
        """
        <div style="text-align: justify;">
            <p> En este apartado puedes encontrar recursos bibliográficos y artículos relacionados a la toma de muestras, el proyecto en general e investigación científica relevante. </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Ejemplo de datos para la tabla
    data = {
        "Nombre": ["Acoculco", "Alcaparrosa", "Azufres", "Chichinautzin", "Escalera", "Michoa", "Puruandiro"],
        "Ubicacion": [(19.94551763857352, -98.1342090794785), (19.938287335451456, -98.1403903008043), (19.922608931287755, -98.1446972068743), (19.08627758098732, -99.1271971420124), (19.59937443895357, -101.03290674004415), (19.329928048541866, -96.30251214624522), (20.088816962773418, -101.49355905556486)],
        "Estado": ["Puebla", "Alcaparrosa", "Los Azufres", "CDMX-Morelos", "Michoacan", "Michoacan", "Michoacan"],
        "Descripción": ["", "", "", "", "", "", ""], 
        "Archivo": ["P_Acoculco.csv", "P_alcaparrosa.csv", "P_Azufres.csv", "P_Chichinautzin.csv", "P_Escalera.csv", "P_Michoa.csv", "P_Puruandiro.csv"]  # Nombres de archivos CSV
    }
    df = pd.DataFrame(data)

    # Desplegar la tabla
    st.write("Información de Usuarios")
    st.dataframe(df, use_container_width=True)

    # Ruta al directorio donde están almacenados los archivos CSV
    csv_dir = "./data/raw/"  # Ajusta esta ruta según tu estructura de archivos

    # Crear una tabla con encabezados
    st.write("Descarga de archivos con datos crudos.")
    columns_len = [1 for _ in data["Archivo"]]
    header_cols = st.columns(columns_len)

    # Crear filas con datos y botones de descarga
    for idx, file in enumerate(data["Archivo"]):

        # Ruta completa del archivo CSV
        file_path = os.path.join(csv_dir, file)

        # Leer el archivo CSV para obtener los bytes
        with open(file_path, "rb") as file:
            file_bytes = file.read()
            
        with header_cols[idx]:
            # Crear el botón de descarga en la última columna
            st.download_button(
                label=file_path[11:-4],
                data=file_bytes,
                file_name=file_path,
                mime="text/csv",
                key=f"download-btn-{idx}"  # Clave única para cada botón
            )
           
    
    

def listado_mapas():
    """
    Crea una interfaz de selección de mapas para diferentes ubicaciones geográficas.

    Esta función genera una página web utilizando Streamlit que permite al usuario
    seleccionar y navegar entre diferentes mapas de ubicaciones específicas. La función
    implementa un sistema de navegación basado en un menú desplegable.

    Estructura:
        1. Muestra un título principal
        2. Presenta un menú desplegable con ubicaciones disponibles
        3. Redirecciona al mapa seleccionado usando un sistema de navegación

    Diccionario de ubicaciones:
        El diccionario nombres_unicos contiene pares de:
        - Clave: Nombre de la ubicación (str)
        - Valor: Ruta al archivo CSV procesado (str)
        
    Ubicaciones disponibles:
        - Acoculco
        - Alcaparrosa
        - Azufres
        - Chichinautzin
        - Escalera
        - Michoa
        - Puruandiro
    
    Parámetros:
    -----------
    - No recibe parámetros de entrada.

    Returns:
    -----------
        None: La función modifica directamente la interfaz de Streamlit
    """
    # Funcion para crear las paginas con parametro de definicion
    st.title("Listado completo de mapas")
    
    # Listado de nombres específicos
    nombres_unicos = {"Acoculco": "/data/processed\\P_AcoculcoLatLon.csv", "alcaparrosa": "/data/processed\\P_alcaparrosaLatLon.csv", "Azufres": "/data/processed\\P_AzufresLatLon.csv", "Chichinautzin": "/data/processed\\P_ChichinautzinLatLon.csv", "Escalera": "/data/processed\\P_EscaleraLatLon.csv", "Michoa": "/data/processed\\P_MichoaLatLon.csv", "Puruandiro": "/data/processed\\P_PuruandiroLatLon.csv"}
    
    st.markdown("### Seleccione una ubicación para mostrar el mapa con los datos")
    
    opcion_seleccionada = st.selectbox("Busca una ubicación:", list(nombres_unicos.keys()))
    
    go_to_page(opcion_seleccionada)
    
    
            
def encabezado_mapa_individual(zona):
    """
    Genera el encabezado descriptivo para la página de un mapa individual de una zona específica.

    Esta función crea un título y una descripción estándar para las páginas que muestran
    mapas individuales de zonas de muestreo. La función proporciona contexto sobre
    la información que se visualizará en el mapa.

    Args:
        zona (str): Nombre de la zona geográfica que se está visualizando.
                   Ejemplos: "Acoculco", "Azufres", "Chichinautzin", etc.

    Returns:
        None: La función modifica directamente la interfaz de Streamlit
    """
    st.title(f"Información de zona: {zona}")
    st.text("""
            Este mapa despliega la localización de las muestras tomadas así como el valor medido.
            """)
    
    
    
def pie_de_pagina():
    """
    Genera un pie de página fijo en la parte inferior de la aplicación web.

    Esta función crea un pie de página con estilo personalizado utilizando HTML y CSS
    que se mantiene fijo en la parte inferior de la página independientemente del
    contenido y el scroll.

    Estilos CSS implementados:
        - container:
            * Display: flex
            * Dirección: columna
            * Altura mínima: 100vh (altura total de la ventana)
        
        - content:
            * Flex-grow: 1 (ocupa el espacio disponible)
        
        - footer:
            * Posición: fija
            * Ubicación: parte inferior (bottom: 0)
            * Ancho: 100%
            * Color de fondo: #444446 (gris oscuro)
            * Alineación de texto: centrado
    """
    # Pie de página fijo
    st.markdown("""
    <style>
    .container {
        display: flex;
        flex-direction: column;
        min-height: 100vh; /* Asegurar que el contenedor ocupe toda la altura de la viewport */
    }
    
    .content {
        flex-grow: 1; /* El contenido principal ocupará el espacio restante */
    }
    
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #444446;
        text-align: center;
    }
    </style>
    
    <div class="container">
        <div class="content">
            </div>
        <div class="footer">
            <p>© 2023 UNAM - Todos los derechos reservados</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
        
        

"""
-----------------------------------------------------------------------------
------------------------ FUNCIONES DEPRECADAS -------------------------------
-----------------------------------------------------------------------------
"""

# # Función para mostrar el encabezado con imágenes
# # Función para mostrar el encabezado con la imagen en la esquina superior izquierda
# def show_header(image):
#     col1, col2 = st.columns([1, 4])  # La columna de la imagen es 1/5 del ancho, la del texto es 4/5

#     with col1:
#         st.image(image, width=100)  # Imagen en la esquina superior izquierda

#     with col2:
#         st.title("Análisis de CO₂ en Puntos de Recolección")  # Texto de encabezado
#         st.markdown("---")  # Línea divisoria debajo del título

#TODO: Columna deprecada
# def columna_navegacion():
#     # Menú en la barra lateral
#     # st.sidebar.title("📚 Inventario de emisiones")
#     # st.sidebar.write("**Selecciona un módulo:**")
#     # st.sidebar.write("- Descripción del proyecto")
#     # st.sidebar.write("- Modulo 1: Datos")

    
#     # Menú en la barra lateral
#     st.sidebar.title("Inventario de emisiones")
#     section = st.sidebar.radio("Selecciona un módulo:", 
#                             ["Descripción del proyecto", 
#                              "Modulo 1: Datos Nacionales",])

#     # Contenido basado en la selección
#     if section == "Descripción del proyecto":
#         st.header("Descripción del proyecto")
#         st.write("Aquí va una descripción del curso...")
        
#     elif section == "Modulo 1: Datos Nacionales":
#         st.header("Module 1: Datos")
#         st.write("Contenido de la introducción y los prerrequisitos...")
#         show_country()