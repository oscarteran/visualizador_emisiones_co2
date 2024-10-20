import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
from pyproj import Proj, transform
import os
from utils import *



# Función principal para organizar la aplicación
def main():
    
    # Menú en la barra lateral
    st.sidebar.title("📚 DE Zoomcamp")
    section = st.sidebar.radio("Selecciona un módulo:", 
                            ["Descripción del proyecto", 
                             "Modulo 1: Datos",])

    # Contenido basado en la selección
    if section == "Descripción del proyecto":
        st.header("Descripción del proyecto")
        st.write("Aquí va una descripción del curso...")
    elif section == "Module 1: Datos":
        st.header("Module 1: Datos")
        st.write("Contenido de la introducción y los prerrequisitos...")
    
    
    # Título y descripción de la aplicación
    st.title("Mapa Interactivo de emisiones de CO2.")
    st.markdown("""
    # Visualización de CO2
    Mapas interactivos para revisión de datos de emisiones de CO2.  
    """)

    # Mostrar encabezado con imágenes
    # show_header(image="output/LogoUnam.png")

    # # Crear dos columnas (izquierda para descripción y derecha para mapas)
    # col1, col2 = st.columns([1, 2])  # La columna izquierda será 1/3, la derecha 2/3

    # # Columna izquierda: descripción del proyecto
    # with col1:
    #     show_description()

    # Columna derecha: mapa interactivo
    #with col2:
    # Despliegue de mapa
    st.markdown("""
    ### Visualización de datos de La Escalera
    """)
    grafico_de_puntos(file='data/processed/grafico_nacional.json')
    #plot_map(file='data/raw/P_Escalera.csv')

    # Despliegue de mapa
    # st.markdown("""
    # ### Visualización de datos de Los Azufres
    # """)
    # plot_map(file='data/raw/P_Azufres.csv')
    
        
if __name__ == "__main__":
    main()