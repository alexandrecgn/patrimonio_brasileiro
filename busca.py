"""
Copyright© 2024 Alexandre Cavalcanti

    This file is part of "Buscador do Patrimônio".

    "Buscador do Patrimônio" is free software: you can redistribute
    it and/or modify it under the terms of the GNU General Public
    License as published by the Free Software Foundation, either version
    3 of the License, or (at your option) any later version.

    "Buscador do Patrimônio" is distributed in the hope that it will
    be useful, but WITHOUT ANY WARRANTY; without even the implied
    warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with "Buscador do Patrimônio". If not, see <https://www.gnu.org/licenses/>. 

"""

import geopandas as gpd
import pandas as pd


def pesquisar(area, base_bens):
    """
    consulta o Geoserver Iphan para verificar se existem Bens
    Culturais Acautelados na área do polígono de busca através
    da consulta aos dados oficiais do Iphan.

    Args:
        poligono (GeoDataFrame): polígono contendo a área na qual
        se pretende fazer a busca por bens culturais.
    
    Return:
        GeoDataFrame: Recorte dos bens culturais identificados dentro
        da área de busca.
    """
    busca = gpd.read_file(area)
    bens_culturais = gpd.read_file(base_bens)
    bens = gpd.overlay(busca, bens_culturais, how="intersection", keep_geom_type=False)
    return bens


def to_dict(bens):
    """
    Converte o objeto de entrada de GeoDataFrame para GeoDict.

    Args:
        bens (GeoDataFrame): Recorte dos bens culturais identificados
        dentro da área de busca.

    Returns:
        GeoDict: O mesmo conteúdo do objeto de entrada, mas no formato
        de dicionário georreferenciado.
    """
    resultado = bens.to_geo_dict()
    return resultado

def refinar_material(resultado):
    """
    Seleciona o nome do bem cultural material e seu código SICG para gerar
    um DataFrame com o nome e link da ficha de cadastro de cada bem.

    Args:
        resultado (GeoDict): Dicinário georreferenciado contendo o resultado
        da busca por bens culturais.

    Returns:
        DataFrame: Objeto contendo o nome do bem cultural e o link para sua
        ficha no Sistema Integrado de Conhecimento e Gestão - SICG/IPHAN.
    """
    refinar = []
    for bem in resultado["features"]:
        nome = bem['properties']['identificacao_bem']
        ficha = f"https://sicg.iphan.gov.br/sicg/bem/visualizar/{bem['properties']['id_bem']}"
        refinar.append({"Nome do bem": nome, "Ficha do bem": ficha})
    refinado = pd.DataFrame(refinar)
    return refinado


def refinar_imaterial(resultado):
    """
    Seleciona o nome do bem cultural imaterial e o link para sua ficha no BCR
    para gerar um DataFrame com essas informações.

    Args:
        resultado (GeoDict): Dicinário georreferenciado contendo o resultado
        da busca por bens culturais.

    Returns:
        DataFrame: Objeto contendo o nome do bem cultural e o link para sua
        ficha no Banco de Bens Culturais Registrados - BCR/IPHAN.
    """
    refinar = []
    for bem in resultado["features"]:
        nome = bem["properties"]["titulo"]
        ficha = bem["properties"]["bcr"]
        refinar.append({"Nome do bem": nome, "Ficha do bem": ficha})
    refinado = pd.DataFrame(refinar)
    return refinado
