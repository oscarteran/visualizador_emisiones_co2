import pandas as pd
from pyproj import Proj
import folium
from streamlit_folium import st_folium
import streamlit as st
import json

def grafico_de_puntos(file: str):
    # Abrir y leer el archivo JSON
    with open(file, 'r') as archivo_json:
        mi_diccionario = json.load(archivo_json)
        
    # Conversión de JSON a DF
    nombres, lat, lon = [], [], []

    for key, value in mi_diccionario.items():
        nombres.append(key)
        lat.append(value[0])
        lon.append(value[1])
        
    df = pd.DataFrame(data={'ubi': nombres, 'Lat': lat, 'Lon': lon})
    
    # Crear un mapa centrado en el primer punto
    mapa = folium.Map(location=[23.6345, -102.5528], 
                      tiles="Stadia.AlidadeSatellite",
                      #tiles="OpenStreetMap",
                      zoom_start=5,
                    )

    # Definir el tamaño de la malla (en metros, ajustar según sea necesario)
    grid_size = 10  # Tamaño del cuadrado de la malla

    # Añadir la malla al mapa
    for x in range(int(df['Lat'].min()), int(df['Lat'].max()), grid_size):
        for y in range(int(df['Lon'].min()), int(df['Lon'].max()), grid_size):
            mask = (df['Lat'] >= x) & (df['Lat'] < x + grid_size) & \
                   (df['Lon'] >= y) & (df['Lon'] < y + grid_size)
            
            if mask.any():
                #avg_co2 = df.loc[mask, 'CO2_value'].mean()
                folium.Rectangle(
                    bounds=[[y, x], [y + grid_size, x + grid_size]], 
                    color='blue', 
                    fill=True,
                    fill_opacity=0.1,
                    #tooltip=f"Promedio CO₂: {avg_co2:.2f} gm-2-d-1"
                ).add_to(mapa)

    # Añadir puntos al mapa
    for _, row in df.iterrows():
        folium.Marker([row['Lat'], row['Lon']], 
                      popup=f"({row['Lat']}, {row['Lon']})",
                      icon=folium.Icon(icon="cloud", color="red"),
                      tooltip=row['ubi'],
                      ).add_to(mapa)

    # Mostrar el mapa en la aplicación web dentro de un contenedor
    with st.container():
        st_folium(mapa, width=700, height=500)
    
    

def plot_map(file: str):
    ## Todo el código debe ir a una función
    # Carga de datos
    df = pd.read_csv(file)
    df.columns = ['UTM X', 'UTM Y', 'CO2_value', 'Nombre de la zona']

    # Definir el sistema de coordenadas UTM (Zona 16N en este caso, cambia según sea necesario)
    proj_utm = Proj(proj='utm', zone=14, ellps='WGS84')

    # Función para convertir coordenadas UTM a latitud/longitud
    def utm_to_latlon(x, y, proj_utm):
        lon, lat = proj_utm(x, y, inverse=True)
        return lat, lon

    # Crear nuevas columnas en el DataFrame para latitud y longitud
    df['lat'], df['lon'] = zip(*df.apply(lambda row: utm_to_latlon(row['UTM X'], row['UTM Y'], proj_utm), axis=1))

    # Crear un mapa centrado en el primer punto
    mapa = folium.Map(location=[23.6345, -102.5528], 
                      tiles="Stadia.AlidadeSatellite",
                      zoom_start=5,
                    )

    # Definir el tamaño de la malla (en metros, ajustar según sea necesario)
    grid_size = 10  # Tamaño del cuadrado de la malla

    # Añadir la malla al mapa
    for x in range(int(df['UTM X'].min()), int(df['UTM X'].max()), grid_size):
        for y in range(int(df['UTM Y'].min()), int(df['UTM Y'].max()), grid_size):
            mask = (df['UTM X'] >= x) & (df['UTM X'] < x + grid_size) & \
                   (df['UTM Y'] >= y) & (df['UTM Y'] < y + grid_size)
            
            if mask.any():
                avg_co2 = df.loc[mask, 'CO2_value'].mean()
                folium.Rectangle(
                    bounds=[[y, x], [y + grid_size, x + grid_size]], 
                    color='blue', 
                    fill=True,
                    fill_opacity=0.1,
                    tooltip=f"Promedio CO₂: {avg_co2:.2f} gm-2-d-1"
                ).add_to(mapa)

    # Añadir puntos al mapa
    for _, row in df.iterrows():
        folium.Marker([row['lat'], row['lon']], 
                      popup=f"({row['UTM X']}, {row['UTM Y']})",
                      icon=folium.Icon(icon="cloud", color="blue"),
                      tooltip=f"Valor de CO₂: {row['CO2_value']} gm-2-d-1",
                      ).add_to(mapa)

    # Mostrar el mapa en la aplicación web dentro de un contenedor
    with st.container():
        st_folium(mapa, width=700, height=500)
        
    #folium.TileLayer('Stamen Terrain', attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.').add_to(mapa)
