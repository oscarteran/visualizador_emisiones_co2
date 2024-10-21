import pandas as pd
from pyproj import Proj
import folium
from streamlit_folium import st_folium
import streamlit as st
import json
from .pages import *


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


def columna_navegacion():
    # Menú en la barra lateral
    # st.sidebar.title("📚 Inventario de emisiones")
    # st.sidebar.write("**Selecciona un módulo:**")
    # st.sidebar.write("- Descripción del proyecto")
    # st.sidebar.write("- Modulo 1: Datos")

    
    # Menú en la barra lateral
    st.sidebar.title("Inventario de emisiones")
    section = st.sidebar.radio("Selecciona un módulo:", 
                            ["Descripción del proyecto", 
                             "Modulo 1: Datos Nacionales",])

    # Contenido basado en la selección
    if section == "Descripción del proyecto":
        st.header("Descripción del proyecto")
        st.write("Aquí va una descripción del curso...")
        
    elif section == "Modulo 1: Datos Nacionales":
        st.header("Module 1: Datos")
        st.write("Contenido de la introducción y los prerrequisitos...")
        show_country()
        