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


import csv
import geopandas as gpd


def get_bens(poligono):
    """
    Esta função consulta o Geoserver Iphan para verificar se existem
    sítios arqueológicos cadastrados ou Bens Imateriais Registrados na
    área do polígono de busca e chama as funções sitios_csv() e imat_csv()
    para salvar as informações dos bens interceptados.

    Args:
        poligono (GeoDataFrame): polígono contendo a área na qual se
        pretende fazer a busca por bens culturais.
    
    Return: GeoDict
    """
    sitios = gpd.read_file("http://portal.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG%3Asitios&maxFeatures=2147483647&outputFormat=application%2Fjson")
    registrados = gpd.read_file("bens/imaterial.geojson")
    tombados = gpd.read_file("bens/tombados.geojson")
    busca = gpd.read_file(poligono)
    st_pol = gpd.overlay(sitios, busca, how="intersection")
    rg_pol = gpd.overlay(registrados, busca, how="intersection")
    tb_pol = gpd.overlay(tombados, busca, how="intersection")
    sitios_dict = st_pol.to_geo_dict()
    rg_dict = rg_pol.to_geo_dict()
    tb_dict = tb_pol.to_geo_dict()
    return sitios_dict, rg_dict, tb_dict


def mat_csv(busca_dict):
    """
    Esta função salva os bens materiais encontrados na área de
    busca em um arquivo CSV contendo o nome e link para ficha SICG de
    cada bem.

    Args:
        busca_dict (GeoDict): dicionário contendo as informações dos 
        Bens Culturais Materiais encontrados na área de busca.
    
    Return: None
    """
    with open("bens_materiais.csv", "a", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=["Nome", "Ficha"])
        writer.writeheader()
        for bem in busca_dict["features"]:
            nome = bem['properties']['identificacao_bem']
            ficha = f"https://sicg.iphan.gov.br/sicg/bem/visualizar/{bem['properties']['id_bem']}"
            writer.writerow({"Nome": nome, "Ficha": ficha})


def imat_csv(rg_dict):
    """
    Esta função salva os bens imateriais encontrados na área de
    busca em um arquivo CSV contendo o nome e link para ficha BCR de
    cada bem.

    Args:
        rg_dict (GeoDict): dicionário contendo as informações
        presentes no geopackage de Patrimônio Imaterial acerca
        dos bens na área de busca.
    
     Return: None
    """
    with open("bens_imateriais.csv", "a", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=["Nome", "Ficha"])
        writer.writeheader()
        for cada in rg_dict["features"]:
            nome = cada["properties"]["titulo"]
            ficha = cada["properties"]["bcr"]
            writer.writerow({"Nome": nome, "Ficha": ficha})
