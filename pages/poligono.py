import folium
import streamlit as st
import pandas as pd
import geopandas as gpd
from streamlit_folium import st_folium
from utils import pesquisar
from layout import hero, page_config, disclaimer


page_config()


#  ----------------------------------------------------------------------------------------------------------------
mapinha = folium.Map(
    tiles="http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}",
    attr="Google Maps Satellite",
    control_scale=True,
    prefer_canvas=True,
    font_size="0.8rem",
    )
tooltip_area = folium.Tooltip(text="Área da busca")
icon = folium.Icon(color="lightgray")
popup1 = folium.GeoJsonPopup(
                fields=["nome", "tipo", "ficha"],
                aliases=["Nome do Bem:", "Tipo:", "Ficha do bem:"],
                max_width=500,
                localize=True,
)
popup2 = folium.GeoJsonPopup(
                fields=["nome", "tipo", "ficha"],
                aliases=["Nome do Bem:", "Tipo:", "Ficha do bem:"],
                max_width=500,
                localize=True,
)
marker = folium.Marker(popup=popup1, icon=icon)

#  ----------------------------------------------------------------------------------------------------------------


hero()

st.write(
    """
    ### Busca por polígono

    Na seção abaixo, faça o upload de um POLÍGONO georreferenciado para definir a área onde será feita a busca por Bens Culturais acautelados em âmbito federal e, em seguida, clique em **Pesquisar** para exibir os resultados.
    """
)

with st.form("busca", border=False):
    with st.container(border=True, vertical_alignment="center"):
        area = st.file_uploader("Selecionar área", type=["kml", "gpkg", "geojson"])
        enviado = st.form_submit_button("Pesquisar", type="primary")
    
    if enviado:
        folium.GeoJson(
            gpd.read_file(area),
            name="Polígono de busca",
            style_function=lambda cor: {"color": "red"},
            tooltip=tooltip_area,
            ).add_to(mapinha)

        with st.status(
            "Pesquisando Bens Culturais na área inserida",
            expanded=True,
            ) as status:
            resultado_pol, resultado_pt = pesquisar(area=area)

            folium.GeoJson(
                data=resultado_pol,
                name="Bens Culturais (polígonos)",
                style_function=lambda cor: {"color": "yellow"},
                popup=popup1,
                ).add_to(mapinha)
            folium.GeoJson(
                data=resultado_pt,
                name="Bens Culturais (pontos)",
                marker=marker,
                popup=popup2,
                ).add_to(mapinha)

            folium.LayerControl().add_to(mapinha)
            # folium.plugins.MeasureControl(secondary_length_unit="kilometers", secondary_area_unit="hectares").add_to(mapinha)
            # folium.plugins.MiniMap(tile_layer="OpenStreetMap.Mapnik", toggle_display=True).add_to(mapinha)
            # folium.plugins.Fullscreen().add_to(mapinha)
        
            status.update(label="Pesquisa Concluída", state="complete")
            st_folium(
                fig=mapinha,
                use_container_width=True
                )
            
            tabela = pd.concat([resultado_pol, resultado_pt])
            st.dataframe(
                data=tabela,
                hide_index=True,
                column_config={
                    "nome": st.column_config.Column(pinned=True),
                    "ficha": st.column_config.LinkColumn(),
                    },
            )


disclaimer()
