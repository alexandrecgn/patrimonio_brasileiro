"""
Copyright© 2024 Alexandre Cavalcanti

    This file is part of "Patrimônio Brasileiro".

    "Patrimônio Brasileiro" is free software: you can redistribute
    it and/or modify it under the terms of the GNU General Public
    License as published by the Free Software Foundation, either version
    3 of the License, or (at your option) any later version.

    "Patrimônio Brasileiro" is distributed in the hope that it will
    be useful, but WITHOUT ANY WARRANTY; without even the implied
    warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with "Patrimônio Brasileiro".
    If not, see <https://www.gnu.org/licenses/>.
"""

import geopandas as gpd
import pandas as pd
import streamlit as st


@st.cache_data
def pesquisar(area):
    """
    Recebe um arquivo georreferenciado de um polígono e verifica se existem bens \
    culturais nessa área

    Args:
        area (arquivo georreferenciado): _description_

    Returns:
        resultado_pol (GeoDataFrame): GeoDataFrame com os bens culturais em formato\
            polígono encontrados na área.
        resultado_pt (GeoDataFrame): GeoDataFrame com os bens culturais em formato\
            ponto encontrados na área.
    """
    # Carregar o arquivo geo da área de busca.
    busca = gpd.read_file(area)
    # Carregar o arquivo de bens culturais no formato polígono.
    bens_pol = gpd.read_file("bens/bens_pol.gpkg")
    # Carregar o arquivo de bens culturais no formato ponto.
    bens_pt = gpd.read_file("bens/bens_pt.gpkg")
    # Fazer o intersect da área de busca com os bens culturais.
    resultado_pol = gpd.overlay(
        busca, bens_pol, how="intersection", keep_geom_type=False
    )
    resultado_pt = gpd.overlay(busca, bens_pt, how="intersection", keep_geom_type=False)
    # Retornar os bens em polígono e ponto eventualmente existentes na área.
    return resultado_pol, resultado_pt


def separar_tombados(nome_arquivo, nome_planilha):
    # Carregar o tabelão de bens tombados da CGID/DEPAM.
    tomb_tabelao = pd.read_excel(nome_arquivo, nome_planilha)
    # Transformar o dtype das colunas em string.
    tomb_str = tomb_tabelao.astype(dtype=str)

    # Criar lista vazia para receber códigos SICG dos bens no tabelão
    sicg = []

    # Filtrar os bens do tabelão para selecionarsomente os verdadeiramente tombados e carregá-los no DataFrame vazio.
    for index, row in tomb_str.iterrows():
        if (
            row["Estágio da Instrução (Portaria 11/86)"] == "HOMOLOGADO"
            or row["Estágio da Instrução (Portaria 11/86)"] == "TOMB. APROV."
            or row["Estágio da Instrução (Portaria 11/86)"] == "TOMBADO"
        ):
            sicg.append(row["CÓDIGO IPHAN"].strip().replace("-", "").replace(" ", ""))

    # Carregar os bens materiais no geoserver
    tomb_geoserver = gpd.read_file(
        "https://geoserver.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG%3Atg_bem_classificacao&maxFeatures=2147483647&outputFormat=application%2Fjson"
    )

    # Criar DataFrame vazio para receber os bens filtrados.
    tombados = gpd.GeoDataFrame(columns=tomb_geoserver.columns.to_list())

    for indice, linha in tomb_geoserver.iterrows():
        if linha["co_iphan"] in sicg:
            tombados.loc[len(tombados)] = linha

    return tombados


def normalizar_material(gdf, tipo_bem, geometria):
    """
    Recebe um arquivo com os bens culturais materiais retirados do SICG e\
    normaliza as informações para serem consumidas/exibidas no Patrimônio Brasileiro.

    Args:
        gdf (GeoDataFrame): GeoDataFrame com os bens culturais materiais.
        tipo_bem (String): String com o tipo de bem material sendo normalizado\
            (tombado, valorado ou arqueológico)
        geometria (String): String com a geometria dos bens no GeoDataFrame\
            (ponto ou polígono)

    Returns:
        bens (GeoDataFrame): GeoDataFrame com os bens materiais normalizados no\
            formato esperado pelo Patrimônio Brasileiro.
    """
    # Criar GeoDataFrame vazio para receber os bens normalizados.
    bens = gpd.GeoDataFrame(
        columns=[
            "nome",
            "descricao",
            "ficha",
            "tipo",
            "classificacao",
            "data_protecao",
            "processo_iphan",
            "tipo_geom",
            "geometry",
        ],
        geometry="geometry",
        crs="EPSG:4674",
    )

    # Criar novos campos e atualizar o nome de outros campos do GDF carregado.
    for index, row in gdf.iterrows():
        bem = {}
        bem["nome"] = row["identificacao_bem"]
        bem["descricao"] = row["sintese_bem"]
        bem["ficha"] = f"https://sicg.iphan.gov.br/sicg/bem/visualizar/{row['id_bem']}"
        bem["tipo"] = f"{tipo_bem}"
        bem["classificacao"] = row["ds_classificacao"]
        bem["data_protecao"] = None
        bem["processo_iphan"] = None
        bem["tipo_geom"] = f"{geometria}"
        bem["geometry"] = row["geometry"]
        bens.loc[len(bens)] = bem
    # Retornar o GeoDataFrame normalizado.
    return bens


