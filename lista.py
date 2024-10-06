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

from requests import get


def listar_sitios():
    sitios = get(
        "http://portal.iphan.gov.br/geoserver/SICG/\
            ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG\
                %3Asitios&maxFeatures=2147483647&outputFormat=application%2Fjson",
        timeout=10,
    )
    sitios_json = sitios.json()
    for sitio in sitios_json["features"]:
        print(
            f'\nNome: {sitio["properties"]["identificacao_bem"]}\
                \n>> Ficha: https://sicg.iphan.gov.br/sicg/bem/visualizar/\
                {sitio["properties"]["id_bem"]}\n'
        )


def listar_imaterial():
    imaterial = get(
        "https://bcr.iphan.gov.br/wp-json/tainacan/v2/items/?perpage=96&order=ASC&orderby=date&metaquery%5B0%5D%5Bkey%5D=\
                1850&metaquery%5B0%5D%5Bvalue%5D%5B0%5D=65733&metaquery%5B0%5D%5Bcompare%5D=IN&exposer=json-flat&paged=1",
        timeout=50,
    )
    imaterial_json = imaterial.json()
    for ben_registrado in imaterial_json["items"]:
        print(
            f'\nNome: {ben_registrado["data"]["titulo-25"]["value"]}\
                \n>> Ficha: {ben_registrado["url"]}\n'
        )

listar_imaterial()