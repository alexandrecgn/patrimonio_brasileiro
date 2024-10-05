import csv
import geopandas as gpd


# Verifica se a área inserida se sobrepõe a algum ponto na camada
# de sítios arqueológicos no geoserver do Iphan.
def get_sitios(poligono):
    sitios = gpd.read_file(
        "http://portal.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG%3Asitios&maxFeatures=2147483647&outputFormat=application%2Fjson"
    )
    busca = gpd.read_file(poligono)
    st_pol = gpd.overlay(sitios, busca, how="intersection")
    busca_dict = st_pol.to_geo_dict()
    sitios_csv(busca_dict)

#Salva os bens identificados na área em csv
def sitios_csv(busca_dict):
    with open("sitios_csv.csv", "w", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=["Nome", "Ficha"])
        writer.writeheader()
    with open("sitios_csv.csv", "a", encoding="utf-8") as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=["Nome", "Ficha"])
        for sitio in busca_dict["features"]:
            nome = sitio['properties']['identificacao_bem']
            ficha = f"https://sicg.iphan.gov.br/sicg/bem/visualizar/{sitio['properties']['id_bem']}"
            writer.writerow({"Nome": nome, "Ficha": ficha})


# def get_imaterial(poligono):
#     imaterial = gpd.read_file(URL DO IMATERIAL NO GEOSERVER)
#     busca = gpd.read_file(poligono)
#     imat_pol = gpd.overlay(imaterial, busca, how="intersection")
#     busca_dict = imat_pol.to_geo_dict()
#     for bem in busca_dict["titulo"]:
#         print(f"\nNome: {bem["data"]["titulo-25"]["value"]}\n>>> Ficha: {bem["url"]}\n")
