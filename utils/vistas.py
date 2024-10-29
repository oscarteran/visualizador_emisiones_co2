import pandas as pd
from pyproj import Proj
import folium
from streamlit_folium import st_folium
import streamlit as st
import json
from .pages import *
import glob


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



def definir_pagina_actual():
    titulo = "Inventario nacional de emisiones de CO"

    # Mostrar ícono como botón para cambiar de página
    st.sidebar.title(titulo)
    st.sidebar.button("Descripción del proyecto", on_click=go_to_page, args=("Inicio",))
    st.sidebar.button("Modulo 1. Datos nacionales", on_click=go_to_page, args=("Acerca de",))
    st.sidebar.button("Redirección a los mapas", on_click=go_to_page, args=("Mapas",))
    
    
    
def contenido_principal():
    st.title("Catálogo nacional de emisiones de CO2")
    st.header("UNAM: Universidad Nacional Autónoma de México.")
    st.subheader("Instituto de Geofísica. Departamento de Recursos Nacionales.")
    st.text("""
            Descripción completa del proyecto
            """)
    
    

def listado_mapas():
    # Leer todos los csv convertidos en latitud y longitud
    # Especificar el directorio y tipo de archivo
    csv_archivos = glob.glob("data\processed\*.csv")
    
    # Crear diccionario con nombre/df de datos
    # Leer cada ruta de archivo y convertirlo a un DafaFrame
    dataframes = [pd.read_csv(file) for file in csv_archivos]
    
    # Unir en un diccionario ambas listas de elementos
    mapas_completos = dict(zip(csv_archivos, dataframes))
    
    # Funcion para crear las paginas con parametro de definicion
    st.title("Listado completo de mapas")
    
    st.markdown("### Seleccione un Mapa")
    for nombre, datos in mapas_completos.items():
        with st.container():
            st.button(nombre[17:-10],  on_click=go_to_page, args=(str(nombre[17:-10]),))
            
def encabezado_mapa_individual(zona):
    st.title(f"Información de zona: {zona}")
    st.text("""
            Este mapa despliega la localización de las muestras tomadas así como el valor medido.
            """)
        
        