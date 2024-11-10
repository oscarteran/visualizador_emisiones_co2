import streamlit as st
import folium
from .pages import *

# FUNCION DEPRECADA
def mostrar_pagina_(pagina):
    if pagina == 'home':
        st.header("Página Principal")
        st.write("Bienvenido a la página principal.")
        show_country()
    elif pagina == 'detalle1':
        st.header("Detalles de la ubicación 1")
        st.write("Esta es la página de detalles para la ubicación 1.")
        
    elif pagina == 'detalle2':
        st.header("Detalles de la ubicación 2")
        st.write("Esta es la página de detalles para la ubicación 2.")
    elif pagina == 'mapa':
        st.header("Mapa Interactivo")
        mapa = folium.Map(location=[23.6345, -102.5528], zoom_start=5)