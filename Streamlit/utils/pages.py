import streamlit as st
from .mapas import *

def mostrar_datos_nacionales():
    """
    Muestra una sección de encabezado con información sobre datos nacionales y un mapa interactivo.

    La función presenta una breve descripción centrada en la página acerca de la distribución 
    de las principales zonas de medición de CO₂ en el territorio nacional y luego invoca la 
    función `grafico_de_puntos` para mostrar un mapa interactivo de dichas zonas.

    Descripción de la función:
    --------------------------
    1. Utiliza Streamlit para mostrar un encabezado HTML con título y descripción sobre el propósito 
       del mapa interactivo.
    2. Llama a la función `grafico_de_puntos` con un archivo JSON que contiene las ubicaciones de 
       interés a nivel nacional para visualizar la distribución de puntos de medición.

    Parámetros:
    -----------
    - No recibe parámetros de entrada.

    Archivos requeridos:
    --------------------
    - `grafico_nacional.json`: Archivo JSON ubicado en `data/processed/` que contiene las ubicaciones 
      de medición de CO₂ en territorio nacional. Este archivo es pasado a la función `grafico_de_puntos` 
      para su visualización en el mapa.

    Bibliotecas utilizadas:
    ------------------------
    - streamlit as st: Para mostrar texto y elementos de HTML en la interfaz de usuario.
    - grafico_de_puntos: Función llamada para renderizar un mapa interactivo con los puntos de medición.

    Ejemplo de uso:
    ---------------
    >>> mostrar_datos_nacionales()
    """
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
    
    
        