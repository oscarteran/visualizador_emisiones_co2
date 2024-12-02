import pandas as pd
from pyproj import Proj
import folium
from streamlit_folium import st_folium
import streamlit as st
import json
from pathlib import Path
import numpy as np

def grafico_de_puntos(file: str):
    """
    Genera y muestra un mapa con puntos geolocalizados y una malla sobre una región específica.

    La función carga un archivo JSON con coordenadas geográficas, convierte los datos a un DataFrame de Pandas, 
    y utiliza la biblioteca Folium para renderizar un mapa interactivo centrado en México. Cada punto en el mapa 
    representa una ubicación geográfica, y la función también dibuja una malla rectangular de tamaño configurable 
    para cubrir la región.

    Parámetros:
    -----------
    - file (str): Ruta al archivo JSON que contiene las ubicaciones geográficas en formato clave-valor, donde
      la clave es el nombre de la ubicación y el valor es una lista con latitud y longitud [lat, lon].

    Archivos requeridos:
    --------------------
    - Archivo JSON en la ruta especificada por `file`, que debe tener el siguiente formato:
      ```
      {
        "ubicacion1": [lat1, lon1],
        "ubicacion2": [lat2, lon2],
        ...
      }
      ```

    Detalles del procesamiento:
    ---------------------------
    1. Lee el archivo JSON y carga los datos en un diccionario de Python.
    2. Convierte el diccionario a un DataFrame de Pandas con columnas para nombres de ubicaciones, latitudes y longitudes.
    3. Configura un mapa interactivo de Folium con una capa de imagen satelital de Esri centrado en México.
    4. Dibuja una malla rectangular sobre el área, subdividiendo la región en cuadrados de `grid_size` metros.
    5. Añade marcadores en cada punto de la ubicación con un ícono rojo y una etiqueta con el nombre de la ubicación.
    6. Muestra el mapa en un contenedor Streamlit, con un alto de 600 píxeles para mejorar la visualización.

    Variables y configuración:
    --------------------------
    - api_key: Llave de API opcional para cargar capas de mapa de Stadia Maps.
    - grid_size: Tamaño de cada cuadrado de la malla en grados. Este valor es ajustable según las necesidades.

    Bibliotecas utilizadas:
    ------------------------
    - json: Para cargar datos desde el archivo JSON.
    - pandas as pd: Para manejar datos estructurados en formato tabular.
    - folium: Para la creación del mapa interactivo.
    - streamlit as st: Para mostrar el mapa en una aplicación web de Streamlit.
    - st_folium: Para renderizar el mapa de Folium dentro de la aplicación Streamlit.

    Ejemplo de uso:
    ---------------
    >>> grafico_de_puntos("data/processed/nombres_unicos.json")
    """
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
    
    # API Key
    api_key = "4829d3b3-dc57-4df5-bf47-e9b7732ae181"
    # Crear un mapa centrado en el primer punto
    mapa = folium.Map(location=[23.5, -100], 
                      #tiles="https://tiles.stadiamaps.com/tiles/alidade_satellite/{z}/{x}/{y}.png?api_key="+api_key, 
                      attr='&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>',
                      #tiles="Stadia.AlidadeSatellite",
                      #tiles="OpenStreetMap",
                      tiles='Esri.WorldImagery',
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
        st_folium(mapa, width=None, height=600)
        


def mapas_individuales(file):
    """
    Genera y muestra un mapa interactivo de ubicaciones individuales con una malla de áreas específicas.

    La función lee un archivo CSV con datos de latitud, longitud y valores de CO₂ para una ubicación específica,
    genera un mapa centrado en los puntos, y traza una malla rectangular para subdividir el área. Los puntos 
    en el mapa están marcados con valores de CO₂ en un tooltip y un ícono de marcador.

    Parámetros:
    -----------
    - file (str): Nombre del archivo CSV que contiene los datos de ubicación. La función construye la ruta 
      completa del archivo a partir de este nombre, asumiendo una estructura de carpetas en `data/processed/`.

    Archivos requeridos:
    --------------------
    - CSV con el nombre especificado en `file`, ubicado en "data/processed/" con el formato `P_{file}LatLon.csv`.
      El CSV debe contener las columnas:
        - `Lat`: Latitud de la ubicación.
        - `Lon`: Longitud de la ubicación.
        - `CO2_value`: Valor de CO₂ en gm-2-d-1.

    Detalles del procesamiento:
    ---------------------------
    1. Construye la ruta del archivo CSV, la formatea para el sistema operativo y lee los datos en un DataFrame.
    2. Configura un mapa Folium con capa satelital Esri centrado en el promedio de las coordenadas de latitud y longitud.
    3. Define una malla de cuadrícula sobre el área, subdividiéndola en cuadrados de `grid_size` grados, ajustable según sea necesario.
    4. Añade un marcador en cada punto del DataFrame con la coordenada y el valor de CO₂ en el tooltip.
    5. Ajusta los límites visibles del mapa para mostrar todos los puntos de interés.
    6. Muestra el mapa en un contenedor de Streamlit con un alto de 500 píxeles para asegurar una buena visibilidad.

    Variables y configuración:
    --------------------------
    - api_key: Llave de API opcional para cargar capas de mapa de Stadia Maps.
    - grid_size: Tamaño del cuadrado de la malla en grados. Este valor puede ajustarse para cubrir el área deseada.

    Bibliotecas utilizadas:
    ------------------------
    - pandas as pd: Para manejar datos tabulares del archivo CSV.
    - folium: Para la creación y configuración del mapa interactivo.
    - streamlit as st: Para mostrar el mapa en una aplicación web.
    - st_folium: Para renderizar el mapa Folium dentro de la aplicación Streamlit.

    Ejemplo de uso:
    ---------------
    >>> mapas_individuales("nombre_del_archivo")
    """
    # Creacion de ruta completa de archivo
    ruta = f"data/processed/P_{file}LatLon.csv"
    # Formateo de ruta para actualizarse a sistema operativo
    ruta_formateada = Path(ruta)
    # Lectura de csv de mapa
    df = pd.read_csv(ruta_formateada) 
    
    # API Key
    api_key = "4829d3b3-dc57-4df5-bf47-e9b7732ae181"
    # Crear un mapa centrado en el primer punto
    mapa = folium.Map(location=[df['Lat'].mean(), df['Lon'].mean()], 
                      #tiles="https://tiles.stadiamaps.com/tiles/alidade_satellite/{z}/{x}/{y}.png?api_key="+api_key, 
                      attr='&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>',
                      #tiles="Stadia.AlidadeSatellite",
                      #tiles="OpenStreetMap",
                      tiles='Esri.WorldImagery',
                      zoom_start=12,
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
                      tooltip=f"Emisión CO₂: {row['CO2_value']:.2f} gm-2-d-1"
                      ).add_to(mapa)
        
    # Ajuste de limites visibles del mapa
    mapa.fit_bounds([[df['Lat'].min(), df['Lon'].min()], [df['Lat'].max(), df['Lon'].max()]])
        
    # Mostrar el mapa en la aplicación web dentro de un contenedor
    with st.container():
        st_folium(mapa, width=None, height=500)


"""
-----------------------------------------------------------------------------
------------------------ FUNCIONES DEPRECADAS -------------------------------
-----------------------------------------------------------------------------
"""


# def plot_map(file: str):
#     ## Todo el código debe ir a una función
#     # Carga de datos
#     df = pd.read_csv(file)
#     df.columns = ['UTM X', 'UTM Y', 'CO2_value', 'Nombre de la zona']

#     # Definir el sistema de coordenadas UTM (Zona 16N en este caso, cambia según sea necesario)
#     proj_utm = Proj(proj='utm', zone=14, ellps='WGS84')

#     # Función para convertir coordenadas UTM a latitud/longitud
#     def utm_to_latlon(x, y, proj_utm):
#         lon, lat = proj_utm(x, y, inverse=True)
#         return lat, lon

#     # Crear nuevas columnas en el DataFrame para latitud y longitud
#     df['lat'], df['lon'] = zip(*df.apply(lambda row: utm_to_latlon(row['UTM X'], row['UTM Y'], proj_utm), axis=1))

#     # Crear un mapa centrado en el primer punto
#     mapa = folium.Map(location=[23.6345, -102.5528], 
#                       tiles='Esri.WorldImagery',
#                       zoom_start=5,
#                     )

#     # Definir el tamaño de la malla (en metros, ajustar según sea necesario)
#     grid_size = 10  # Tamaño del cuadrado de la malla

#     # Añadir la malla al mapa
#     for x in range(int(df['UTM X'].min()), int(df['UTM X'].max()), grid_size):
#         for y in range(int(df['UTM Y'].min()), int(df['UTM Y'].max()), grid_size):
#             mask = (df['UTM X'] >= x) & (df['UTM X'] < x + grid_size) & \
#                    (df['UTM Y'] >= y) & (df['UTM Y'] < y + grid_size)
            
#             if mask.any():
#                 avg_co2 = df.loc[mask, 'CO2_value'].mean()
#                 folium.Rectangle(
#                     bounds=[[y, x], [y + grid_size, x + grid_size]], 
#                     color='blue', 
#                     fill=True,
#                     fill_opacity=0.1,
#                     tooltip=f"Promedio CO₂: {avg_co2:.2f} gm-2-d-1"
#                 ).add_to(mapa)

#     # Añadir puntos al mapa
#     for _, row in df.iterrows():
#         folium.Marker([row['lat'], row['lon']], 
#                       popup=f"({row['UTM X']}, {row['UTM Y']})",
#                       icon=folium.Icon(icon="cloud", color="blue"),
#                       tooltip=f"Valor de CO₂: {row['CO2_value']} gm-2-d-1",
#                       ).add_to(mapa)

#     # Mostrar el mapa en la aplicación web dentro de un contenedor
#     with st.container():
#         st_folium(mapa, width=700, height=500)
        
#     #folium.TileLayer('Stamen Terrain', attr='Map tiles by Stamen Design, under CC BY 3.0. Data by OpenStreetMap, under ODbL.').add_to(mapa)
