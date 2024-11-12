import streamlit as st
from busca_web import pesquisar, refinar_material, refinar_imaterial


base_sitios = "http://portal.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG%3Asitios&maxFeatures=2147483647&outputFormat=application%2Fjson"
base_imaterial = "https://raw.githubusercontent.com/alexandrecgn/buscador_patrimonio/refs/heads/main/web/bens/imaterial.geojson"
base_tombados = "https://raw.githubusercontent.com/alexandrecgn/buscador_patrimonio/refs/heads/main/web/bens/tombados.geojson"
base_valorados = "https://raw.githubusercontent.com/alexandrecgn/buscador_patrimonio/refs/heads/main/web/bens/valorados.geojson"


# Título
st.title("Buscador do Patrimônio")

# Descrição
st.write(
    "Faça o upload de um POLÍGONO georreferenciado para definir a área onde será feita a busca por Bens Culturais acautelados em âmbito federal e, em seguida, clique em **Buscar** para exibir os resultados"
)

# Aviso
st.warning("Formatos de arquivo suportados: KML (Google Earth), Geopackage, GeoJSON")

with st.form("pesquisa"):
    # Adicionar área de busca
    area = st.file_uploader("Selecionar área", type=["kml", "gpkg", "geojson"])

    # TODO: Adicionar a pesquisa com retorno para cada categoria de bem
    # tipos = st.multiselect("Categorias", ["Patrimônio Arqueológico", "Patrimônio Imaterial", "Patrimônio Tombado", "Patrimônio Valorado"])

    enviado = st.form_submit_button("Pesquisar")
    if enviado:
        sitios = pesquisar(area, base_sitios)
        imaterial = pesquisar(area, base_imaterial)
        tombados = pesquisar(area, base_tombados)
        valorados = pesquisar(area, base_valorados)
        tab_sit = refinar_material(sitios, "Patrimônio Arqueológico")
        tab_imt = refinar_imaterial(imaterial)
        tab_tmb = refinar_material(tombados, "Patrimônio Tombado")
        tab_val = refinar_material(valorados, "Patrimônio Ferroviário")

        if tab_sit.empty:
            st.write("Não foi identificado Patrimônio Arqueológico na área de busca")
        if not tab_sit.empty:
            st.dataframe(tab_sit)
        if tab_imt.empty:
            st.write("Não foi identificado Patrimônio Imaterial na área de busca")
        if not tab_imt.empty:
            st.dataframe(tab_imt)
        if tab_tmb.empty:
            st.write("Não foi identificado Patrimônio Tombado na área de busca")
        if not tab_tmb.empty:
            st.dataframe(tab_tmb)
        if tab_val.empty:
            st.write("Não foi identificado Patrimônio Ferroviário na área de busca")
        if not tab_val.empty:
            st.dataframe(tab_val)
        
