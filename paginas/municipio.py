import folium
import streamlit as st
# import geopandas as gpd
# import pandas as pd
# from streamlit_folium import st_folium
# from utils import pesquisar, to_dict, refinar_material, refinar_imaterial

mapinha = folium.Map(tiles="Esri WorldImagery", control_scale=True)

# sitios - cinza
# imaterial - roxo
# tombados - verde
# valorados - azul

base_sitios = "http://portal.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG%3Asitios&maxFeatures=2147483647&outputFormat=application%2Fjson"
base_imaterial_pol = "https://raw.githubusercontent.com/alexandrecgn/buscador_patrimonio/refs/heads/main/bens/imaterial_pol.geojson"
base_imaterial_pt = "https://raw.githubusercontent.com/alexandrecgn/buscador_patrimonio/refs/heads/main/bens/imaterial_pt.geojson"
base_tombados = "https://raw.githubusercontent.com/alexandrecgn/buscador_patrimonio/refs/heads/main/bens/tombados.geojson"
base_valorados = "https://raw.githubusercontent.com/alexandrecgn/buscador_patrimonio/refs/heads/main/bens/valorados.geojson"


st.title("Buscador do Patrimônio")


st.write("## Busca por município")


st.write("Em desenvolvimento")
st.warning("*A pesquisa por municípios estará disponível em breve.*", icon="🛠️")
st.error("**Disclaimer:** Este projeto não possui nenhum vínculo com o Instituto do Patrimôno Histórico e Artístico Nacional - IPHAN ou qualquer outro órgão/instuição.")