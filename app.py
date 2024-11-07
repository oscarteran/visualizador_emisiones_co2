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
    # Uso completo de la página
    st.set_page_config(layout="wide")

    
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

    
    # Cargar la página actual
    if st.session_state["page"] == "Inicio":
        contenido_principal()
    elif st.session_state["page"] == "Acerca de":
        mostrar_datos_nacionales()
    elif st.session_state["page"] == "Mapas":
        listado_mapas()
    # elif st.session_state["page"] == "Bibliografía":
    #     bibliografía()
    elif st.session_state["page"] in nombres_unicos:
        encabezado_mapa_individual(zona=str(st.session_state["page"]))
        mapas_individuales(file=str(st.session_state["page"]))
    
    #pie_de_pagina()
if __name__ == "__main__":
    main()