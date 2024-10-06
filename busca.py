import csv
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
    raise NotImplementedError("Aguardando inserção do Imaterial no Geoserver.")
#     imaterial = gpd.read_file(URL DO IMATERIAL NO GEOSERVER)
#     busca = gpd.read_file(poligono)
#     imat_pol = gpd.overlay(imaterial, busca, how="intersection")
#     busca_dict = imat_pol.to_geo_dict()
#     for bem in busca_dict["titulo"]:
#         print(f"\nNome: {bem["data"]["titulo-25"]["value"]}\n>>> Ficha: {bem["url"]}\n")
