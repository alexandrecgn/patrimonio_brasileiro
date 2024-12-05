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

sicg = []

with open("bens_tombados_[cod_sicg].csv", "r") as codigos:
    reader = csv.DictReader(codigos)
    for item in reader:
        sicg.append(item["CÓDIGO IPHAN"])


with open("tg_bem_classificacao.csv", "r") as geoserver, open("tombados.csv", "a") as tombados:
    reader = csv.DictReader(geoserver)
    writer = csv.DictWriter(tombados, fieldnames=["FID","ponto","id_bem","identificacao_bem","co_iphan","no_logradouro","nu_logradouro","id_natureza","ds_natureza","codigo_iphan","id_classificacao","ds_classificacao","id_tipo_bem","ds_tipo_bem","sg_tipo_bem","sintese_bem","dt_cadastro"])
    writer.writeheader()
    for bem in reader:
        if bem["co_iphan"] in sicg:
            writer.writerow(bem)