import folium

m = folium.Map(location=[45.3288, -121.6625], zoom_start=12)

url = "https://leafletjs.com/examples/custom-icons/{}".format
icon_image = url("leaf-red.png")
shadow_image = url("leaf-shadow.png")

icon = folium.CustomIcon(
    icon_image,
    icon_size=(38, 95),
    icon_anchor=(22, 94),
    shadow_image=shadow_image,
    shadow_size=(50, 64),
    shadow_anchor=(4, 62),
    popup_anchor=(-3, -76),
)

folium.Marker(
    location=[45.3288, -121.6625], icon=icon, popup="Mt. Hood Meadows"
).add_to(m)

m