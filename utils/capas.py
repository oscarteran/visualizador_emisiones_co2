# Capas base diferentes
folium.TileLayer('openstreetmap').add_to(mapa)
folium.TileLayer('Stamen Terrain').add_to(mapa)
folium.TileLayer('Stamen Toner').add_to(mapa)
folium.TileLayer('Stamen Watercolor').add_to(mapa)
folium.TileLayer('CartoDB Positron').add_to(mapa)
folium.TileLayer('CartoDB Dark_Matter').add_to(mapa)
