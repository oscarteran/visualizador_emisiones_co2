import streamlit as st
from .mapas import *

# Función para la vista de "Descripción del proyecto"
def mostrar_descripcion_proyecto():
    st.header("Descripción del proyecto")
    st.write("Aquí va una descripción detallada del proyecto de inventario de emisiones...")


# # Función para la vista de "Modulo 1: Datos Nacionales"
# def mostrar_datos_nacionales():
#     st.header("Módulo 1: Datos Nacionales")
#     st.write("Aquí se muestran los datos nacionales de emisiones de CO2...")
#     # Aquí puedes agregar gráficos, mapas, tablas, etc.

def mostrar_datos_nacionales():
    # Crear un header
    st.header("Visualización de CO2 - Mapa Interactivo")
    st.markdown("""
    Mapas interactivos para revisión de datos de emisiones de CO2.  
    """)
    grafico_de_puntos(file='data/processed/grafico_nacional.json')
    
    
        