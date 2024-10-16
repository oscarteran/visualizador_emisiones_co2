import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd
from pyproj import Proj, transform
import os
from utils.utils import *


# Título y descripción de la aplicación
st.title("Mapa Interactivo de emisiones de CO2.")
st.markdown("""
# Visualización de CO2
Mapas interactivos para revisión de datos de emisiones de CO2.  
""")


# Despliegue de mapa
st.markdown("""
### Visualización de datos de La Escalera
""")
plot_map('data/raw/P_Escalera.csv')

# Despliegue de mapa
st.markdown("""
### Visualización de datos de Los Azufres
""")
plot_map('data/raw/P_Azufres.csv')

