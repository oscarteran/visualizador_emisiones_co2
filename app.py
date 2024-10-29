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



# Función principal para organizar la aplicación
def main():
    # Creación de columna de navegación
    #columna_navegacion()    

    
    #mostrar_pagina(pagina=pagina)

    # Invocar funcion para definir vista actual:
    definir_pagina_actual()

    # Cargar la página actual
    if st.session_state["page"] == "Inicio":
        contenido_principal()
    elif st.session_state["page"] == "Acerca de":
        mostrar_datos_nacionales()
    elif st.session_state["page"] == "Mapas":
        datos_nacionales()
    
if __name__ == "__main__":
    main()