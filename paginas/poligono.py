import folium
import streamlit as st
import geopandas as gpd
from streamlit_folium import st_folium
from utils import dataframes_finais

mapinha = folium.Map(tiles="http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}", attr="Google Maps Satellite", control_scale=True)
cluster = folium.plugins.MarkerCluster().add_to(mapinha)

# sitios - cinza
# imaterial - roxo
# tombados - verde
# valorados - azul


st.title("Patrimônio Brasileiro")

st.write("----")

st.write(
    """
    ## Busca por polígono

    Na seção abaixo, faça o upload de um POLÍGONO georreferenciado para definir a área onde será feita a busca por Bens Culturais acautelados em âmbito federal e, em seguida, clique em **Pesquisar** para exibir os resultados.
    """
)

with st.form("busca", border=False):
    area = st.file_uploader("Selecionar área", type=["kml", "gpkg", "geojson"])
    enviado = st.form_submit_button("Pesquisar", type="primary")
    
    if enviado:
        tooltip = folium.Tooltip(text="Área da busca")
        folium.GeoJson(
            gpd.read_file(area),
            name="Polígono de busca",
            style_function=lambda cor: {"color": "red"},
            tooltip=tooltip,
            ).add_to(cluster)

        with st.status(
            "Pesquisando Bens Culturais na área inserida",
            expanded=True,
            ) as status:
            sitios_pt, sitios_pol, imaterial_pol, imaterial_pt, tombados, valorados, tab_st_tot, tab_sit_pt, tab_sit_pol, tab_im_tot, tab_imtpol, tab_imtpt, tab_tmb, tab_val = dataframes_finais(area)
            
            status.update(label="Pesquisa Concluída", state="complete")

        tab1, tab2, tab3, tab4 = st.tabs([
            "Patrimônio Arqueológico",
            "Patrimônio Imaterial",
            "Patrimônio Tombado",
            "Patrimônio Ferroviário",
            ])

        with tab1:
            st.header("Sítios Arqueológicos Cadastrados")
            
            icon = folium.Icon(color="lightgray")

            popup = folium.GeoJsonPopup(
                fields=["identificacao_bem"],
                aliases=["Sítio arqueológico"],
                )
            tooltip = folium.GeoJsonTooltip(
                fields=["identificacao_bem"],
                aliases=["Sítio arqueológico"],
            )

            if tab_sit_pt.empty and tab_sit_pol.empty:
                st.write("Não foi identificado Patrimônio Arqueológico na área de busca")
            elif tab_sit_pol.empty and not tab_sit_pt.empty:
                st.dataframe(tab_sit_pt, use_container_width=True)
                folium.GeoJson(
                    sitios_pt,
                    name="Bens Arqueológicos (pontos)",
                    marker=folium.Marker(icon=icon),
                    zoom_on_click=True,
                    popup=popup,
                    ).add_to(cluster)
            elif tab_sit_pt.empty and not tab_sit_pol.empty:
                st.dataframe(tab_sit_pol, use_container_width=True)
                folium.GeoJson(
                    sitios_pol,
                    name="Bens Arqueológicos (polígonos)",
                    style_function=lambda cor: {"color": "lightgray"},
                    zoom_on_click=True,
                    tooltip=tooltip,
                    ).add_to(cluster)
            elif not tab_sit_pt.empty and not tab_sit_pol.empty:
                st.dataframe(tab_st_tot, use_container_width=True)
                folium.GeoJson(
                    sitios_pol,
                    name="Bens Arqueológicos (polígonos)",
                    style_function=lambda cor: {"color": "lightgray"},
                    zoom_on_click=True,
                    tooltip=tooltip,
                    ).add_to(cluster)
                folium.GeoJson(
                    sitios_pt,
                    name="Bens Arqueológicos (pontos)",
                    marker=folium.Marker(icon=icon),
                    zoom_on_click=True,
                    popup=popup,
                    ).add_to(cluster)
        
        with tab2:
            st.header("Bens Imateriais Registrados")
            
            icon = folium.Icon(color="purple")

            popup = folium.GeoJsonPopup(
                fields=["identificacao_bem"],
                aliases=["Bem Registrado"],
            )

            tooltip = folium.GeoJsonTooltip(
                fields=["identificacao_bem"],
                aliases=["Bem Registrado"],
            )

            if tab_imtpol.empty and tab_imtpt.empty:
                st.write("Não foi identificado Patrimônio Imaterial na área de busca")
            elif tab_imtpol.empty and not tab_imtpt.empty:
                st.dataframe(tab_imtpt, use_container_width=True)
                folium.GeoJson(
                    imaterial_pt,
                    name="Bens Registrados (pontos)",
                    marker=folium.Marker(icon=icon),
                    zoom_on_click=True,
                    popup=popup,
                    ).add_to(cluster)
            elif tab_imtpt.empty and not tab_imtpol.empty:
                st.dataframe(tab_imtpol, use_container_width=True)
                folium.GeoJson(
                    imaterial_pol,
                    name="Bens Registrados (polígonos)",
                    style_function=lambda cor: {"color": "purple"},
                    zoom_on_click=True,
                    tooltip=tooltip,
                    ).add_to(cluster)
            elif not tab_imtpt.empty and not tab_imtpol.empty:
                st.dataframe(tab_im_tot, use_container_width=True)
                folium.GeoJson(
                    imaterial_pol,
                    name="Bens Registrados (polígonos)",
                    style_function=lambda cor: {"color": "purple"},
                    zoom_on_click=True,
                    tooltip=tooltip,
                    ).add_to(cluster)
                folium.GeoJson(
                    imaterial_pt,
                    name="Bens Registrados (pontos)",
                    marker=folium.Marker(icon=icon),
                    zoom_on_click=True,
                    popup=popup,
                    ).add_to(cluster)
        
        with tab3:
            st.header("Bens Materiais Tombados")

            icon = folium.Icon(color="green")

            popup = folium.GeoJsonPopup(
                fields=["identificacao_bem"],
                aliases=["Bem Tombado"],
                )

            if tab_tmb.empty:
                st.write("Não foi identificado Patrimônio Tombado na área de busca")
            if not tab_tmb.empty:
                st.dataframe(tab_tmb, use_container_width=True)
                folium.GeoJson(
                    tombados,
                    name="Bens Tombados",
                    marker=folium.Marker(icon=icon),
                    zoom_on_click=True,
                    popup=popup,
                    ).add_to(cluster)
        
        with tab4:
            st.header("Bens Materiais Valorados")

            icon = folium.Icon(color="blue")

            popup = folium.GeoJsonPopup(
                fields=["identificacao_bem"],
                aliases=["Bem Valorado"],
                )

            if tab_val.empty:
                st.write("Não foi identificado Patrimônio Ferroviário na área de busca")
            if not tab_val.empty:
                st.dataframe(tab_val, use_container_width=True)
                folium.GeoJson(
                    valorados,
                    name="Bens Valorados",
                    marker=folium.Marker(icon=icon),
                    zoom_on_click=True,
                    popup=popup,
                    ).add_to(cluster)

        folium.LayerControl().add_to(mapinha)
        folium.plugins.MeasureControl(secondary_length_unit="kilometers", secondary_area_unit="hectares").add_to(mapinha)
        folium.plugins.MiniMap(tile_layer="OpenStreetMap.Mapnik", toggle_display=True).add_to(mapinha)
        folium.plugins.Fullscreen().add_to(mapinha)
        
        st_folium(mapinha)


st.write("----")

st.error("**Disclaimer:** Este projeto não possui nenhum vínculo com o Instituto do Patrimôno Histórico e Artístico Nacional - IPHAN ou qualquer outro órgão/instuição.")