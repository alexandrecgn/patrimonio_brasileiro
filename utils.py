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


def pesquisar(area):
    """
    consulta o Geoserver Iphan para verificar se existem Bens
    Culturais Acautelados na área do polígono de busca através
    da consulta aos dados oficiais do Iphan.

    Args:
        poligono (GeoDataFrame): polígono contendo a área na qual
        se pretende fazer a busca por bens culturais.

        base_bens (string): string com a URL da base de dados a ser
        consultada.

    Return:
        GeoDataFrame: Recorte dos bens culturais, na geomtria polígono,
        identificados dentro da área de busca.
        GeoDataFrame: Recorte dos bens culturais, na geomtria ponto,
        identificados dentro da área de busca.
    """
    busca = gpd.read_file(area)
    bens_pol = gpd.read_file("bens/bens_pol.gpkg")
    bens_pt = gpd.read_file("bens/bens_pt.gpkg")
    resultado_pol = gpd.overlay(
        busca, bens_pol, how="intersection", keep_geom_type=False
    )
    resultado_pt = gpd.overlay(
        busca, bens_pt, how="intersection", keep_geom_type=False)
    return resultado_pol, resultado_pt


def normalizar_material(gdf, tipo_bem, geometria):
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

    for index, row in gdf.iterrows():
        bem = {}
        bem["nome"] = row["identificacao_bem"]
        bem["descricao"] = row["sintese_bem"]
        bem["ficha"] = f"https://sicg.iphan.gov.br/sicg/bem/visualizar/{
            row['id_bem']}"
        bem["tipo"] = f"{tipo_bem}"
        bem["classificacao"] = row["ds_classificacao"]
        bem["data_protecao"] = None
        bem["processo_iphan"] = None
        bem["tipo_geom"] = f"{geometria}"
        bem["geometry"] = row["geometry"]
        bens.loc[len(bens)] = bem
    return bens


def normalizar_imaterial_sicg(gdf, tipo_bem, geometria):
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
    return bens


def normalizar_imaterial_bcr(gdf, tipo_bem, geometria):
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
    return bens
