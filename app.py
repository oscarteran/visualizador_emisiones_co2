import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
from pyproj import Proj, transform
import os
#from utils.capas import *
from utils.vistas import *
from utils.mapas import *
from utils.links_2_maps import *
from pathlib import Path



# Función principal para organizar la aplicación
def main():
    st.set_page_config(layout="wide")
    # Creación de columna de navegación
    #columna_navegacion()    

    
    #mostrar_pagina(pagina=pagina)
    # Inicializar la variable de sesión para la página actual
    if "page" not in st.session_state:
        st.session_state["page"] = "Inicio"

    # Invocar funcion para definir vista actual:
    definir_pagina_actual()
    
    ruta_nombres = Path("data/processed/nombres_unicos.json")
    
    #ruta_test_server = "data\processed\\nombres_unicos.json"
    
    # Leer lista completa de ubicaciones
    with open(ruta_nombres, "r") as archivo:
        nombres_unicos = json.load(archivo)
        
    # nombres_unicos = {"Acoculco": "/data/processed\\P_AcoculcoLatLon.csv", "alcaparrosa": "/data/processed\\P_alcaparrosaLatLon.csv", "Azufres": "/data/processed\\P_AzufresLatLon.csv", "Chichinautzin": "/data/processed\\P_ChichinautzinLatLon.csv", "Escalera": "/data/processed\\P_EscaleraLatLon.csv", "Michoa": "/data/processed\\P_MichoaLatLon.csv", "Puruandiro": "/data/processed\\P_PuruandiroLatLon.csv"}
        
    # st.markdown("""
    # <style>
    # .container {
    #     max-width: 90%;
    #     margin: 0 auto;
    #     padding: 20px;
    # }
    # </style>

    # <div class="container">
    # </div>
    # """, unsafe_allow_html=True)
    

    # Cargar la página actual
    if st.session_state["page"] == "Inicio":
        contenido_principal()
    elif st.session_state["page"] == "Acerca de":
        mostrar_datos_nacionales()
    elif st.session_state["page"] == "Mapas":
        listado_mapas()
    elif st.session_state["page"] in nombres_unicos:
        encabezado_mapa_individual(zona=str(st.session_state["page"]))
        mapas_individuales(file=str(st.session_state["page"]))
    
    #pie_de_pagina()
if __name__ == "__main__":
    main()