import folium
import streamlit as st
import pandas as pd
import geopandas as gpd
from streamlit_folium import st_folium
from utils import pesquisar
from layout import hero, page_config, disclaimer


# Carregar configuração da página.
page_config()


# Criar os objetos base para o mapa.
#  ----------------------------------------------------------------------------------------------------------------
# Criar instância do mapa com base map da imagem de satélite do Google.
mapinha = folium.Map(
    tiles="http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}",
    attr="Google Maps Satellite",
    control_scale=True,
    prefer_canvas=True,
    font_size="0.8rem",
    )
# Criar instância da tooltip.
tooltip_area = folium.Tooltip(text="Área da busca")
# Criar instância dos ícones.
icon = folium.Icon(color="lightgray")
# Criar as duas instâncias de popup.
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
# Criar instância dos marcadores.
marker = folium.Marker(popup=popup1, icon=icon)

#  ----------------------------------------------------------------------------------------------------------------


# Carregar o cabeçalho da página.
hero()

# Apresentar a funcionalidade de busca por polígono.
st.write(
    """
    ### Busca por polígono

    Na seção abaixo, faça o upload de um POLÍGONO georreferenciado para definir a área onde será feita a busca por Bens Culturais acautelados em âmbito federal e, em seguida, clique em **Pesquisar** para exibir os resultados.
    """
)

# Criar formulário para o conteúdo do site.
# Foi escolhido criar um formulário porquê o st.button() não mantém o estado true.
with st.form("busca", border=False):
    with st.container(border=True, vertical_alignment="center"):
        area = st.file_uploader("Selecionar área", type=["kml", "gpkg", "geojson"])
        enviado = st.form_submit_button("Pesquisar", type="primary")
    
# Se o botão "Pesquisar" for clicado a área de busca será carregada.
    if enviado:
        folium.GeoJson(
            gpd.read_file(area),
            name="Polígono de busca",
            style_function=lambda cor: {"color": "red"},
            tooltip=tooltip_area,
            ).add_to(mapinha)

# Fazer busca de bens utilizando o polígono carregado.
        with st.status(
            "Pesquisando Bens Culturais na área inserida",
            expanded=True,
            ) as status:
            resultado_pol, resultado_pt = pesquisar(area=area)

# Carregar no mapa os bens encontrados na geometria polígono.
            folium.GeoJson(
                data=resultado_pol,
                name="Bens Culturais (polígonos)",
                style_function=lambda cor: {"color": "yellow"},
                popup=popup1,
                ).add_to(mapinha)
# Carregar no mapa os bens encontrados na geometria ponto.
            folium.GeoJson(
                data=resultado_pt,
                name="Bens Culturais (pontos)",
                marker=marker,
                popup=popup2,
                ).add_to(mapinha)

# Adicionar controle de camadas.            
            folium.LayerControl().add_to(mapinha)
            # folium.plugins.MeasureControl(secondary_length_unit="kilometers", secondary_area_unit="hectares").add_to(mapinha)
            # folium.plugins.MiniMap(tile_layer="OpenStreetMap.Mapnik", toggle_display=True).add_to(mapinha)
            # folium.plugins.Fullscreen().add_to(mapinha)
        
            status.update(label="Pesquisa Concluída", state="complete")
# Exibir o mapa.
            with st.container(height="content"):
                st_folium(
                    fig=mapinha,
                    use_container_width=True
                    )
            with st.container(height="content"):
                tabela = pd.concat([resultado_pol, resultado_pt])
# Carregar o resultado da busca em formato de tabela.
                st.dataframe(
                    data=tabela,
                    hide_index=True,
                    column_config={
                        "nome": st.column_config.Column(pinned=True),
                        "ficha": st.column_config.LinkColumn(),
                        },
                )


# Carregar o disclaimer.
disclaimer()
