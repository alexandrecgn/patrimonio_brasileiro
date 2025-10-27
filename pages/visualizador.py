# import folium
# import streamlit as st
# from streamlit_folium import st_folium


# mapinha = folium.Map(tiles="http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}", attr="Google Maps Satellite", control_scale=True)
# cluster = folium.plugins.MarkerCluster().add_to(mapinha)

# # sitios - cinza
# # imaterial - roxo
# # tombados - verde
# # valorados - azul

# base_sitios_pt = "http://portal.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG%3Asitios&maxFeatures=2147483647&outputFormat=application%2Fjson"
# base_sitios_pol = "https://geoserver.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG%3Asitios_pol&maxFeatures=2147483647&outputFormat=application%2Fjson"
# base_imaterial_pol = "https://raw.githubusercontent.com/alexandrecgn/buscador_patrimonio/refs/heads/main/bens/imaterial_pol.geojson"
# base_imaterial_pt = "https://raw.githubusercontent.com/alexandrecgn/buscador_patrimonio/refs/heads/main/bens/imaterial_pt.geojson"
# base_tombados = "https://raw.githubusercontent.com/alexandrecgn/buscador_patrimonio/refs/heads/main/bens/tombados.geojson"
# base_valorados = "https://raw.githubusercontent.com/alexandrecgn/buscador_patrimonio/refs/heads/main/bens/valorados.geojson"

# st.title("Patrimônio Brasileiro")
# st.write("---")


# st.write("## Visualizador dos Bens Culturais")

# st.warning("*O visualizador ainda está em desenvolvimento. Podem ocorrer problemas de performance.*", icon="🛠️")

# # Ícone, popup e tooltip dos bens arqueológicos
# icon_sitio = folium.Icon(color="lightgray")

# popup_sitio = folium.GeoJsonPopup(
#     fields=["identificacao_bem"],
#     aliases=["Sítio arqueológico"],
#     )

# tooltip_sitio = folium.GeoJsonTooltip(
#     fields=["identificacao_bem"],
#     aliases=["Sítio arqueológico"]
# )


# # Ícone, popup e tooltip dos bens registrados
# icon_imaterial = folium.Icon(color="purple")

# popup_imaterial = folium.GeoJsonPopup(
#     fields=["identificacao_bem"],
#     aliases=["Bem Registrado"],
# )

# tooltip_imaterial = folium.GeoJsonTooltip(
#     fields=["identificacao_bem"],
#     aliases=["Bem Registrado"],
# )


# # Ícone e popup dos bens tombados
# icon_tombado = folium.Icon(color="green")

# popup_tombado = folium.GeoJsonPopup(
#     fields=["identificacao_bem"],
#     aliases=["Bem Tombado"],
#     )


# # Ícone e popup dos bens valorados
# icon_valorado = folium.Icon(color="blue")

# popup_valorado = folium.GeoJsonPopup(
#     fields=["identificacao_bem"],
#     aliases=["Bem Valorado"],
#     )


# with st.status("Carregando visualizador de bens", expanded=True):
#     # Adicionando os bens arqueológicos ao mapa
#     sitios_pt = folium.GeoJson(
#         data=base_sitios_pt,
#         name="Bens Arqueológicos (pontos)",
#         marker=folium.Marker(icon=icon_sitio),
#         zoom_on_click=True,popup=popup_sitio,
#         show=True,
#     )

#     sitios_pol = folium.GeoJson(
#         base_sitios_pol,
#         name="Bens Arqueológicos (polígonos)",
#         style_function=lambda cor: {"color": "lightgray"},
#         zoom_on_click=True,
#         tooltip=tooltip_sitio,
#         show=True,
#     )

#     # Adicionando os bens registrados ao mapa
#     imaterial_pol = folium.GeoJson(
#         data=base_imaterial_pol,
#         name="Bens Registrados (polígonos)",
#         style_function=lambda cor: {"color": "purple"},
#         zoom_on_click=True,
#         tooltip=tooltip_imaterial,
#         show=True,
#     )

#     imaterial_pt = folium.GeoJson(
#         data=base_imaterial_pt,
#         name="Bens Registrados (pontos)",
#         marker=folium.Marker(icon=icon_imaterial),
#         zoom_on_click=True,
#         popup=popup_imaterial,
#         show=True,
#     )


#     # Adicionando os bens tombados ao mapa
#     tombados = folium.GeoJson(
#         data=base_tombados,
#         name="Bens Tombados",
#         marker=folium.Marker(icon=icon_tombado),
#         zoom_on_click=True,
#         popup=popup_tombado,
#         show=True,
#     )


#     # Adicionando os bens valorados ao mapa
#     valorados = folium.GeoJson(
#         base_valorados,
#         name="Bens Valorados",
#         marker=folium.Marker(icon=icon_valorado),
#         zoom_on_click=True,
#         popup=popup_valorado,
#         show=True,
#     )


#     sitios_pt.add_to(cluster)
#     sitios_pol.add_to(cluster)
#     imaterial_pol.add_to(cluster)
#     imaterial_pt.add_to(cluster)
#     tombados.add_to(cluster)
#     valorados.add_to(cluster)

#     folium.plugins.MeasureControl(secondary_length_unit="kilometers", secondary_area_unit="hectares").add_to(mapinha)
#     folium.plugins.MiniMap(tile_layer="OpenStreetMap.Mapnik", toggle_display=True).add_to(mapinha)
#     folium.plugins.Fullscreen().add_to(mapinha)

#     with st.form("mapa", border=False):
#         st_folium(mapinha)
#         st.form_submit_button(disabled=True)

# st.write("---")
# st.error("**Disclaimer:** Este projeto não possui nenhum vínculo com o Instituto do Patrimôno Histórico e Artístico Nacional - IPHAN ou qualquer outro órgão/instuição.")