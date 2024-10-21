import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
from pyproj import Proj, transform
import os
#from utils.capas import *
from utils.vistas import *
from utils.mapas import *



# Función principal para organizar la aplicación
def main():
    # Creación de columna de navegación
    columna_navegacion()    
    
    
if __name__ == "__main__":
    main()