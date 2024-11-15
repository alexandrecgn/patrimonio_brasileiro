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

import sys
import pandas
from busca import pesquisar, to_dict, refinar_material, refinar_imaterial


base_sitios = "http://portal.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG%3Asitios&maxFeatures=2147483647&outputFormat=application%2Fjson"
base_imaterial = "https://raw.githubusercontent.com/alexandrecgn/buscador_patrimonio/refs/heads/main/web/bens/imaterial.geojson"
base_tombados = "https://raw.githubusercontent.com/alexandrecgn/buscador_patrimonio/refs/heads/main/web/bens/tombados.geojson"
base_valorados = "https://raw.githubusercontent.com/alexandrecgn/buscador_patrimonio/refs/heads/main/web/bens/valorados.geojson"


def main():
    area = sys.argv[1]

    print("\nBuscando bens culturais\n")

    sitios = pesquisar(area, base_sitios)
    imaterial = pesquisar(area, base_imaterial)
    tombados = pesquisar(area, base_tombados)
    valorados = pesquisar(area, base_valorados)

    sit_dt = refinar_material(to_dict(sitios))
    ima_dt = refinar_imaterial(to_dict(imaterial))
    tom_dt = refinar_material(to_dict(tombados))
    val_dt = refinar_material(to_dict(valorados))

    print("\nSalvando listas de bens encontrados")

    sit_dt.to_csv("Patrimônio Arqueológico")
    ima_dt.to_csv("Patrimônio Imaterial")
    tom_dt.to_csv("Patrimônio Tombado")
    val_dt.to_csv("Patrimônio Valorado")


if __name__ == "__main__":
    main()