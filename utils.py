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
        
        base_bens (string): string com a URL da base de dados a ser
        consultada.
    
    Return:
        GeoDataFrame: Recorte dos bens culturais identificados dentro
        da área de busca.
    """
    busca = gpd.read_file(area)
    bens_culturais = gpd.read_file(base_bens)
    bens = gpd.overlay(busca, bens_culturais, how="intersection", keep_geom_type=False)
    if "dt_cadastro" in bens.columns:
        bens = bens.drop(columns=["dt_cadastro"])
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

def refinar_arqueologico(resultado):
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


def refinar(resultado):
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
        nome = bem["properties"]["identificacao_bem"]
        ficha = bem["properties"]["ficha"]
        refinar.append({"Nome do bem": nome, "Ficha do bem": ficha})
    refinado = pd.DataFrame(refinar)
    return refinado


def dataframes_finais(area):
    """_summary_

    Args:
        area (_type_): _description_

    Returns:
        _type_: _description_
    """
    base_sitios_pt = "http://portal.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG%3Asitios&maxFeatures=2147483647&outputFormat=application%2Fjson"
    base_sitios_pol = "https://geoserver.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG%3Asitios_pol&maxFeatures=2147483647&outputFormat=application%2Fjson"
    base_imaterial_pol = "https://raw.githubusercontent.com/alexandrecgn/patrimonio_brasileiro/refs/heads/main/bens/imaterial_pol.geojson"
    base_imaterial_pt = "https://raw.githubusercontent.com/alexandrecgn/patrimonio_brasileiro/refs/heads/main/bens/imaterial_pt.geojson"
    base_tombados = "https://raw.githubusercontent.com/alexandrecgn/patrimonio_brasileiro/refs/heads/main/bens/tombados.geojson"
    base_valorados = "https://raw.githubusercontent.com/alexandrecgn/patrimonio_brasileiro/refs/heads/main/bens/valorados.geojson"

    sitios_pt = pesquisar(area, base_sitios_pt)
    sitios_pol = pesquisar(area, base_sitios_pol)
    imaterial_pol = pesquisar(area, base_imaterial_pol)
    imaterial_pt = pesquisar(area, base_imaterial_pt)
    tombados = pesquisar(area, base_tombados)
    valorados = pesquisar(area, base_valorados)

    sit_pt_dict = to_dict(sitios_pt)
    sit_pol_dict = to_dict(sitios_pol)
    imapol_dict = to_dict(imaterial_pol)
    imapt_dict = to_dict(imaterial_pt)
    tom_dict = to_dict(tombados)
    val_dict = to_dict(valorados)

    tab_sit_pt = refinar_arqueologico(sit_pt_dict)
    tab_sit_pol = refinar_arqueologico(sit_pol_dict)
    stpol = pd.DataFrame(tab_sit_pt)
    stpt = pd.DataFrame(tab_sit_pol)
    tab_st_tot = pd.concat([stpol, stpt])

    tab_imtpol = refinar(imapol_dict)
    tab_imtpt = refinar(imapt_dict)
    impol = pd.DataFrame(tab_imtpol)
    impt = pd.DataFrame(tab_imtpt)
    tab_im_tot = pd.concat([impol, impt])
    
    tab_tmb = refinar(tom_dict)
    
    tab_val = refinar(val_dict)

    return sitios_pt, sitios_pol, imaterial_pol, imaterial_pt, tombados, valorados, tab_st_tot, tab_sit_pt, tab_sit_pol, tab_im_tot, tab_imtpol, tab_imtpt, tab_tmb, tab_val