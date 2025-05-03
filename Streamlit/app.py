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
    """
    Función principal para organizar la aplicación y controlar la navegación entre las diferentes páginas.
    
    Esta función configura el diseño de la página, inicializa el estado de sesión para manejar la navegación, 
    carga una lista de nombres únicos de ubicaciones, y muestra el contenido adecuado basado en la página actual.
    
    Flujo de la función:
    1. Configura la página en modo ancho completo.
    2. Inicializa la variable de sesión `page` con el valor "Inicio" si aún no ha sido definida.
    3. Llama a la función `definir_pagina_actual` para actualizar la página actual según la navegación.
    4. Lee un archivo JSON con la lista de nombres únicos de ubicaciones.
    5. Carga y muestra el contenido correspondiente según la página actual.
    
    Parámetros:
    ----------
    No recibe parámetros directos. Utiliza y modifica el estado de sesión (`st.session_state`).
    
    Variables de sesión utilizadas:
    -------------------------------
    - st.session_state["page"]: indica la página actual de la aplicación.
    
    Funciones auxiliares:
    ---------------------
    - definir_pagina_actual(): Actualiza la página actual en base a la navegación del usuario.
    - contenido_principal(): Muestra el contenido de la página de inicio.
    - mostrar_datos_nacionales(): Muestra la sección de datos nacionales.
    - listado_mapas(): Muestra una lista de mapas.
    - bibliografia(): Muestra la sección de bibliografía.
    - pie_de_pagina(): Muestra el pie de página en la sección de bibliografía.
    - encabezado_mapa_individual(zona): Muestra el encabezado para un mapa específico.
    - mapas_individuales(file): Muestra un mapa individual basado en el archivo correspondiente.
    
    Archivos utilizados:
    --------------------
    - `nombres_unicos.json`: JSON ubicado en "data/processed/nombres_unicos.json" que contiene una lista de ubicaciones únicas.
    
    """

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
    elif st.session_state["page"] == "Bibliografía":
        bibliografia()
        pie_de_pagina()
    elif st.session_state["page"] in nombres_unicos:
        encabezado_mapa_individual(zona=str(st.session_state["page"]))
        mapas_individuales(file=str(st.session_state["page"]))
    
    #pie_de_pagina()


if __name__ == "__main__":
    main()