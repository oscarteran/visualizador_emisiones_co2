import pandas as pd
from pyproj import Proj
import folium
from streamlit_folium import st_folium
import streamlit as st
import json
from .pages import *
import glob
from io import BytesIO


# Función para mostrar el encabezado con imágenes
# Función para mostrar el encabezado con la imagen en la esquina superior izquierda
def show_header(image):
    col1, col2 = st.columns([1, 4])  # La columna de la imagen es 1/5 del ancho, la del texto es 4/5

    with col1:
        st.image(image, width=100)  # Imagen en la esquina superior izquierda

    with col2:
        st.title("Análisis de CO₂ en Puntos de Recolección")  # Texto de encabezado
        st.markdown("---")  # Línea divisoria debajo del título

# Función para mostrar el texto en la columna izquierda
def show_description():
    st.subheader("Descripción del Proyecto")
    st.write("""
        Este mapa muestra los puntos de recolección de datos de CO₂ en una zona específica. 
        La cuadrícula azul indica el promedio de CO₂ en distintas áreas geográficas.
        Los valores de CO₂ se expresan en **gm-2-d-1**.
    """)
    st.write("""
        Usa el cursor para interactuar con los marcadores y ver los valores exactos.
    """)

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

# Función para cambiar de página
def go_to_page(page_name):
    st.session_state["page"] = page_name
    
    
def encabezado():
    st.markdown(
    """
    <div style='text-align: center;'>
        <h1>Catálogo nacional de emisiones de CO2</h1>
        <h2>UNAM: Universidad Nacional Autónoma de México.</h2>
        <h3>Instituto de Geofísica. Departamento de Recursos Nacionales.</h3>
    </div>
    """,
    unsafe_allow_html=True
    )
    
def n_espacios(n: int):
    for _ in range(n):
        st.markdown("<br>", unsafe_allow_html=True)


def definir_pagina_actual():
    titulo = "Inventario nacional de emisiones de CO"

    # Mostrar ícono como botón para cambiar de página
    st.sidebar.title(titulo)
    st.sidebar.button("Descripción del proyecto", on_click=go_to_page, args=("Inicio",))
    st.sidebar.button("Modulo 1. Datos nacionales", on_click=go_to_page, args=("Acerca de",))
    st.sidebar.button("Redirección a los mapas", on_click=go_to_page, args=("Mapas",))
    st.sidebar.button("Bibliografía", on_click=go_to_page, args=("Bibliografía",))
    
    
    
def contenido_principal():
    
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
    
    
def bibliografía():
    # Titulos y encabezados
    encabezado()
    
    n_espacios(n=5)
    
    st.markdown(
        """
        <div style="text-align: justify;">
            <p> En este apartado puedes encontrar recursos bibliográficos y artículos relacionados a la toma de muestras, el proyecto en general e investigación científica relevante. </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    
    # Datos de ejemplo
    data = {
        "Nombre del Archivo": ["archivo1.csv", "archivo2.csv", "archivo3.csv"],
        "Descripción": ["Datos de ventas", "Datos de clientes", "Datos de inventario"]
    }

    # Crear DataFrame
    df = pd.DataFrame(data)

    # Función para generar un archivo de muestra
    def generar_archivo(nombre_archivo):
        output = BytesIO()
        df_sample = pd.DataFrame({"Columna A": [1, 2, 3], "Columna B": [4, 5, 6]})
        df_sample.to_csv(output, index=False)
        output.seek(0)
        return output

    # HTML para tabla con bordes
    table_html = """
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
    <table>
        <tr>
            <th>Nombre del Archivo</th>
            <th>Descripción</th>
            <th>Descargar</th>
        </tr>
    """

    # Generar filas de la tabla con botones de descarga
    for i, row in df.iterrows():
        download_button = st.download_button(
            label="Descargar",
            data=generar_archivo(row["Nombre del Archivo"]),
            file_name=row["Nombre del Archivo"],
            mime="text/csv",
            key=i  # Clave única para cada botón
        )
        # Agregar la fila en HTML (el botón de descarga se agrega desde Streamlit)
        table_html += f"""
        <tr>
            <td>{row['Nombre del Archivo']}</td>
            <td>{row['Descripción']}</td>
            <td>{download_button}</td>
        </tr>
        """

    table_html += "</table>"

    # Mostrar la tabla con bordes en Streamlit
    st.markdown(table_html, unsafe_allow_html=True)
    
    
    

def listado_mapas():
    # Funcion para crear las paginas con parametro de definicion
    st.title("Listado completo de mapas")
    
    # Listado de nombres específicos
    nombres_unicos = {"Acoculco": "/data/processed\\P_AcoculcoLatLon.csv", "alcaparrosa": "/data/processed\\P_alcaparrosaLatLon.csv", "Azufres": "/data/processed\\P_AzufresLatLon.csv", "Chichinautzin": "/data/processed\\P_ChichinautzinLatLon.csv", "Escalera": "/data/processed\\P_EscaleraLatLon.csv", "Michoa": "/data/processed\\P_MichoaLatLon.csv", "Puruandiro": "/data/processed\\P_PuruandiroLatLon.csv"}
    
    st.markdown("### Seleccione una ubicación para mostrar el mapa con los datos")
    
    opcion_seleccionada = st.selectbox("Busca una ubicación:", list(nombres_unicos.keys()))
    
    go_to_page(opcion_seleccionada)
    
    
            
def encabezado_mapa_individual(zona):
    st.title(f"Información de zona: {zona}")
    st.text("""
            Este mapa despliega la localización de las muestras tomadas así como el valor medido.
            """)
    
    
    
def pie_de_pagina():
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
        
        