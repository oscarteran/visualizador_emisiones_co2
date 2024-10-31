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
    st.markdown(
    """
    <div style='text-align: center;'>
        <h2>Distribución de principales zonas de medición en territorio nacional</h2>
        <p>Mapas interactivos para revisión de datos de emisiones de CO2.</p>
    </div>
    """,
    unsafe_allow_html=True
    )
    grafico_de_puntos(file='data/processed/grafico_nacional.json')
    
    
        