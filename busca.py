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
import requests
from sys import argv
import geopandas as gpd


def get_sitios(poligono):
    """
    Esta função consulta o Geoserver Iphan para verificar se existem
    sítios arqueológicos cadastrados na área do polígono de busca e
    chama a função sitios_csv() para salvar as informações dos sítios.

    Args:
        poligono (GeoDataFrame): polígono contendo a área na qual se
        pretende fazer a busca por bens culturais.
    Return: None
    """
    geoserver = gpd.read_file("http://portal.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG%3Asitios&maxFeatures=2147483647&outputFormat=application%2Fjson")
    busca = gpd.read_file(poligono)
    st_pol = gpd.overlay(geoserver, busca, how="intersection")
    sitios_dict = st_pol.to_geo_dict()
    sitios_csv(sitios_dict)


def sitios_csv(busca_dict):
    """
    Esta função salva os sítios arqueológicos encontrados na área de
    busca em um arquivo CSV contendo o nome e link para ficha SICG de
    cada sítio.

    Args:
        busca_dict (GeoDict): dicionário contendo as informações
        presentes no Geoserver Iphan acerca dos sítios identificados
        na área de busca.
    Retrurn: None
    """
    with open("sitios_csv.csv", "w", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=["Nome", "Ficha"])
        writer.writeheader()
    with open("sitios_csv.csv", "a", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=["Nome", "Ficha"])
        for sitio in busca_dict["features"]:
            nome = sitio['properties']['identificacao_bem']
            ficha = f"https://sicg.iphan.gov.br/sicg/bem/visualizar/{sitio['properties']['id_bem']}"
            writer.writerow({"Nome": nome, "Ficha": ficha})


def get_imaterial(poligono):
    registrados = gpd.read_file("test/bens_registrados_poligono_[tratado].gpkg")
    busca = gpd.read_file(poligono)
    rg_pol = gpd.overlay(registrados, busca, how="intersection")
    rg_dict = rg_pol.to_geo_dict()
    imat_csv(rg_dict)

def imat_csv(rg_dict):
    with open("imat_csv.csv", "w", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=["Nome", "Ficha"])
        writer.writeheader()
        with open("imat_csv.csv", "a", encoding="utf-8") as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=["Nome", "Ficha"])
            for cada in rg_dict["features"]:
                nome = cada["properties"]["titulo"]
                ficha = get_ficha_imat(nome)
                writer.writerow({"Nome": nome, "Ficha": ficha})


def get_ficha_imat(bem):
    bcr = requests.get("https://bcr.iphan.gov.br/wp-json/tainacan/v2/items/?perpage=96&order=ASC&orderby=date&metaquery%5B0%5D%5Bkey%5D=1850&metaquery%5B0%5D%5Bvalue%5D%5B0%5D=65733&metaquery%5B0%5D%5Bcompare%5D=IN&exposer=json-flat&paged=1")
    bcr_j = bcr.json()
    bens = []
    for item in bcr_j["items"]:
        bens.append(dict(nome=item["data"]["titulo-25"], ficha=item["url"]))
    for cada in bens:
        if cada["nome"] == bem:
            return cada["ficha"]
        else:
            return "Ficha não encontrada"


if __name__ == "__main__":
    print("Buscando Sítios Arqueológicos Cadastrados")
    get_sitios(argv[1])
    print("Salvando lista de Sítios Arqueológicos")
    print("Buscando Bens Imateriais Registrados")
    get_imaterial(argv[1])
    print("Salvando lista de Bens Registrados")
