import pandas as pd
from pyproj import Proj
import folium
from streamlit_folium import st_folium



def plot_map(file: str):
    ## Todo el codigo debe ir a una funcion
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
    mapa = folium.Map(location=[df['lat'].mean(), df['lon'].mean()], zoom_start=13)

    # Definir el tamaño de la malla (en metros, ajustar según sea necesario)
    grid_size = 10  # Tamaño del cuadrado de la malla

    # Añadir la malla al mapa
    for x in range(int(df['UTM X'].min()), int(df['UTM X'].max()), grid_size):
        for y in range(int(df['UTM Y'].min()), int(df['UTM Y'].max()), grid_size):
            # Calcular el valor promedio de CO₂ para el cuadrado
            # (puedes ajustar esta lógica según cómo quieras agrupar los datos)
            mask = (df['UTM X'] >= x) & (df['UTM X'] < x + grid_size) & \
                (df['UTM Y'] >= y) & (df['UTM Y'] < y + grid_size)
            
            if mask.any():
                avg_co2 = df.loc[mask, 'CO2_value'].mean()
                # Crear el rectángulo
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

    # Mostrar el mapa en la aplicación web
    st_folium(mapa, width=700, height=500)