def normalizar_imaterial_sicg(gdf, tipo_bem, geometria):
    """
    Recebe um arquivo com os bens culturais imateriais retirados do SICG e\
    normaliza as informações para serem consumidas/exibidas no Patrimônio Brasileiro.

    Args:
        gdf (GeoDataFrame): GeoDataFrame com os bens culturais imateriais.
        tipo_bem (String): String com o tipo de bem imaterial sendo normalizado\
            (tombado, valorado ou arqueológico)
        geometria (String): String com a geometria dos bens no GeoDataFrame\
            (ponto ou polígono)

    Returns:
        bens (GeoDataFrame): GeoDataFrame com os bens imateriais normalizados no\
            formato esperado pelo Patrimônio Brasileiro.
    """
    # Criar GeoDataFrame vazio para receber os bens normalizados.
    bens = gpd.GeoDataFrame(
        columns=[
            "nome",
            "descricao",
            "ficha",
            "tipo",
            "classificacao",
            "data_protecao",
            "processo_iphan",
            "tipo_geom",
            "geometry",
        ],
        geometry="geometry",
        crs="EPSG:4674",
    )

    # Criar novos campos e atualizar o nome de outros campos do GDF carregado.
    for index, row in gdf.iterrows():
        bem = {}
        bem["nome"] = row["no_bem_imaterial"]
        bem["descricao"] = row["ds_bem_imaterial"]
        bem["ficha"] = f"https://sicg.iphan.gov.br/sicg/bemImaterial/acao/{
            row['id_bem_imaterial']
        }"
        bem["tipo"] = f"{tipo_bem}"
        bem["classificacao"] = None
        bem["data_protecao"] = None
        bem["processo_iphan"] = None
        bem["tipo_geom"] = f"{geometria}"
        bem["geometry"] = row["geometry"]
        bens.loc[len(bens)] = bem
    # Retornar o GeoDataFrame normalizado.
    return bens


def normalizar_imaterial_bcr(gdf, tipo_bem, geometria):
    """
    Recebe um arquivo com os bens culturais imateriais retirados do BCR e\
    normaliza as informações para serem consumidas/exibidas no Patrimônio Brasileiro.

    Args:
        gdf (GeoDataFrame): GeoDataFrame com os bens culturais imateriais.
        tipo_bem (String): String com o tipo de bem imaterial sendo normalizado\
            (tombado, valorado ou arqueológico)
        geometria (String): String com a geometria dos bens no GeoDataFrame\
            (ponto ou polígono)

    Returns:
        bens (GeoDataFrame): GeoDataFrame com os bens imateriais normalizados no\
            formato esperado pelo Patrimônio Brasileiro.
    """
    # Criar GeoDataFrame vazio para receber os bens normalizados.
    bens = gpd.GeoDataFrame(
        columns=[
            "nome",
            "descricao",
            "ficha",
            "tipo",
            "classificacao",
            "data_protecao",
            "processo_iphan",
            "tipo_geom",
            "geometry",
        ],
        geometry="geometry",
        crs="EPSG:4674",
    )

    # Criar novos campos e atualizar o nome de outros campos do GDF carregado.
    for index, row in gdf.iterrows():
        bem = {}
        bem["nome"] = row["identificacao_bem"]
        bem["descricao"] = None
        bem["ficha"] = row["ficha"]
        bem["tipo"] = f"{tipo_bem}"
        bem["classificacao"] = None
        bem["data_protecao"] = None
        bem["processo_iphan"] = None
        bem["tipo_geom"] = f"{geometria}"
        bem["geometry"] = row["geometry"]
        bens.loc[len(bens)] = bem
    # Retornar o GeoDataFrame normalizado.
    return bens


def adicionar_municipio(gdf):
    # Carregar GDF dos municípios brasileiros (fonte: IBGE).
    municipios = gpd.read_file("https://geoservicos.ibge.gov.br/geoserverIBGE/CGMAT/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=CGMAT%3Apbqg22_04_Municipios_cd_mun&outputFormat=application%2Fjson&maxFeatures=600000")
    # Definir crs do GDF de municípios.
    municipios.set_crs("EPSG:4674", inplace=True)

    # Inserir dados de Estado e município nos GDF dos bens na geometria ponto.
    bens_muni_uf = gdf.sjoin(df=municipios, how="inner", predicate="intersects")
    # Definir crs do novo GDF.
    bens_muni_uf.set_crs("EPSG:4674", inplace=True)
    # Renomear colunas de Estado e município.
    bens_muni_uf.rename(
        columns={
            "nm_mun": "municipio",
            "sigla_uf": "uf",
        },
        inplace=True,
    )

    # Excluir colunas desnecessárias vindas do GDF de municípios.
    bens_muni_uf.drop(
        columns=[
            "cd_recorte",
            "quadro",
            "cd_uf",
            "cd_mun",
        ],
        inplace=True,
    )

    return bens_muni_uf
