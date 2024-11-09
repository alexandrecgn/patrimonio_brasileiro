import geopandas as gpd
import pandas as pd


def pesquisar(area, base_bens):
    busca = gpd.read_file(area)
    bens_culturais = gpd.read_file(base_bens)
    bens = gpd.overlay(busca, bens_culturais, how="intersection", keep_geom_type=False)
    resultado = bens.to_geo_dict()
    return resultado


def refinar_material(resultado, tipo_bem):
    refinar = []
    for bem in resultado["features"]:
        nome = bem['properties']['identificacao_bem']
        tipo = tipo_bem
        ficha = f"https://sicg.iphan.gov.br/sicg/bem/visualizar/{bem['properties']['id_bem']}"
        refinar.append({"Nome do bem": nome, "Tipo de bem": tipo, "Ficha do bem": ficha})
    refinado = pd.DataFrame(refinar)
    return refinado


def refinar_imaterial(resultado):
    refinar = []
    for bem in resultado["features"]:
        nome = bem["properties"]["titulo"]
        tipo = "Patrimônio Imaterial"
        ficha = bem["properties"]["bcr"]
        refinar.append({"Nome do bem": nome, "Tipo de bem": tipo, "Ficha do bem": ficha})
    refinado = pd.DataFrame(refinar)
    return refinado


# base_bens =[
#     {"tipo": "sitios", "base": gpd.read_file("http://portal.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG%3Asitios&maxFeatures=2147483647&outputFormat=application%2Fjson")},
#     {"tipo": "registrados", "base": gpd.read_file("bens/imaterial.geojson")},
#     {"tipo": "tombados", "base": gpd.read_file("bens/tombados.geojson")},
#     {"tipo": "valorados", "tipo": gpd.read_file("bens/valorados.geojson")},
# ]
